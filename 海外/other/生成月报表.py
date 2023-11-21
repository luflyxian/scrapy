# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
from queue import Queue

import pandas as pd
import pymysql
import time
import time
from queue import Queue
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
from chinese_calendar import is_workday, is_holiday, is_in_lieu, get_holiday_detail


class SqlQueue(object):  # mysql长连接类
    def __init__(self, host="localhost", user="root", password="123456", database="pa1"):
        """
        数据库链接属性存储 第一次链接
        :param host: 数据库ip
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名称
        """
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
        """
        数据库查询
        :param sql: sql查询语句
        :param fetch_one: 是否只查询一条
        :return: 数据查询结果
        """
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
                results = cursor.fetch_one()
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
        更新入库模块
        :param sql: sql语句
        :param data: sql参数
        :return:
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


def send_email(mail_host, mail_user, mail_pass, sender, receivers, pd_date):
    # 第三方 SMTP 服务
    mail_host = mail_host  # 设置服务器
    mail_user = mail_user  # 用户名
    mail_pass = mail_pass  # 口令
    sender = sender  # 发送者
    receivers = receivers  # 接收邮者，可设置为你的QQ邮箱或者其他邮箱
    From = ';'.join(receivers)

    inpuit_pre = """

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>爬虫错误统计</title>
    </head>



    <body>
    <table>"""
    input_suf = """
         </body>

         </html>
         """
    pre_python = pd_date

    inpuit_Text = inpuit_pre + pre_python + input_suf

    message = MIMEText(inpuit_Text, 'html', 'utf-8')  # 发送内容
    # message['From'] = Header(From, 'utf-8')#发件人联系地址
    message['To'] = Header(From, 'utf-8')  # 文章关键词

    current_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 当前日期
    current_year = current_time[:4]
    current_month = current_time[6:7]
    current_day = current_time[8:]
    year_month_day = current_year + "年" + current_month + "月" + current_day + "日"

    subject = f'{year_month_day}数据环比报告'  # 主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        print("今日已发送过警告邮件，程序休息")
        time.sleep(86400)
    except smtplib.SMTPException:
        print("邮件发送失败")


