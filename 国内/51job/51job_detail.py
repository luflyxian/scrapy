# -*- coding: utf-8 -*-
import json
import threading

import requests
import queue
import redis
import time
import datetime
from pprint import pprint
from bs4 import BeautifulSoup
import execjs
import pymysql
import re
import threadpool
from queue import Queue
import random
from subprocess import Popen

from requests.exceptions import ProxyError
from requests.exceptions import ConnectionError

Popen.__init__.__kwdefaults__['encoding'] = "utf-8"

js = """
    function get_token(arg1){
            var _0x5e8b26 = "3000176000856006061501533003690027800375";

String["prototype"]["hexXor"] = function (_0x4e08d8) {
    var _0x5a5d3b = "";

    for (var _0xe89588 = 0; _0xe89588 < this["length"] && _0xe89588 < _0x4e08d8["length"]; _0xe89588 += 2) {
        var _0x401af1 = parseInt(this["slice"](_0xe89588, _0xe89588 + 2), 16);

        var _0x105f59 = parseInt(_0x4e08d8["slice"](_0xe89588, _0xe89588 + 2), 16);

        var _0x189e2c = (_0x401af1 ^ _0x105f59)["toString"](16);

        if (_0x189e2c["length"] == 1) {
            _0x189e2c = "0" + _0x189e2c;
        }

        _0x5a5d3b += _0x189e2c;
    }

    return _0x5a5d3b;
};

String["prototype"]["unsbox"] = function () {
    var _0x4b082b = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
    var _0x4da0dc = [];
    var _0x12605e = "";

    for (var _0x20a7bf = 0; _0x20a7bf < this["length"]; _0x20a7bf++) {
        var _0x385ee3 = this[_0x20a7bf];

        for (var _0x217721 = 0; _0x217721 < _0x4b082b["length"]; _0x217721++) {
            if (_0x4b082b[_0x217721] == _0x20a7bf + 1) {
                _0x4da0dc[_0x217721] = _0x385ee3;
            }
        }
    }

    _0x12605e = _0x4da0dc["join"]("");
    return _0x12605e;
};

var _0x23a392 = arg1["unsbox"]();

arg2 = _0x23a392["hexXor"](_0x5e8b26);
                return arg2
        }
    """

lock = threading.Lock()


