import hashlib
import json
import socket
import threading
import traceback
from hashlib import md5
from pprint import pprint

import requests
import redis
import time
import datetime
import pymysql
import random
from queue import Queue
import re
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
from math import ceil

socket.setdefaulttimeout(60)
# 全局变量 职位字典 地址变量
Industry_dict = {'Accounting': 'Accounting', 'Admin': 'Admin', 'Advertising': 'Advertising',
                 'Agriculture': 'Agriculture', 'Architecture': 'Architecture', 'Arts': 'Arts',
                 'Automation': 'Automation', 'Bank': 'Bank', 'Bpo': 'Bpo', 'Computer': 'Computer',
                 'Construction': 'Construction', 'Consultant': 'Consultant', 'Customer Service': 'Customer+Service',
                 'Education': 'Education', 'Electrical': 'Electrical', 'Electronics': 'Electronics', 'Energy': 'Energy',
                 'Engineering': 'Engineering', 'Facilities': 'Facilities', 'Finance': 'Finance',
                 'Food Service': 'Food+Service', 'Fresher': 'Fresher', 'Government': 'Government',
                 'Healthcare': 'Healthcare', 'Hospitality': 'Hospitality', 'Human Resources': 'Human+Resources',
                 'Insurance': 'Insurance', 'Internet': 'Internet', 'IT': 'IT', 'Law Enforcement': 'Law+Enforcement',
                 'Legal': 'Legal', 'Loans': 'Loans', 'Logistics': 'Logistics', 'Management': 'Management',
                 'Manufacturing': 'Manufacturing', 'Marketing': 'Marketing', 'Mechanical': 'Mechanical',
                 'Medical': 'Medical', 'Networking': 'Networking', 'Part-time': 'Part-time',
                 'Pharmaceutical': 'Pharmaceutical', 'PR': 'PR', 'Publishing': 'Publishing',
                 'Real Estate': 'Real+Estate', 'Recruitment': 'Recruitment', 'Restaurant': 'Restaurant',
                 'Retail': 'Retail', 'Sales': 'Sales', 'Scientific': 'Scientific', 'Security': 'Security',
                 'Services': 'Services', 'Social Media': 'Social+Media', 'Teacher': 'Teacher',
                 'Telecommunication': 'Telecommunication', 'Training': 'Training', 'Transportation': 'Transportation',
                 'Travel': 'Travel', 'Volunteering': 'Volunteering', 'Walk-in': 'Walk-in'}