def create_sql(country, country_db_name, site_db_name, site_name, judgb_date, pd_date):
    sql = SqlQueue(host='10.86.0.107', user='root', password='wit123456', database='hrdatabase')
    # 这个月的1,10,20号
    now = datetime.datetime.now();
    this_month_start = datetime.datetime(now.year, now.month, 1).strftime("%Y-%m-%d %H:%M:%S");
    this_month_ten = (datetime.datetime(now.year, now.month, 1) + datetime.timedelta(days=+10)).strftime(
        "%Y-%m-%d %H:%M:%S");
    this_month_twenty = (datetime.datetime(now.year, now.month, 1) + datetime.timedelta(days=+20)).strftime(
        "%Y-%m-%d %H:%M:%S");
    this_month = this_month_start.replace("-", '')[:6]  # 当前年月
    # 上个月的1,10,20号
    last_month_start = datetime.datetime(now.year, now.month - 1, 1).strftime("%Y-%m-%d %H:%M:%S");
    last_month_ten = (datetime.datetime(now.year, now.month - 1, 1) + datetime.timedelta(days=+10)).strftime(
        "%Y-%m-%d %H:%M:%S");
    last_month_twenty = (datetime.datetime(now.year, now.month - 1, 1) + datetime.timedelta(days=+20)).strftime(
        "%Y-%m-%d %H:%M:%S");
    last_month = last_month_start.replace("-", '')[:6]  # 上个月的年月
    #####开始查询
    if judgb_date == '10':

        select_sql = 'select ' + f'sum(job_day_number) from crawler_statistics_database.crawler_pre_statistics_tb WHERE update_time > "{last_month_start}" and update_time < "{last_month_ten}" and id>0 and site = "{site_name}" union all ' \
                                 f'select sum(job_day_number) from crawler_statistics_database.crawler_pre_statistics_tb WHERE update_time > "{this_month_start}" and update_time < "{this_month_ten}" and id>0  and site = "{site_name}"'

        # print(select_sql)
        select_sql_data = sql.select(select_sql)
        try:
            pd_date = pd.DataFrame(select_sql_data)
            pd_date['环比'] = pd_date.pct_change()
            pd_date['国家'] = country
            pd_date['平台名称'] = site_name

            pd_date['环比'] = pd_date['环比'].astype(float)
            pd_date.loc[pd_date['环比'].isna(), '查询年月'] = last_month[:4] + '-' + last_month[4:]
            pd_date.loc[pd_date['环比'].notna(), '查询年月'] = this_month[:4] + '-' + this_month[4:]
            # pd_date.loc[:, '是否正常?'] = pd_date['环比'].apply(lambda x:'数据上涨超过20' if x>0.2 else ('----' if x>=-0.2 else '数据下降超过20'))

            pd_date.loc[pd_date['环比'] > 0.2, '是否正常?'] = '数据上涨超过20%'
            pd_date.loc[pd_date['环比'] < -0.2, '是否正常?'] = '数据下降超过20'
            pd_date.loc[pd_date['环比'].isna(), '是否正常?'] = '----'

            pd_date['环比'].fillna('---', inplace=True)
            pd_date['是否正常?'].fillna('正常', inplace=True)

            return pd_date
        except:
            return

    else:
        select_sql = 'select ' + f'sum(job_day_number) from crawler_statistics_database.crawler_pre_statistics_tb WHERE update_time > "{last_month_start}" and update_time < "{last_month_twenty}" and id>0 and site = "{site_name}" union all ' \
                                 f'select sum(job_day_number) from crawler_statistics_database.crawler_pre_statistics_tb WHERE update_time > "{this_month_start}" and update_time < "{this_month_twenty}" and id>0  and site = "{site_name}"'

        # print(select_sql)
        select_sql_data = sql.select(select_sql)
        try:
            pd_date = pd.DataFrame(select_sql_data)
            pd_date['环比'] = pd_date.pct_change()
            pd_date['国家'] = country
            pd_date['平台名称'] = site_name
            pd_date['环比'] = pd_date['环比'].astype(float)
            pd_date.loc[pd_date['环比'].isna(), '查询年月'] = last_month[:4] + '-' + last_month[4:]
            pd_date.loc[pd_date['环比'].notna(), '查询年月'] = this_month[:4] + '-' + this_month[4:]
            pd_date.loc[pd_date['环比'] > 0.2, '是否正常?'] = '数据上涨超过20%'
            pd_date.loc[pd_date['环比'] < -0.2, '是否正常?'] = '数据下降超过20'
            pd_date.loc[pd_date['环比'].isna(), '是否正常?'] = '----'

            pd_date['环比'].fillna('---', inplace=True)
            pd_date['是否正常?'].fillna('正常', inplace=True)
            return pd_date
        except:
            return