class SqlQueue(object):  # mysql长连接类
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

    def select(self, sql):
        """
        查询模块
        :param sql: 查询语句
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
        return None

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


class Job(object):
    def __init__(self):
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.job_url = "https://jobs.51job.com/tianjin/141279239.html?s=sou_sou_soulb&t=0_0"
        with open('js51.js', "r", encoding='utf8') as f:
            js1 = f.read()
        with open('get_new_url.js', "r", encoding='utf8') as f:
            js2 = f.read()
        self.v1 = execjs.compile(js1
                                 )
        self.v2 = execjs.compile(js)
        self.v3 = execjs.compile(js2)
        self.sql = SqlQueue(host='10.86.0.107', user='root', password='wit123456', database='hrdatabase')
        self.failed_proxies = set()
        self.proxies = []
        self.thread_proxy_map = {}
        # self.q_ip = queue.Queue(maxsize=10)
        # for i in range(0, 10):
        #     self.q_ip.put([self.get_proxy(), None])
        threading.Thread(target=self.get_proxies, daemon=True).start()

        self.y = None
        self.m = None
        # self.cookie_key_q = queue.Queue(maxsize=10)
        # for key in ['cookie_51job_0', 'cookie_51job_1', 'cookie_51job_2', 'cookie_51job_3', 'cookie_51job_4',
        #             'cookie_51job_5', 'cookie_51job_6', 'cookie_51job_7', 'cookie_51job_8', 'cookie_51job_9']:
        #     self.cookie_key_q.put(key)

    def get_proxy(self):
        while True:
            if self.proxies:
                return self.proxies.pop()
            else:
                print('未获取到代理ip,重试中...')
            time.sleep(1)

    def get_proxies(self):
        while True:
            try:
                self.proxies = self.client.lrange('use_proxies', 0, -1)
                self.failed_proxies = set(self.proxies) & self.failed_proxies
                self.proxies = [x for x in self.proxies if x not in self.failed_proxies]
            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    raise KeyboardInterrupt(e)
                print(e)
            time.sleep(1)

    def add_failed_proxy(self, proxy):
        if proxy not in self.failed_proxies:
            self.failed_proxies.add(proxy)
            self.proxies = [x for x in self.proxies if x not in self.failed_proxies]

    def get_cookie(self, proxies, cookies=None):
        print('获取cookie')
        # proxies = {'http': 'http://%s' % proxy, 'https': 'https://%s' % proxy}
        # proxies = {'http': proxy, 'https': proxy}
        try:

            response = requests.get(self.job_url, headers=self.headers, proxies=proxies, timeout=10, cookies=None)
            cookies = cookies or {}
            # cookies.update(response.cookies.get_dict())
            cookies = self.update_cookies(cookies, response=response)
            return cookies
        except BaseException as e:
            # print('cookie页面响应获取失败,报错：', e)
            return None

    def update_cookies(self, cookies, response=None):
        cookie = self.v1.call('get_token')
        cookies = cookies or {}
        cookies.update({i.split('=', 1)[0]: i.split('=', 1)[1] for i in cookie.split('; ') if i.strip()})
        if response is None:
            pass
        else:
            cookies.update(response.cookies.get_dict())
        return cookies

    def download(self, url, ii=3, timedelay=0.7):
        url = (url if 'timestamp' in url else self.v3.call('get_url', url))
        print('Downloading: %s 次数: %s' % (url.split('?')[0], 4 - ii))
        thread_name = threading.currentThread().getName().replace('-', '')

        # while True:
        #     thead_map = self.thread_proxy_map.get(thread_name, {})
        #     proxy = thead_map.get('proxy', self.get_proxy())
        #     cookies = thead_map.get('cookie', None)
        #     proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}
        #
        #     # proxies = {'http': proxy, 'https': proxy}
        #     if cookies:
        #         break
        #
        #     cookies = self.get_cookie(proxies, cookies)
        #
        #     if cookies:
        #         self.thread_proxy_map[thread_name] = {'proxy': proxy, 'cookie': cookies}
        #         break
        #     self.thread_proxy_map[thread_name] = {'proxy': self.get_proxy(), 'cookie': None}
        #     self.add_failed_proxy(proxy)

        thead_map = self.thread_proxy_map.get(thread_name, {})
        proxy = thead_map.get('proxy', self.get_proxy())
        cookies = thead_map.get('cookie', None)
        proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}

        cookies = self.update_cookies(cookies)

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "From-Domain": "51job_web",
            "Origin": "https://we.51job.com",
            "Referer": "https://we.51job.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            "account-id": "",
            "partner": "",
            "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "user-token": "",
        }
        try:

            response = requests.get(url, headers=headers, proxies=proxies, timeout=10, cookies=cookies)
            response.encoding = response.apparent_encoding
            if 'utf-8' in response.text:
                # print('编码修改')
                response.encoding = 'utf8'

            text = response.text
            if '滑动验证页面' in text:
                print('滑动验证')

                self.thread_proxy_map[thread_name] = {'proxy': self.get_proxy(), 'cookie': None}
                self.add_failed_proxy(proxy)
                time.sleep(timedelay)
                if ii > 0:
                    return self.download(url, ii=ii - 1, timedelay=timedelay)
                else:
                    return None
            if '前程无忧官方招聘网站' not in text:
                print('链接加密界面')
                # print(text)
                url = self.v3.call('get_url', url.split('&timestamp')[0])
                self.thread_proxy_map[thread_name] = {'proxy': self.get_proxy(), 'cookie': None}
                self.add_failed_proxy(proxy)
                time.sleep(timedelay)
                if ii > 0:
                    return self.download(url, ii=ii - 1, timedelay=timedelay)
                else:
                    return None
            # cookies = self.update_cookies(cookies, response)
            cookies.update(response.cookies.get_dict())
            self.thread_proxy_map[thread_name] = {'proxy': proxy, 'cookie': cookies}
            return response
        except BaseException as e:
            if not isinstance(e, (ProxyError,)):
                print('error :', e)

            self.thread_proxy_map[thread_name] = {'proxy': self.get_proxy(), 'cookie': None}
            self.add_failed_proxy(proxy)
            if ii > 0:
                time.sleep(timedelay)
                return self.download(url, ii=ii - 1)
            else:
                return None

    def get_jobInfo(self, item):
        sql_pass = "UPDATE " + f""" jobinfo_{self.y}{self.m} SET `status` = 0
   WHERE id = %s ;"""
        sql_address = "UPDATE " + f""" jobinfo_{self.y}{self.m} SET city = %s
   WHERE id = %s ;"""
        if 'jobs.51job' not in item['detailUrl']:
            self.sql.insert(sql_pass, (item['id'],))
            return None
        response = self.download(item['detailUrl'])
        if response is None:
            print('html没有获取到')
            return
        text = response.text
        if response.status_code == 200:
            soup = BeautifulSoup(text, 'lxml')
            try:
                address = soup.findAll('p', {'class': ['fp']})[-1].get_text()
                if '地址' in address:
                    item['workAddress'] = address.replace('上班地址：', '').strip()
                else:
                    item['workAddress'] = ''
            except (AttributeError, IndexError):
                item['workAddress'] = ''
            try:
                item['jobInfo'] = '\n'.join(
                    x for x in soup.find('div', {'class': ['tBorderTop_box']}).strings if x.strip()).replace(
                    '微信分享', '').replace('职位信息', '').strip()
                self.insert(item)
            except BaseException as e:
                self.sql.insert(sql_pass, (item['id'],))
                print('页面解析失败：', e)
                # print(soup)
            if item['offsite'] == 1:
                try:
                    real_city = soup.find('p', {'class': ['msg ltype']}).get_text().split('|')[0].strip()
                    self.sql.insert(sql_address, [real_city, item['id']])
                except BaseException as e:
                    print(e)
        else:
            self.sql.insert(sql_pass, (item['id'],))
            return None

    def insert(self, item):
        """
        入库函数
        :return:
        """
        # print('=' * 50)
        # print(json.dumps(item, ensure_ascii=False))
        sql_pass = "UPDATE " + f""" jobinfo_{self.y}{self.m} SET `status` = 0
   WHERE id = %s ;"""
        sql_job_add = "UPDATE " + f""" jobinfo_add_{self.y}{self.m} SET jobInfo = %s ,workAddress = %s
   WHERE id = %s ;"""
        idd = self.sql.insert(sql_job_add, [item['jobInfo'], item['workAddress'], item['id']])
        if not idd:
            self.sql.insert(sql_pass, (item['id'],))
        print('工作数据入库成功'.center(50, '#'))

    def change_date(self, y, m):
        self.y = y
        self.m = m


def sql_select(sql, host='10.86.0.107', user='root', password='wit123456', database='hrdatabase'):
    results = None
    db = pymysql.connect(host=host, user=user, password=password, database=database, charset='utf8')  # 打开数据库连接
    cursor = db.cursor(pymysql.cursors.DictCursor)  # 使用cursor()方法获取操作游标
    try:
        cursor.execute(sql)  # 执行SQL语句
        results = cursor.fetchall()  # 获取所有记录列表
    except BaseException as e:
        print("Error: ", e)
    db.close()  # 关闭数据库连接
    return results

if __name__ == '__main__':
    J = Job()
    pool = threadpool.ThreadPool(16)
    while True:
        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        start_sql = "SELECT" + f""" id,detailUrl,offsite FROM jobinfo_{y}{m} WHERE `status` = 1 ORDER BY id limit 0,5000 """
        url_list = sql_select(start_sql)
        J.change_date(y, m)
        try:
            list_number = len(url_list)
        except BaseException as e:
            print('获取未抓取jobinfo详情页网址列表失败：', e)
            list_number = 0
        print('列表数量：', list_number)
        if list_number >= 1:
            job_requests = threadpool.makeRequests(J.get_jobInfo, url_list)
            [pool.putRequest(req) for req in job_requests]
            pool.wait()
        else:
            time.sleep(60)