Location_dict = {'Ahmedabad': 'ahmedabad', 'Bangalore': 'bangalore', 'Chandigarh': 'chandigarh', 'Chennai': 'chennai',
                 'Hyderabad': 'hyderabad', 'Mumbai': 'mumbai', 'Delhi': 'delhi', 'Noida': 'noida', 'Gurgaon': 'gurgaon',
                 'Kolkata': 'kolkata', 'Pune': 'pune', 'Agra': 'agra', 'Ajmer': 'ajmer', 'Aligarh': 'aligarh',
                 'Allahabad': 'allahabad', 'Alwar': 'alwar', 'Ambala': 'ambala', 'Amritsar': 'amritsar',
                 'Anantnag': 'anantnag', 'Baddi': 'baddi', 'Baramulla': 'baramulla', 'Bareilly': 'bareilly',
                 'Batala': 'batala', 'Bathinda': 'bathinda', 'Bhiwani': 'bhiwani', 'Bhopal': 'bhopal',
                 'Bikaner': 'bikaner', 'Bilaspur': 'bilaspur', 'Budgam': 'budgam', 'Chamba': 'chamba',
                 'Dalhousie': 'dalhousie', 'Dehradun': 'dehradun', 'Dharamshala': 'dharamshala', 'Doda': 'doda',
                 'Faizabad': 'faizabad', 'Faridabad': 'faridabad', 'Faridkot': 'faridkot', 'Fatehabad': 'fatehabad',
                 'Fatehgarh Sahib': 'fatehgarh-sahib', 'Ferozepur': 'ferozepur', 'Ghaziabad': 'ghaziabad',
                 'Gorakhpur': 'gorakhpur', 'Gurdaspur': 'gurdaspur', 'Gwalior': 'gwalior', 'Haldwani': 'haldwani',
                 'Hamirpur': 'hamirpur', 'Haridwar': 'haridwar', 'Hissar': 'hissar', 'Hoshiarpur': 'hoshiarpur',
                 'Indore': 'indore', 'Jabalpur': 'jabalpur', 'Jaipur': 'jaipur', 'Jaisalmer': 'jaisalmer',
                 'Jalandhar': 'jalandhar', 'Jammu': 'jammu', 'Jhajjar': 'jhajjar', 'Jind': 'jind', 'Jodhpur': 'jodhpur',
                 'Kaithal': 'kaithal', 'Kangra': 'kangra', 'Kanpur': 'kanpur', 'Kapurthala': 'kapurthala',
                 'Kargil': 'kargil', 'Karnal': 'karnal', 'Kasauli': 'kasauli', 'Kathua': 'kathua', 'Katni': 'katni',
                 'Kinnaur': 'kinnaur', 'Kota': 'kota', 'Kullu': 'kullu', 'Kupwara': 'kupwara',
                 'Kurukshetra': 'kurukshetra', 'Lahaul & Spiti': 'lahaul-spiti', 'Leh': 'leh', 'Lucknow': 'lucknow',
                 'Ludhiana': 'ludhiana', 'Mahendergarh': 'mahendergarh', 'Manali': 'manali', 'Mandi': 'mandi',
                 'Mansa': 'mansa', 'Mathura': 'mathura', 'Meerut': 'meerut', 'Moga': 'moga', 'Mohali': 'mohali',
                 'Moradabad': 'moradabad', 'Muktsar': 'muktsar', 'Muzaffarnagar': 'muzaffarnagar',
                 'Nainital': 'nainital', 'Nalagarh': 'nalagarh', 'Narnaul': 'narnaul', 'Nawanshahr': 'nawanshahr',
                 'Panchkula': 'panchkula', 'Panipat': 'panipat', 'Parwanoo': 'parwanoo', 'Pathankot': 'pathankot',
                 'Patiala': 'patiala', 'Poonch': 'poonch', 'Pulwama': 'pulwama', 'Rajouri': 'rajouri',
                 'Ratlam': 'ratlam', 'Rewari': 'rewari', 'Rohtak': 'rohtak', 'Roorkee': 'roorkee', 'Ropar': 'ropar',
                 'Rudrapur': 'rudrapur', 'Sagar': 'sagar', 'Saharanpur': 'saharanpur', 'Sangrur': 'sangrur',
                 'Satna': 'satna', 'Shimla': 'shimla', 'Sirmaur': 'simaur', 'Sirsa': 'sirsa', 'Solan': 'solan',
                 'Sonepat': 'sonepat', 'Srinagar': 'srinagar', 'Udaipur': 'udaipur', 'Udhampur': 'udhampur',
                 'Ujjain': 'ujjain', 'Una': 'una', 'Varanasi / Banaras': 'varanasi-banaras',
                 'Yamunanagar': 'yamunanagar', 'Agartala': 'agartala', 'Aizawal': 'aizawal', 'Asansol': 'asansol',
                 'Bhagalpur': 'bhagalpur', 'Bhilai-Durg': 'bhilai-durg', 'Bhubaneshwar': 'bhubaneshwar',
                 'Bokaro': 'bokaro', 'Bongaigaon': 'bongaigaon', 'Burdwan': 'burdwan', 'Cuttack': 'cuttack',
                 'Dhanbad': 'dhanbad', 'Dhubri': 'dhubri', 'Dibrugarh': 'dibrugarh', 'Dimapur': 'dimapur',
                 'Durgapur': 'durgapur', 'Gangtok': 'gangtok', 'Guwahati': 'guwahati', 'Haldia': 'haldia',
                 'Imphal': 'imphal', 'Itanagar': 'itanagar', 'Jamshedpur': 'jamshedpur', 'Jorhat': 'jorhat',
                 'Kharagpur': 'kharagpur', 'Kohima': 'kohima', 'Malda': 'malda', 'Midnapur': 'midnapur',
                 'Muzaffarpur': 'muzaffarpur', 'Paradeep': 'paradeep', 'Patna': 'patna', 'Puri': 'puri',
                 'Raipur': 'raipur', 'Ranchi': 'ranchi', 'Raniganj': 'raniganj', 'Rourkela': 'rourkela',
                 'Shillong': 'shillong', 'Sibsagar': 'sibsagar', 'Silchar': 'silchar', 'Siliguri': 'siliguri',
                 'Tezpur': 'tezpur', 'Tinsukia': 'tinsukia', 'Anantapur': 'anantapur', 'Belgaum': 'belgaum',
                 'Bellary': 'bellary', 'Bidar': 'bidar', 'Calicut/ Kozhikode': 'calicut-kozhikode',
                 'Cochin/ Kochi/ Ernakulam': 'cochin-kochi-ernakulam', 'Coimbatore': 'coimbatore',
                 'Cuddalore': 'cuddalore', 'Davanagere': 'davanagere', 'Dharwad': 'dharwad', 'Erode': 'erode',
                 'Gulbarga': 'gulbarga', 'Guntakal': 'guntakal', 'Guntur': 'guntur', 'Hosur': 'hosur', 'Hubli': 'hubli',
                 'Kakinada': 'kakinada', 'Kanniyakumari': 'kanniyakumari', 'Kannur': 'kannur', 'Kolar': 'kolar',
                 'Kollam': 'kollam', 'Kottayam': 'kottayam', 'Kurnool': 'kurnool', 'Madurai': 'madurai',
                 'Mangalore': 'mangalore', 'Mysoru/ Mysore': 'mysoru-mysore', 'Nagercoil': 'nagercoil',
                 'Nellore': 'nellore', 'Nizamabad': 'nizamabad', 'Ooty': 'ooty', 'Palakkad': 'palakkad',
                 'Rajahmundry': 'rajahmundry', 'Salem': 'salem', 'Thanjavur': 'thanjavur',
                 'Thiruvananthapuram': 'thiruvananthapuram', 'Thrissur': 'thrissur', 'Tirunelveli': 'tirunelveli',
                 'Tirupati': 'tirupati', 'Trichy': 'trichy', 'Tuticorin': 'tuticorin', 'Vellore': 'vellore',
                 'Vijayawada': 'vijayawada', 'Visakhapatnam': 'visakhapatnam', 'Warangal': 'warangal',
                 'Ahmednagar': 'ahmednagar', 'Akola': 'akola', 'Amravati': 'amravati', 'Anand': 'anand',
                 'Ankleshwar': 'ankleshwar', 'Aurangabad': 'aurangabad', 'Bharuch': 'bharuch', 'Bhavnagar': 'bhavnagar',
                 'Bhuj': 'bhuj', 'Buldhana': 'buldhana', 'Chandrapur': 'chandrapur', 'Dhule': 'dhule',
                 'Gandhidham': 'gandhidham', 'Gandhinagar': 'gandhinagar', 'Gir': 'gir', 'Gondia': 'gondia',
                 'Jalgaon': 'jalgaon', 'Jamnagar': 'jamnagar', 'Junagarh': 'junagarh', 'Kandla': 'kandla',
                 'Kolhapur': 'kolhapur', 'Latur': 'latur', 'Lonavala': 'lonavala', 'Mahabaleshwar': 'mahabaleshwar',
                 'Mehsana': 'mehsana', 'Nagpur': 'nagpur', 'Nanded': 'nanded', 'Nasik': 'nasik',
                 'Navi Mumbai': 'navi-mumbai', 'Panjim/ Panaji': 'panjim-panaji', 'Porbandar': 'porbandar',
                 'Rajkot': 'rajkot', 'Sangli': 'sangli', 'Satara': 'satara', 'Solapur': 'solapur', 'Surat': 'surat',
                 'Thane': 'thane', 'Vadodara': 'vadodara', 'Valsad -Vapi': 'valsad-vapi',
                 'Vasco Da Gama': 'vasco-da-gama', 'Yavatmal': 'yavatmal'}


