import math
import threading
import traceback
from urllib import parse
from uuid import uuid4

import execjs
import requests
import redis
import json
import time
import datetime
from pprint import pprint
import pymysql
from hashlib import md5
import re
import threadpool
import random
from queue import Queue
from math import ceil
from lagou_url_list import start_list
from bs4 import BeautifulSoup, BeautifulStoneSoup


class Parse:
    def __init__(self):
        self.pattern = re.compile(r'(\d+\.*\d*).*?')
        self.company_state_mapping = {'存续': 0, '在业': 1, '吊销': 2, '注销': 3, '迁入': 4, '迁出': 5, '停业': 6, '清算': 7, 8: '其他'}
        self.manage_state = ['存续', '在业', '吊销', '注销', '迁入', '迁出', '停业', '清算']
        self.education = ['初中', '高中', '中专', '中技', '大专', '本科', '硕士', '博士', 'MBA', 'EMBA', '其他']
        self.education_mapping = {'不限': 0, '初中': 1, '高中': 2, '中专': 3, '中技': 3, '大专': 4, '本科': 5, '硕士': 6, '博士': 7,
                                  'MBA': 8, 'EMBA': 8, '其他': 9}

    def parse_work_experience(self, work_experience):
        """
        获取工作经验中的年限，格式化返回
        @param work_experience:
        @return: 工作经验对应的数字
        0: "不限", 1: "无经验", 2: "1年以内", 3: "1-3年", 4: "3-5年", 5: "5-10年", 6: "10年以上", 7:"在校/应届"
        """
        if work_experience == '无经验':
            return 1
        elif work_experience == '不限':
            return 0
        elif '在校' in work_experience or '应届' in work_experience:
            return 7
        work_years = self.pattern.findall(work_experience)
        work_years = [eval(x) for x in work_years if x]
        if len(work_years):
            work_year = max(work_years)
            if work_year <= 1:
                return 2
            elif work_year <= 3:
                return 3
            elif work_year <= 5:
                return 4
            elif (work_year <= 10) and ('以上' not in work_experience):
                return 5
            elif (work_year == 10 and '以上' in work_experience) or (work_year > 10):
                return 6
            else:
                return 0
        else:
            return 0

    def parse_education(self, education):
        """
        根据学位返回学位对应的序号
        @param education: 学位 string
        @return: 学历
        0: "不限", 1: "初中及以下", 2: "高中", 3: "中专/中技", 4: "大专", 5: "本科", 6: "硕士", 7: "博士", 8: "MBA/EMBA", 9: "其他"
        """
        for key in self.education:
            if key in education:
                return self.education_mapping.get(key, 0)
        return 0

    def parse_company_person_num(self, person_number):
        """
        获取公司人数，并对数量进行分类处理
        @param person_number:
        @return: 工作经验对应的数字
        0: 不限, 1: 0-20人, 2: 20-99人, 3: 100-499人, 4: 500-999人, 5: 1000-9999', 6: 10000人以上
        """
        if person_number:
            number_ls = self.pattern.findall(str(person_number))
            number_ls = [eval(x) for x in number_ls if x]
            if len(number_ls):
                person_number = max(number_ls)
                if person_number <= 20:
                    return 1
                elif person_number <= 99:
                    return 2
                elif person_number <= 499:
                    return 3
                elif person_number <= 999:
                    return 4
                elif person_number <= 9999:
                    return 5
                elif person_number > 9999:
                    return 6
            else:
                return 0
        else:
            return 0

    def parse_recruit_num(self, recruit_num):
        """
            从招收人数的字符串中获取招收人数
            @param recruit_num: 招收人数字符串
            @return: 工作经验对应的数字
            """
        number_ls = self.pattern.findall(recruit_num)
        number_ls = [eval(x) for x in number_ls if x]
        if len(number_ls):
            return max(number_ls)
        else:
            return 1

    def parse_salary(self, salary):
        """
        将薪资返回处理成最高薪资，最低薪资，多少薪
        @param salary: 薪资范围字符串
        @return: [最低薪资， 最高薪资， 多少薪]
        """
        if '面议' in salary:
            return [0, 0, 12]
        try:
            salary_list = self.pattern.findall(salary)
            salary_list = [eval(x) for x in salary_list]
            salary_len = len(salary_list)
            if not salary_len:
                return [0, 0, 12]
        except BaseException as e:
            print('Salary parse error:', e)
            return [0, 0, 12]
        if len(salary_list) == 1:
            unit = self.change_unit(salary)
            return self.calculate_salary(salary, salary_list[0], salary_list[0], unit, unit, 12)
        elif len(salary_list) == 2:
            if '薪' in salary and '月薪' not in salary and '年薪' not in salary:
                unit = self.change_unit(salary)
                return self.calculate_salary(salary, salary_list[0], salary_list[0], unit, unit, salary_list[1])
            else:
                s0 = str(salary_list[0]).replace('.', r'\.')
                s1 = str(salary_list[1]).replace('.', r'\.')
                unit_1 = self.change_unit(
                    re.search(r'%s(\S+?)\s?' % s0, salary).group(1))
                try:
                    if salary_list[1] == salary_list[0]:
                        unit_2 = self.change_unit(re.search(r'.*%s(\S+?)' % s1, salary).group(1))
                    else:
                        unit_2 = self.change_unit(
                            re.search(r'%s(\S+?)' % s1, salary.replace(str(salary_list[0]), '', 1)).group(1))
                except AttributeError as e:
                    print(e)
                    unit_2 = 1
                return self.calculate_salary(salary, salary_list[0], salary_list[1], unit_1, unit_2, 12)
        elif len(salary_list) == 3:
            s0 = str(salary_list[0]).replace('.', r'\.')
            s1 = str(salary_list[1]).replace('.', r'\.')
            unit_1 = self.change_unit(
                re.search(r'%s(\S+?)\s?' % s0, salary).group(1))
            if salary_list[1] == salary_list[0]:
                unit_2 = self.change_unit(re.search(r'%s.*?%s(\S+?)\s?' % (s0, s1), salary).group(1))
            else:
                unit_2 = self.change_unit(
                    re.search(r'%s(\S+?)' % s1, salary.replace(str(salary_list[0]), '', 1)).group(1))
            return self.calculate_salary(salary, salary_list[0], salary_list[1], unit_1, unit_2, salary_list[2])
        else:
            return [0, 0, 12]

    def change_unit(self, unit_value):
        """
        转换单位为数字
        :param unit_value:
        :return: unit (int)
        """
        if 'k' in unit_value or 'K' in unit_value or '千' in unit_value:
            return 1000
        elif '百万' in unit_value or '百萬' in unit_value:
            return 1000000
        elif '百' in unit_value:
            return 100
        elif '万' in unit_value or '萬' in unit_value:
            return 10000
        else:
            return 1

    def calculate_salary(self, salary, minSalary, maxSalary, unit_min, unit_max, much_salary):
        if unit_min == 1 and minSalary <= maxSalary:
            unit_min = unit_max
        if '天' in salary:
            return [minSalary * unit_min * 21.75, maxSalary * unit_max * 21.75, much_salary]
        elif '周' in salary:
            return [minSalary * unit_min * 4, maxSalary * unit_max * 4, much_salary]
        elif '年' in salary:
            return [minSalary * unit_min // 12, maxSalary * unit_max // 12, much_salary]
        elif '时' in salary or '時' in salary:
            return [minSalary * unit_min * 174, maxSalary * unit_max * 174, much_salary]
        else:
            return [minSalary * unit_min, maxSalary * unit_max, much_salary]

    def parse_manage_state(self, state):
        """
        格式化处理公司用运行的状态
        @param state: 公司运行的状态
        @return:
        """
        for key in self.manage_state:
            if key == '存续':
                list1 = [key, "开业", "正常", "登记"]
                if len([x for x in list1 if x in state]):
                    return self.company_state_mapping.get(key)
            if key == "在业":
                list1 = [key, "在营", "正常", "经营", "在营在册", "有效", "在业在册"]
                if len([x for x in list1 if x in state]):
                    return self.company_state_mapping.get(key)
            if key in state:
                return self.company_state_mapping.get(key)
        return 8

    def parse_date(self, publishdate, default=datetime.date.today()):
        if not publishdate:
            return default
        today = datetime.date.today()
        if '小时前' in publishdate or '分钟前' in publishdate:
            return today
        elif '天前' in publishdate:
            d_day = re.search(r'(\d+)天前', publishdate).group(1)
            return today - datetime.timedelta(days=int(d_day))
        elif '年' in publishdate and '月' in publishdate and '日' in publishdate:
            d = re.search(r'(\d+)年(\d+)月(\d+)日', publishdate)
            if len(d.group(1)) == 2:
                return datetime.date(year=int('20' + d.group(1)), month=int(d.group(2)), day=int(d.group(3)))
            elif len(d.group(1)) == 4:
                return datetime.date(year=int(d.group(1)), month=int(d.group(2)), day=int(d.group(3)))
            else:
                return datetime.date(year=today.year, month=int(d.group(2)), day=int(d.group(3)))
        elif '月' in publishdate and '日' in publishdate:
            d = re.search(r'(\d+)月(\d+)日', publishdate)
            return datetime.date(year=today.year, month=int(d.group(1)), day=int(d.group(2)))
        elif '-' in publishdate or '/' in publishdate:
            if '-' in publishdate:
                date_list = publishdate.split('-')
            else:
                date_list = publishdate.split('/')
            if len(date_list) == 2:
                return datetime.date(today.year, int(date_list[0]), int(date_list[1]))
            elif len(date_list) == 3:
                if len(date_list[0]) == 2:
                    y = int('20' + date_list[0])
                elif len(date_list[0]) == 4:
                    y = int(date_list[0])
                else:
                    y = today.year
                return datetime.date(y, int(date_list[1]), int(date_list[2]))
            else:
                return today
        else:
            return default

    def last_date(self, update_time):
        if update_time.month == 1:
            return update_time.year - 1, 12
        else:
            return update_time.year, update_time.month - 1

class SqlQueue:  # mysql长连接类
    def __init__(self, host="localhost", user="root", password="123456", database="pa1"):
        """
        初次链接，存放链接属性
        :param host: 数据库ip地址
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名称
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = 'utf8'
        self.q = Queue(maxsize=5)
        for i in range(0, 5):
            db = pymysql.connect(host=host, user=user, password=password, database=database,
                                 charset='utf8')  # 打开数据库连接
            self.q.put(db)

    def test_conn(self, db):
        """
        测试是否断开链接，并重连
        """
        # noinspection PyBroadException
        try:
            db.ping()  # 运行ping函数，判断是否断开链接
            return True
        except BaseException:
            return False

    def select(self, sql, fetch_one=False):
        """
        查询模块
        :param sql: 查询语句
        :param fetch_one: 是否查询单条
        :return: sql查询结果
        """
        results = None
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        if not self.test_conn(db):
            db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.database, charset=self.charset)  # 重连数据库
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 使用cursor()方法获取操作游标
        try:
            cursor.execute(sql)  # 执行SQL语句
            if fetch_one:
                results = cursor.fetchone()
            else:
                results = cursor.fetchall()  # 获取所有记录列表
            # print('查询成功')
        except BaseException as e:
            print("Error: unable to fetch data", e)
        finally:
            self.q.put(db)
        return results

    def insert(self, sql, data=None):
        """
        新增
        :param sql:插入语句
        :param data: 插入的数据列表
        :return: 最新id
        """
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        if not self.test_conn(db):
            db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.database, charset=self.charset)  # 重连数据库
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 使用cursor()方法获取操作游标
        try:
            if data:
                cursor.execute(sql, data)  # 执行SQL语句
            else:
                cursor.execute(sql)  # 执行SQL语句
            db.commit()  # 提交到数据库执行
            # print('插入成功')
            return cursor.lastrowid
        except BaseException as e:
            print('Error: ', e)
            db.rollback()  # 发生错误时回滚
        finally:
            self.q.put(db)

    def __del__(self):
        """
        断开数据库链接
        """
        try:
            while True:
                self.q.get().close()
                if self.q.empty():
                    break
        except BaseException as e:
            print(e)

class GetProxy(object):
    def __init__(self):
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.failed_proxies = set()
        self.proxies = []
        threading.Thread(target=self.get_proxies, daemon=True).start()

    def get_proxy(self):
        while True:
            if self.proxies:
                return random.choice(self.proxies)
            else:
                print('未获取到代理ip,重试中...')
            time.sleep(2)

    def get_proxies(self, proxy_type='short'):
        if proxy_type == 'long':
            proxy_key = 'proxies'  # use_proxies
        else:
            proxy_key = 'use_proxies'  # use_proxies
        while True:
            try:
                self.proxies = self.client.lrange('use_proxies', 0, -1)
                self.failed_proxies = set(self.proxies) & self.failed_proxies
                self.proxies = [x for x in self.proxies if x not in self.failed_proxies]
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    raise KeyboardInterrupt(e)
                print(e)
            time.sleep(2)

    def add_failed_proxy(self, proxy):
        if proxy not in self.failed_proxies:
            self.failed_proxies.add(proxy)
            self.proxies = [x for x in self.proxies if x not in self.failed_proxies]

class Spider:
    def __init__(self):
        self.spider_name = '/'.join(__file__.split('/')[-2:])
        self.proxy_pool = GetProxy()
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Referer": "http://www.jyzhaopin.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.p = Parse()
        self.sql = SqlQueue(host='10.86.0.107', user='root', password='wit123456', database='lagouhr')
        self.sql_company_id = "SELECT" + " id FROM company.company_info WHERE companyUrl = '%s' OR companyName = '%s' "
        self.sql_company = "INSERT" + """ INTO company.company_info (companyName,companyUrl,companyType,companyIndustry,companyPersonNum,update_time,address)
                VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        self.url = 'https://www.lagou.com/wn/jobs?'
        self.key_list = ['lg_cookie1', 'lg_cookie2', 'lg_cookie3', 'lg_cookie4', 'lg_cookie5']
        self.url_set = set()
        self.m = str(datetime.date.today().month).zfill(2)
        self.get_lg_stoken()
        self.thread_proxy_map = {}

    def get_lg_stoken(self, timeout=8):
        while True:
            proxy = self.proxy_pool.get_proxy()
            try:
                original_data = {
                    "city": "全国",  # 城市范围
                    "kd": "Java",  # 关键词
                }
                # 获取 cookie 中的 __lg_stoken__
                token_url = "https://www.lagou.com/wn/jobs"
                token_headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Referer": "http://www.jyzhaopin.com/",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "cross-site",
                    "Sec-Fetch-User": "?1",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Windows\""
                }
                params = {
                    "kd": original_data["kd"],
                    "city": original_data["city"]
                }
                # proxies = {'http://': proxy, 'https://': proxy}
                proxies = {'http': f"http://{proxy}", 'https': f"http://{proxy}"}
                token_response = requests.get(url=token_url, params=params, headers=token_headers, cookies={},
                                              allow_redirects=False, proxies=proxies, timeout=timeout)
                if token_response.status_code != 302:
                    raise Exception("获取跳转链接异常！检查 global_cookies 是否已包含 __lg_stoken__！")
                # 获取 302 跳转的地址
                security_check_url = token_response.headers["Location"]
                if "login" in security_check_url:
                    raise Exception("IP 被关进小黑屋啦！需要登录！请补全登录后的 Cookie，或者自行添加代理！")
                parse_result = parse.urlparse(security_check_url)
                #ParseResult(scheme='https', netloc='www.lagou.com', path='/utrack/trackMid.html', params='', query='f=https%3A%2F%2Fwww.lagou.com%2Fwn%2Fjobs%3Fkd%3DJava%26city%3D%25E5%2585%25A8%25E5%259B%25BD&t=1667811387&_t=1&_ti=1', fragment='')

                # url 的参数为待加密对象
                security_check_params = parse_result.query
                # 取 name 参数，为混淆 js 的文件名
                security_check_js_name = parse.parse_qs(security_check_params)["name"][0]

                # 发送请求，获取混淆的 js
                js_url = "https://www.lagou.com/common-sec/dist/" + security_check_js_name + ".js"

                js_response = requests.get(url=js_url, headers=token_headers, proxies=proxies, timeout=timeout).text
                # 补全 js，添加 window 参数和一个方法，用于获取 __lg_stoken__ 的值
                lg_js = """
                        window = {
                            "location": {
                                "hostname": "www.lagou.com",
                                "search": '?%s'
                            }
                        }
                        function getLgStoken(){
                            return window.gt.prototype.a()
                        }
                        """ % security_check_params + js_response

                self.ctx = execjs.compile(lg_js)
                print('加密函数生成完成')
                break
            except Exception as e:
                print(e)
                time.sleep(1)
                self.proxy_pool.add_failed_proxy(proxy)

    def update_cookies(self, cookies, response=None):
        if not cookies:
            cookies = {
                '__lg_stoken__': self.ctx.call('getLgStoken'),
                'user_trace_token': datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '-' + re.sub(
                    '(\w{8})(\w{4})(\w{4})(\w{4})(\w+)', '\\1-\\2-\\3-\\4-\\5', uuid4().hex)
            }
        else:
            if response is None:
                pass
            else:
                cookies.update(requests.utils.dict_from_cookiejar(response.cookies))
        return cookies

    def download(self, url, data=None, ii=5):
        print('Downloading: ', parse.unquote(url))
        thread_name = threading.currentThread().getName().replace('-', '')
        thead_map = self.thread_proxy_map.get(thread_name, {})
        proxy = thead_map.get('proxy', self.proxy_pool.get_proxy())
        cookies = thead_map.get('cookies', None)
        # proxies = {'http': 'http://%s' % proxy, 'https': 'https://%s' % proxy}
        proxies = {'http': f"http://{proxy}", 'https': f"http://{proxy}"}
        headers = self.headers
        cookies = self.update_cookies(cookies)
        try:
            response = requests.get(url, headers=headers, proxies=proxies, cookies=cookies, timeout=5)
            time.sleep(0.8)
            response.encoding = 'utf-8'
            text = response.text
            if '您操作太频繁,请稍后再访问' in text or 'dtaccess deny' in text or '页面加载中' in text or '__NEXT_DATA__' not in text:
                self.proxy_pool.add_failed_proxy(proxy)
                self.thread_proxy_map[thread_name] = {'proxy': self.proxy_pool.get_proxy(), 'cookies': None}
                print('您操作太频繁,请稍后再访问')
                if ii > 0:
                    time.sleep(0.5)
                    return self.download(url, data=data, ii=ii - 1)
                return None
            cookies = self.update_cookies(cookies, response)
            self.thread_proxy_map[thread_name] = {'proxy': proxy, 'cookies': cookies}
            return response
        except Exception as e:
            print('error :', e)
            self.proxy_pool.add_failed_proxy(proxy)
            self.thread_proxy_map[thread_name] = {'proxy': self.proxy_pool.get_proxy(), 'cookies': None}
            if ii > 0:
                time.sleep(0.5)
                return self.download(url, data=data, ii=ii - 1)

    def get_list(self, url_items):
        params = {'kd' if key == 'thirdJobType' else key: val for key, val in url_items.items() if
                  key in ['city', 'thirdJobType']}
        query_str = parse.urlencode(params) + '&cl=false&fromSearch=true&px=new'
        origin_url = self.url + query_str
        response = self.download(origin_url, data=params)
        if response is None:
            print(origin_url, '->数据为空')
            return False

        total_count = 1
        try:
            html = BeautifulSoup(response.text, 'lxml')
            json_data = json.loads(html.find('script', {'id': ['__NEXT_DATA__']}).string)
            data_info = json_data.get('props', {}).get('pageProps', {}).get('initData', {}).get('content', {})
            data_list = data_info.get('positionResult', {}).get('result', []) or []
            total_count = data_info.get('positionResult', {}).get('totalCount', 1)
        except Exception as e:
            # print(e)
            print('error_url: ', origin_url)
            traceback.print_exc()
            data_list = []
        if data_list:
            self.get_item_to_sql(data_list, url_items, params=params)
            total_page = 30 if total_count / 15 > 30 else math.ceil(total_count / 15)
            for pn in range(2, total_page + 1):
                params['pn'] = pn
                next_url = origin_url + '&pn=' + str(pn)
                if self.get_next(next_url, next_data=params, url_items=url_items):
                    break

    def get_next(self, next_url, next_data=None, url_items=None):
        response = self.download(next_url, data=next_data)
        if response is None:
            return False
        try:
            html = BeautifulSoup(response.text, 'lxml')
            json_data = json.loads(html.find('script', {'id': ['__NEXT_DATA__']}).string)
            data_info = json_data.get('props', {}).get('pageProps', {}).get('initData', {}).get('content', {})
            data_list = data_info.get('positionResult', {}).get('result', []) or []
        except Exception as e:
            print(e)
            print('error_url: ', next_url)
            traceback.print_exc()
            data_list = []
        return self.get_item_to_sql(data_list, url_items, params=next_data)

    def get_item_to_sql(self, data_list, url_items, params=None):
        print('data_list:', len(data_list), 'city: ', params.get('city', ''), 'job: ', params.get('kd', '')
              , 'pn: ', params.get('pn', 1))
        total = 0
        for data in data_list:
            item = url_items.copy()
            item['update_time'] = datetime.datetime.now()  # 采集时间
            p_y, p_m = self.p.last_date(item['update_time'])

            item['detailUrl'] = 'https://www.lagou.com/jobs/%s.html' % data.get('positionId', "")  # 职位详情地址
            try:
                item['publishTime'] = self.p.parse_date(
                    str(data.get('createTime', time.strftime("%Y-%m-%d ", time.localtime()))[:10]))  # 插入时间
                if item['publishTime'] < datetime.date(year=p_y, month=p_m, day=1):
                    print('根据时间过滤: ', item['detailUrl'])
                    continue
            except AttributeError:
                continue
            if self.url_qc(item['detailUrl']):
                continue
            total += 1
            item['jobName'] = data.get('positionName', '')  # 职位名称
            item['companyName'] = data.get('companyFullName', "")  # 公司名称
            item['companyPersonNum'] = self.p.parse_company_person_num(data.get('companySize', ""))  # 公司规模
            item['companyIndustry'] = data.get('industryField', "")  # 公司行业
            item['companyType'] = data.get('financeStage', '')  # 公司性质
            item['companyUrl'] = 'https://www.lagou.com/gongsi/%s.html' % data.get('companyId', "")  # 公司详情地址

            item['welfare'] = ','.join([x for x in data.get('companyLabelList', [])])  # 公司福利

            item["firstJobType"] = data.get('firstType', '')  # 一级
            item['secondJobType'] = data.get('secondType', '')  # 二级
            item['thirdJobType'] = data.get('thirdType', '')  # 三级

            item['skillRequirement'] = ','.join([x for x in data.get('skillLables', [])])  # 技能要求

            item['city'] = data.get('city', "")  # 工作城市
            salary = data.get('salary', "")
            item['minSalary'], item['maxSalary'], item['muchSalary'] = self.p.parse_salary(salary)  # 薪资范围
            item['workExperience'] = self.p.parse_work_experience(data.get('workYear', ""))  # 工作经验
            item['education'] = self.p.parse_education(data.get('education', ''))  # 学历要求
            try:
                detail_html =  BeautifulSoup(data.get('positionDetail', ''), 'lxml')

                item['jobInfo'] = detail_html.get_text()
            except Exception as e:
                print(e)
                item['jobInfo'] =''
                traceback.print_exc()
            item['companyInfo'] = ''  # 公司详情
            item['workAddress'] = data.get('positionAddress', '')  # 公司详情
            item['company_id'] = self.get_company_id(item)
            if item['company_id']:
                self.insert(item)
            # pprint(item)
            # print('#' * 100)
            # break
        #if len(data_list) < 15 or total <= 1:
        if len(data_list) < 15:
            return True

    def get_company_id(self, item):
        company_id_dict = self.sql.select(self.sql_company_id % (item['companyUrl'], item['companyName']),
                                          fetch_one=True)
        if company_id_dict:
            company_id = company_id_dict.get('id', None)
        else:
            company_id = self.sql.insert(self.sql_company, [
                item['companyName'], item['companyUrl'], item['companyType'], item['companyIndustry'],
                item['companyPersonNum'], item['update_time'], item['workAddress']])
            print('公司数据录入成功'.center(100, '#'))
            if not company_id:
                company_id_dict = self.sql.select(self.sql_company_id % (item['companyUrl'], item['companyName']),
                                                  fetch_one=True)
                company_id = company_id_dict.get('id', None)
        return company_id

    def insert(self, item):
        """
        入库函数
        :return:
        """
        print(self.spider_name.center(100, '='))
        # pprint(item)
        ls = [item.get('jobName'), item['minSalary'], item['maxSalary'], item['city'], item['company_id'],
              datetime.date.today().month]
        item['job_id'] = md5(''.join([str(x) for x in ls]).encode()).hexdigest()
        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        sql_job = "INSERT " + f"""INTO jobinfo_{y}{m} (jobName,minSalary,maxSalary,monthSalary,detailUrl,education,city,
    publishTime,workExperience,firstJobType,secondJobType,thirdJobType,resource,company_id,update_time,job_id)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        sql_job_add = "INSERT " + f""" INTO jobinfo_add_{y}{m} (id,welfare,skillRequirement,update_time,jobInfo,workAddress)
    VALUES (%s,%s,%s,%s,%s,%s);"""
        job_id = self.sql.insert(sql_job, [
            item['jobName'], item['minSalary'], item['maxSalary'], item['muchSalary'], item['detailUrl'],
            item['education'], item['city'], item['publishTime'], item['workExperience'], item["firstJobType"],
            item['secondJobType'], item['thirdJobType'], '6', item['company_id'], item['update_time'],
            item['job_id']])
        if job_id:
            self.sql.insert(sql_job_add, [
                job_id, item['welfare'], item['skillRequirement'], item['update_time'], item['jobInfo'],
                item['workAddress']])
        print('工作数据入库成功'.center(100, '#'))

    def url_qc(self, url):
        # y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        if self.m != m:
            self.url_set.clear()
            self.m = m
        url_md5 = md5(url.encode()).hexdigest()
        if url_md5 in self.url_set:
            print(f"{self.spider_name} url重复: {url}".center(50, "*"))
            return True
        else:
            self.url_set.add(url_md5)
            return False

    def spider_start(self):
        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        url_list = self.sql.select("SELECT " + f"MD5(detailUrl) as url FROM `jobinfo_{y}{m}`")
        for url in url_list:
            self.url_set.add(url['url'])


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor
    global start_list
    print('开始')
    S = Spider()
    S.spider_start()
    pool = ThreadPoolExecutor(16)

    # url_dict = list_url()
    # start_list = [item for item in start_list if item['city'] in {'焦作', }]
    start_list = start_list
    total_length = len(start_list)
    print('列表页数量：', total_length)
    while True:
        if total_length > 0:
            start_time = time.time()
            job_requests = pool.map(S.get_list, start_list)
            for i, req in enumerate(job_requests):
                end_time = time.time()
                print('已完成：{}/{} 占比：{:.2%} \t耗时：{}'.format(i + 1, total_length, (i + 1) / total_length,
                                                           datetime.timedelta(seconds=int(end_time - start_time))))

            else:
                end_time = time.time()
                print('已完成：{}/{} 占比：{:.2%} \t耗时：{}'.format(total_length, total_length, 1,
                                                           datetime.timedelta(seconds=int(end_time - start_time))))
                print('暂停执行 一小时后重新开始'.center(50, "*"))
                time.sleep(60 * 60)
                S.get_lg_stoken()