if __name__ == '__main__':
    mail_host = "smtp.51helpdesk.com"  # 设置服务器
    mail_user = "witbigdata_notice@51helpdesk.com"  # 用户名
    mail_pass = "6kSLpeF8Sj9cFjXw"  # 口令 & 授权码
    sender = 'witbigdata_notice@51helpdesk.com'  # 发送者
    receivers_luxian = ['lu_xian@51helpdesk.com']
    receivers = ['lu_xian@51helpdesk.com',
                 "geng_xuekai@51helpdesk.com",
                 "yan_xingke@51helpdesk.com",
                 "wang_zheng@51helpdesk.com"
                 ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    list_site = [
        {'country': '中国', 'country_db_name': 'hrdatabase', 'site_db_name': 'jobinfo', 'site_name': '51job'},
        {'country': '中国', 'country_db_name': 'bosshr', 'site_db_name': 'jobinfo', 'site_name': 'boss'},
        {'country': '中国', 'country_db_name': 'zhilianhr', 'site_db_name': 'jobinfo', 'site_name': '智联'},
        {'country': '中国', 'country_db_name': 'liepinhr', 'site_db_name': 'jobinfo', 'site_name': '猎聘'},
        {'country': '中国', 'country_db_name': 'zhuopinhr', 'site_db_name': 'jobinfo', 'site_name': '卓聘'},
        {'country': '中国', 'country_db_name': 'lagouhr', 'site_db_name': 'jobinfo', 'site_name': '拉勾'},
        {'country': '中国', 'country_db_name': 'tongchenghr', 'site_db_name': 'jobinfo', 'site_name': '58同城'},
        {'country': '中国', 'country_db_name': 'baipinhr', 'site_db_name': 'jobinfo', 'site_name': '百聘'},
        {'country': '中国', 'country_db_name': 'baixinghr', 'site_db_name': 'jobinfo', 'site_name': '百姓'},
        {'country': '中国', 'country_db_name': 'cjolhr', 'site_db_name': 'jobinfo', 'site_name': '人才热线'},
        {'country': '中国', 'country_db_name': 'jobcnhr', 'site_db_name': 'jobinfo', 'site_name': '卓博'},
        {'country': '中国', 'country_db_name': 'jrzphr', 'site_db_name': 'jobinfo', 'site_name': '今日招聘'},
        {'country': '中国', 'country_db_name': 'shixisenghr', 'site_db_name': 'jobinfo', 'site_name': '实习僧'},
        {'country': '中国', 'country_db_name': 'zbjhr', 'site_db_name': 'jobinfo', 'site_name': '猪八戒'},
        {'country': '中国台湾', 'country_db_name': 'hk_tw_hr', 'site_db_name': '104_jobinfo', 'site_name': '104'},
        {'country': '中国台湾', 'country_db_name': 'hk_tw_hr', 'site_db_name': '1111_jobinfo', 'site_name': '1111'},
        {'country': '中国香港', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'jobsdb_jobinfo', 'site_name': 'jobsdb'},
        {'country': '中国香港', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'hkjobs_jobinfo', 'site_name': 'hkjobs'},
        {'country': '中国香港', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'hkgoodjobs_jobinfo',
         'site_name': 'hkgoodjobs'},
        {'country': '中国香港', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'recruit_jobinfo',
         'site_name': 'recruit'},
        {'country': '中国澳门', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'ejobmacau_jobinfo',
         'site_name': 'ejobmacau'},
        {'country': '英国', 'country_db_name': 'ukhr', 'site_db_name': 'reed_jobinfo', 'site_name': 'reed'},
        {'country': '英国', 'country_db_name': 'ukhr', 'site_db_name': 'cvlibrary_jobinfo', 'site_name': 'cvlibrary'},
        {'country': '英国', 'country_db_name': 'ukhr', 'site_db_name': 'ukindeed_jobinfo', 'site_name': 'ukindeed'},
        {'country': '澳洲', 'country_db_name': 'auhr', 'site_db_name': 'seek_jobinfo', 'site_name': 'seek'},
        {'country': '澳洲', 'country_db_name': 'auhr', 'site_db_name': 'Adzuna_jobinfo', 'site_name': 'Adzuna'},
        {'country': '澳洲', 'country_db_name': 'auhr', 'site_db_name': 'auindeed_jobinfo', 'site_name': 'auindeed'},
        {'country': '新西兰', 'country_db_name': 'auhr', 'site_db_name': 'nzseek_jobinfo', 'site_name': 'nzseek'},
        {'country': '新西兰', 'country_db_name': 'auhr', 'site_db_name': 'myjobspace_jobinfo',
         'site_name': 'myjobspace'},
        {'country': '新加坡', 'country_db_name': 'sghr', 'site_db_name': 'jobstreet_jobinfo', 'site_name': 'jobstreet'},
        {'country': '新加坡', 'country_db_name': 'sghr', 'site_db_name': 'sgindeed_jobinfo', 'site_name': 'sgindeed'},
        {'country': '新加坡', 'country_db_name': 'sghr', 'site_db_name': 'sgmonster_jobinfo', 'site_name': 'sgmonster'},
        {'country': '加拿大', 'country_db_name': 'cahr', 'site_db_name': 'jobbank_jobinfo', 'site_name': 'jobbank'},
        {'country': '加拿大', 'country_db_name': 'cahr', 'site_db_name': 'caindeed_jobinfo', 'site_name': 'caindeed'},
        {'country': '加拿大', 'country_db_name': 'cahr', 'site_db_name': 'randstad_jobinfo', 'site_name': 'randstad'},
        {'country': '加拿大', 'country_db_name': 'cahr', 'site_db_name': 'workopolis_jobinfo',
         'site_name': 'workopolis'},
        {'country': '美国', 'country_db_name': 'usahr', 'site_db_name': 'usajobs_jobinfo', 'site_name': 'usajobs'},
        {'country': '美国', 'country_db_name': 'usahr', 'site_db_name': 'monster_jobinfo', 'site_name': 'monster'},
        {'country': '美国', 'country_db_name': 'usahr', 'site_db_name': 'simolyhired_jobinfo',
         'site_name': 'simolyhired'},
        {'country': '美国', 'country_db_name': 'usahr', 'site_db_name': 'glassdoor_jobinfo', 'site_name': 'glassdoor'},
        {'country': '美国', 'country_db_name': 'usahr', 'site_db_name': 'indeed_jobinfo', 'site_name': 'indeed'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'daijob_jobinfo', 'site_name': 'daijob'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'gaijinpot_jobinfo', 'site_name': 'gaijinpot'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'japanesejobs_jobinfo',
         'site_name': 'japanesejobs'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'jobsinjapan_jobinfo',
         'site_name': 'jobsinjapan'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'jpindeed_jobinfo', 'site_name': 'jpindeed'},
        {'country': '韩国', 'country_db_name': 'krhr', 'site_db_name': 'incruit_jobinfo', 'site_name': 'incruit'},
        {'country': '韩国', 'country_db_name': 'krhr', 'site_db_name': 'saramin_jobinfo', 'site_name': 'saramin'},
        {'country': '韩国', 'country_db_name': 'krhr', 'site_db_name': 'workgo_jobinfo', 'site_name': 'workgo'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'naukri_jobinfo', 'site_name': 'naukri'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'timesjobs_jobinfo',
         'site_name': 'timesjobs'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'monsterindia_jobinfo',
         'site_name': 'monsterindia'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'inindeed_jobinfo', 'site_name': 'inindeed'},
        {'country': '法国', 'country_db_name': 'frhr', 'site_db_name': 'frmonster_jobinfo', 'site_name': 'frmonster'},
        {'country': '法国', 'country_db_name': 'frhr', 'site_db_name': 'frindeed_jobinfo', 'site_name': 'frindeed'},
        {'country': '法国', 'country_db_name': 'frhr', 'site_db_name': 'hellowork_jobinfo', 'site_name': 'hellowork'},
        {'country': '意大利', 'country_db_name': 'ithr', 'site_db_name': 'itmonster_jobinfo', 'site_name': 'itmonster'},
        {'country': '意大利', 'country_db_name': 'ithr', 'site_db_name': 'itindeed_jobinfo', 'site_name': 'itindeed'},
        {'country': '意大利', 'country_db_name': 'ithr', 'site_db_name': 'infojobs_jobinfo', 'site_name': 'infojobs'},
        {'country': '意大利', 'country_db_name': 'ithr', 'site_db_name': 'jobleads_jobinfo', 'site_name': 'jobleads'},
        {'country': '德国', 'country_db_name': 'dehr', 'site_db_name': 'demonster_jobinfo', 'site_name': 'demonster'},
        {'country': '德国', 'country_db_name': 'dehr', 'site_db_name': 'gehalt_jobinfo', 'site_name': 'gehalt'},
        {'country': '德国', 'country_db_name': 'dehr', 'site_db_name': 'deindeed_jobinfo', 'site_name': 'deindeed'},
        {'country': '新西兰', 'country_db_name': 'auhr', 'site_db_name': 'nz_trademe_jobinfo',
         'site_name': 'nz_trademe'},
        {'country': '澳洲', 'country_db_name': 'auhr', 'site_db_name': 'careerone_jobinfo', 'site_name': 'careerone'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'caressma_jobinfo', 'site_name': 'caressma'},
        {'country': '印度', 'country_db_name': 'indiahr', 'site_db_name': 'placementindia_jobinfo',
         'site_name': 'placementindia'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'dodajop_jobinfo', 'site_name': 'dodajop'},
        {'country': '日本', 'country_db_name': 'jphr', 'site_db_name': 'tenshoku_mynavi_jobinfo',
         'site_name': 'tenshoku_mynavi'},
        {'country': '新加坡', 'country_db_name': 'sghr', 'site_db_name': 'jobscentral_jobinfo',
         'site_name': 'jobscentral'},
        {'country': '法国', 'country_db_name': 'frhr', 'site_db_name': 'fr_jobs_jobinfo', 'site_name': 'fr_jobs'},
        {'country': '澳洲', 'country_db_name': 'auhr', 'site_db_name': 'workforceaustralia_jobinfo',
         'site_name': 'workforceaustralia'},
        {'country': '加拿大', 'country_db_name': 'cahr', 'site_db_name': 'monster_jobinfo', 'site_name': 'camonster'},
        {'country': '英国', 'country_db_name': 'ukhr', 'site_db_name': 'ukmonster_jobinfo', 'site_name': 'ukmonster'}]
    # list_try = [        {'country': '新西兰', 'country_db_name': 'auhr', 'site_db_name': 'nzseek_jobinfo', 'site_name': 'nzseek'},
    #     {'country': '新西兰', 'country_db_name': 'auhr', 'site_db_name': 'myjobspace_jobinfo', 'site_name': 'myjobspace'},
    #     {'country': '中国香港', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'recruit_jobinfo','site_name': 'recruit'},
    #     {'country': '中国澳门', 'country_db_name': 'hk_tw_hr', 'site_db_name': 'ejobmacau_jobinfo','site_name': 'ejobmacau'},
    #
    #                     ]
    while True:
        print("程序开始运行")
        current_time = datetime.datetime.now().strftime('%Y-%m-%d')  # 当前日期
        current_time_date = current_time[8:]
        judgb_date = current_time_date
        print(f"当前日期：{current_time_date}")

        # current_time_date = '20'
        # judgb_date = current_time_date

        if current_time_date == "10":
            pd_date = pd.DataFrame()
            for i in list_site:
                select_sql_data = create_sql(i.get("country"), i.get("country_db_name"), i.get("site_db_name"),
                                             i.get("site_name"), judgb_date, pd_date)
                pd_date = pd_date.append(select_sql_data, ignore_index=True)
            pd_date.rename(mapper={'sum(job_day_number)': '数量'}, axis=1, inplace=True)
            pd_date['处理状态'] = ''
            pd_date['异常原因'] = ''
            pd_date = pd_date.loc[:,
                      ['国家', '平台名称', '查询年月', '数量', '环比', '是否正常?', '处理状态', '异常原因']]
            pd_date = pd_date.to_html()

            print(pd_date)
            send_email(mail_host, mail_user, mail_pass, sender, receivers, pd_date)

        elif current_time_date == "20":
            pd_date = pd.DataFrame()
            for i in list_site:
                select_sql_data = create_sql(i.get("country"), i.get("country_db_name"), i.get("site_db_name"),
                                             i.get("site_name"), judgb_date, pd_date)
                pd_date = pd_date.append(select_sql_data, ignore_index=True)

            pd_date.rename(mapper={'sum(job_day_number)': '数量'}, axis=1, inplace=True)
            pd_date['处理状态'] = ''
            pd_date['异常原因'] = ''
            pd_date = pd_date.loc[:,
                      ['国家', '平台名称', '查询年月', '数量', '环比', '是否正常?', '处理状态', '异常原因']]
            pd_date = pd_date.to_html()
            print(pd_date)
            send_email(mail_host, mail_user, mail_pass, sender, receivers, pd_date)

        else:
            print("程序休息")
            time.sleep(86400)