def list_url():
    """
    生成需要爬取的网站列表页
    :return:网站列表页列表
    """
    start_list = []
    for Location, Location_url in Location_dict.items():
        for Industry, Industry_url in Industry_dict.items():
            start_list.append({'city': Location,
                               'Industry': Industry,
                               'url': f'https://careesma.in/jobs?q={Industry_url}&lc={Location_url}'
                               })
        #     break
        # break

    return start_list

class SqlQueue(object):  # mysql长连接类
    def __init__(self, host="localhost", user="root", password="123456", database="pa1"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = 'utf8'
        # 定义队列，实现多线程 maxsize 数值为最大线程数
        self.q = Queue(maxsize=3)
        for i in range(0, 3):
            db = pymysql.connect(host=host, user=user, password=password, database=database,
                                 charset='utf8')  # 打开数据库连接
            self.q.put(db)

    def test_conn(self, db):
        """
        判断是否断开链接
        :param db:
        :return:
        """
        # noinspection PyBroadException
        try:
            db.ping()  # 运行ping函数，判断是否断开链接
            return True
        except BaseException:
            return False

    def select(self, sql, fetch_one=False):
        results = None
        # 获取数据链接
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        # 检查数据链接是否断了
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
        自动断开数据库链接
        :return:
        """
        try:
            while True:
                self.q.get().close()
                if self.q.empty():
                    break
        except BaseException as e:
            print(e)

class GetProxy:  # 获取ip类
    def __init__(self):
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.proxies = []
        self.failed_proxies = set()
        threading.Thread(target=self.change_proxies, daemon=True).start()

    def get_proxy(self, proxy_type='short'):
        while True:
            if len(self.proxies):
                return random.choice(self.proxies)
            print('等待代理ip')
            time.sleep(2)

    def change_proxies(self, delay=3, proxy_type='short'):
        if proxy_type == 'long':
            proxy_key = 'proxies'  # use_proxies
        else:
            proxy_key = 'use_proxies'  # use_proxies
        while True:
            self.proxies = self.client.lrange(proxy_key, 0, -1)
            self.failed_proxies = self.failed_proxies & set(self.proxies)
            self.proxies = [x for x in self.proxies if x not in self.failed_proxies]
            time.sleep(delay)

    def add_failed_proxy(self, proxy):
        self.failed_proxies.add(proxy)
        self.proxies = [x for x in self.proxies if x not in self.failed_proxies]


class Spider:
    def __init__(self):
        self.spider_name = str(__file__.split('\\')[-1])  # 程序名称
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.headers = {
            "authority": "careesma.in",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            # "referer": "https://careesma.in/jobs?q=Accounting&lc=&job=8pyDAsD6acnVW6PtbhQXuMyCrOBCSkSZEbTMRKp4k-4j17vf_JcF_AfQgMj2h7B2&pc=ABkAAYEAGQAAAAAAAAAAAAAAAeZ0YqIAPgEBAQcEHFinWuHVUEv7K7kVJJ7wOrWcQoVCc67oVtbASy4pBAi%2Bh2ENu2FvT%2FVqiRIlQ7G6xh%2BnanHu92YtAAA%3D&pn=2",
            "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"113\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        self.sql = SqlQueue(host='10.86.0.107', user='root', password='wit123456', database='indiahr')  # 调用操作sql类
        self.url_set = set()
        self.G = GetProxy()
        self.spider_start()
        self.current_date = datetime.date.today()
        self.cookies_key = 'careessma_cookies'

    def download(self, url, timesleep=0.7, timeout=45, ii=3):
        indeed_cookies = self.client.lrange(self.cookies_key, 0, -1)
        if not len(indeed_cookies):
            time.sleep(2)
            return self.download(url, timesleep, timeout, ii)
        indeed_cookies_not = random.choice(indeed_cookies)
        proxy, cookies = list(json.loads(indeed_cookies_not).items())[0]
        headers = self.headers.copy()
        try:
            # cookies = {i.split('=')[0]: i.split('=')[1] for i in cookie.split('; ') if i.strip()}
            print('Downloading: %s' % url)
            proxies = {'http': proxy, 'https': proxy}
            cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
            response = requests.get(url, headers=headers, proxies=proxies, timeout=timeout, cookies=cookies)
            if response.status_code != 200:
                print(response)
                self.client.lrem(self.cookies_key, 0, indeed_cookies_not)
                if ii > 0:
                    return self.download(url, timesleep, timeout, ii - 1)
                else:
                    return None

            return response.text
        except BaseException as e:
            self.client.lrem(self.cookies_key, 0, indeed_cookies_not)
            print('error :', e)
            time.sleep(timesleep)
            response = None
            if ii > 0:
                return self.download(url, timesleep=timesleep, timeout=timeout, ii=ii - 1)  # 失败重取
        return response

    def get_list(self, url_dict):
        print(url_dict["url"])
        response_data = self.download(url_dict["url"]) #  爬取数据
        if not response_data:
            return
        html = etree.HTML(response_data)
        datalist = html.xpath("//div[@id='job-list']/article") #数据列表
        for i in datalist:
            item = {}
            item['company'] = ''.join(i.xpath("./div[@class='SerpJob-properties'][1]/div[@class='SerpJob-property SerpJob-company']/span/text()"))
            item['city'] = ''.join(i.xpath("./div[@class='SerpJob-properties']/span[@class='SerpJob-property SerpJob-location']/span/text()")[1])
            item['jobName'] = ''.join(i.xpath("./h2[@class='SerpJob-title']/a[@class='SerpJob-titleLink']/text()"))
            item['Salary'] = ''.join(i.xpath("./div/span[@class='Salary']/text()")).replace('\n', '').replace('  ', '')
            job_id = hashlib.md5((item['Salary'] + item['city'] + item['company'] + item['jobName']).encode("utf-8")).hexdigest()
            item['job_id'] = job_id
            if self.check_duplicates(job_id):
                # print('数据重复', job_id)
                continue
            suf_url = ''.join(i.xpath("./@data-jobkey"))
            detailUrl = "https://careesma.in/posting/" + suf_url
            item['detailUrl'] = detailUrl
            item["Industry"] = url_dict["Industry"]
            self.get_detail_sql(item)  # 列表第一页解析详情页url


        next_list = html.xpath("//span[@class='Pagination-item ']/a/@href")  #翻页处理
        for next_suf in next_list:
            next_url = "https://careesma.in/" + next_suf
            response_data = self.download(next_url)  # 爬取数据

            if not response_data:
                return
            html = etree.HTML(response_data)
            datalist = html.xpath("//div[@id='job-list']/article")#//div[@id='job-list']/article
            for i in datalist:
                item = {}
                item['company'] = ''.join(i.xpath(
                    "./div[@class='SerpJob-properties'][1]/div[@class='SerpJob-property SerpJob-company']/span/text()"))
                item['city'] = ''.join(i.xpath(
                    "./div[@class='SerpJob-properties']/span[@class='SerpJob-property SerpJob-location']/span/text()")[
                                           1])
                item['jobName'] = ''.join(i.xpath("./h2[@class='SerpJob-title']/a[@class='SerpJob-titleLink']/text()"))
                item['Salary'] = ''.join(i.xpath("./div/span[@class='Salary']/text()")).replace('\n', '').replace('  ',
                                                                                                                  '')
                job_id = hashlib.md5(
                    (item['Salary'] + item['city'] + item['company'] + item['jobName']).encode("utf-8")).hexdigest()
                item['job_id'] = job_id
                if self.check_duplicates(job_id):
                    # print('数据重复:', job_id)
                    continue
                suf_url = ''.join(i.xpath("./@data-jobkey"))
                detailUrl = "https://careesma.in/posting/" + suf_url
                item['detailUrl'] = detailUrl
                item["Industry"] = url_dict["Industry"]
                self.get_detail_sql(item)  # 列表第一页解析详情页url

    def get_detail_sql(self,item):
        """
        详情页解析
        """
        item = item.copy()
        response = self.download(item["detailUrl"])
        if not response:
            return None
        html = etree.HTML(response)
        jobInfo = html.xpath("//div[@class='viewjob-description ViewJobBodyDescription']//text()")  # 岗位详情
        item['jobInfo'] = '\n'.join(jobInfo)
        item['publishTime'] = datetime.datetime.now().strftime('%Y-%m-%d')  # 发布时间
        item['update_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 入库时间
        # pprint(item)
        self.insert(item)


    def insert(self, item):
        #print(self.spider_name.center(100, '='))
        date_str = datetime.date.today().strftime('%Y%m')
        sql_job = "INSERT " + f"""INTO indiahr.caressma_jobinfo_{date_str} (jobName,Salary,detailUrl,city,
    publishTime,company,Industry,update_time,jobInfo,job_id)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        self.sql.insert(sql_job, [
            item['jobName'], item['Salary'], item['detailUrl'], item['city'], item['publishTime'],
            item['company'], item['Industry'], item['update_time'], item['jobInfo'],item['job_id']])
        print('工作数据入库成功'.center(100, '#'))
        self.url_set.add(item['job_id'])

    def check_duplicates(self, url):
        """
        url连接去重，跨月重置去重链接集合
        :param url: 采集的链接
        :return: bool
        """
        # md5_url = md5(url.encode()).hexdigest()
        if self.current_date.month == datetime.date.today().month:
            return url in self.url_set
        else:
            self.url_set.clear()
            self.current_date = datetime.date.today()

    def spider_start(self):
        date_str = datetime.date.today().strftime('%Y%m')
        url_list = self.sql.select("SELECT " + f"job_id as url FROM indiahr.caressma_jobinfo_{date_str}")
        for url in url_list:
            self.url_set.add(url['url'])


def main():
    print('开始运行')
    S = Spider()  # 获取爬虫类
    pool = ThreadPoolExecutor(5)
    while True:  # 循环爬取
        url_dict = list_url()  # 列表页不同的关键词data参数
        url_dict.reverse()
        res = pool.map(S.get_list, url_dict)
        for x in res:
            time.sleep(0.3)
            pass
        print('线程执行完毕,程序停止一小时')
        time.sleep(60)

if __name__ == '__main__':
    main()
