import datetime
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


def select_sql_error_site():
    set_check_time_two_day = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y-%m-%d %H:%M:%S")
    set_check_time_one_day = (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    set_check_time_eight_hour = (datetime.datetime.now() + datetime.timedelta(hours=-8)).strftime("%Y-%m-%d %H:%M:%S")
    set_check_time_seven_day = (datetime.datetime.now() + datetime.timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:%S")
    list_site = [
        {"indeed": set_check_time_one_day}, {"infojobs": set_check_time_two_day},
        {"reed": set_check_time_two_day}, {"saramin": set_check_time_two_day},
        {"seek": set_check_time_two_day}, {"sgindeed": set_check_time_one_day},
        {"sgmonster": set_check_time_two_day}, {"simolyhired": set_check_time_two_day},
        {"tenshoku_mynavi": set_check_time_seven_day}, {"timesjobs": set_check_time_two_day},
        {"ukindeed": set_check_time_one_day}, {"ukmonster": set_check_time_two_day},
        {"usajobs": set_check_time_seven_day}, {"workforceaustralia": set_check_time_two_day},
        {"workgo": set_check_time_two_day}, #{"workopolis": set_check_time_seven_day},
        {"inindeed": set_check_time_one_day}, {"itmonster": set_check_time_two_day},
        {"itindeed": set_check_time_one_day}, {"jobstreet": set_check_time_two_day},
        {"jobbank": set_check_time_two_day}, {"jobleads": set_check_time_seven_day},
        {"jobscentral": set_check_time_two_day}, {"jobsdb": set_check_time_two_day},
        {"jpindeed": set_check_time_one_day}, {"monster": set_check_time_two_day},
        {"monsterindia": set_check_time_two_day}, {"nzseek": set_check_time_two_day},
        {"naukri": set_check_time_two_day}, {"nz_trademe": set_check_time_seven_day},
        {"randstad": set_check_time_seven_day}, {"recruit": set_check_time_two_day},
        {"104": set_check_time_eight_hour}, {"1111": set_check_time_seven_day},
        {"Adzuna": set_check_time_two_day}, {"auindeed": set_check_time_one_day},
        {"caindeed": set_check_time_one_day}, {"camonster": set_check_time_two_day},
        {"careerone": set_check_time_two_day}, {"caressma": set_check_time_two_day},
        {"cvlibrary": set_check_time_two_day}, {"daijob": set_check_time_two_day},
        {"deindeed": set_check_time_one_day}, {"demonster": set_check_time_two_day},
        {"ejobmacau": set_check_time_two_day}, {"dodajop": set_check_time_two_day},
        {"fr_jobs": set_check_time_two_day}, {"frindeed": set_check_time_one_day},
        {"frmonster": set_check_time_two_day}, {"gehalt": set_check_time_two_day},
        {"glassdoor": set_check_time_two_day}, {"hellowork": set_check_time_two_day},
        {"hkgoodjobs": set_check_time_seven_day}, {"hkjobs": set_check_time_seven_day},
        {"incruit": set_check_time_two_day}, {"51job": set_check_time_eight_hour},
        {"boss": set_check_time_eight_hour}, {"实习僧": set_check_time_two_day},
        {"智联": set_check_time_eight_hour}, {"猎聘": set_check_time_eight_hour},
        {"卓聘": set_check_time_seven_day}, {"拉勾": set_check_time_eight_hour},
        {"58同城": set_check_time_eight_hour}, {"百聘": set_check_time_two_day},
        {"百姓": set_check_time_one_day}, {"人才热线": set_check_time_one_day},
        {"卓博": set_check_time_two_day}, {"今日招聘": set_check_time_eight_hour},
        #{"猪八戒": set_check_time_seven_day},
        # {"jobsinjapan": set_check_time_seven_day},
        # {"myjobspace": set_check_time_seven_day},
        # {"gaijinpot": set_check_time_two_day},
        # {"japanesejobs": set_check_time_seven_day},
        # {"placementindia": set_check_time_seven_day},
    ]
    # list_try = [{"indeed": set_check_time_one_day}]
    error_list = []
    for i in list_site:
        set_time = ''.join(i.values())  # 时间
        site = ''.join(i.keys())  # 平台名称
        error_site = check_spider(set_time, site)
        if error_site:
            error_list.append(error_site)
        time.sleep(0.2)
    if len(error_list)>5:
        return
    print(error_list)
    return error_list


def check_spider(set_check_time, site):
    while True:
        sql_check_data = sql.select(
            'SELECT' + f' job_day_number FROM crawler_pre_statistics_tb where get_date>"{set_check_time}"  and site="{site}"')
        if sql_check_data is None:
            time.sleep(5)
            continue
        break
    # print(sql_check_data)
    try:

        total = 0
        for i in sql_check_data:
            total += i.get("job_day_number")
        if total == 0:
            return site
        else:
            return ''
            # print('%s爬虫代码没有问题' % (site))
    except :
        alone_send_email(mail_host, mail_user, mail_pass, sender, receivers_luxian)
        print('爬虫监控的sql语句出现问题，或者数据库连接出错')


def alone_send_email(mail_host, mail_user, mail_pass, sender, receivers):
    # 第三方 SMTP 服务
    mail_host = mail_host  # 设置服务器
    mail_user = mail_user  # 用户名
    mail_pass = mail_pass  # 口令
    sender = sender  # 发送者
    receivers = receivers  # 接收邮者，可设置为你的QQ邮箱或者其他邮箱
    input_content = "爬虫监控的sql语句出现问题，或者数据库连接出错"
    From = "爬虫程序出现问题"
    inpuit_Text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>爬虫错误统计</title>
        <style>
            table {
                border: black solid 1px;
                border-spacing: 0;
                margin: 0 auto;
                width: 80%;
            }
            td,th {
                border: black solid 1px;
            }

        </style>
    </head>
    <body>
    <table>
        <tr>
            <th colspan="4">爬虫错误统计</th>
        </tr>
        <tr>

            <th>错误原因</th>
        </tr>""" + input_content + """

    </table>
    </body>
    </html>
    """
    message = MIMEText(inpuit_Text, 'html', 'utf-8')  # 发送内容
    # message['From'] = Header(From, 'utf-8')#发件人联系地址
    message['To'] = Header(From, 'utf-8')  # 文章关键词
    subject = '爬虫问题警告系统'  # 主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        time.sleep(86400)
    except smtplib.SMTPException:
        print("邮件发送失败")


def send_email(mail_host, mail_user, mail_pass, sender, receivers, list_crror_site_country):
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
        <style>
            table {
                border: black solid 1px;
                border-spacing: 0;
                margin: 0 auto;
                width: 80%;
            }
            td,th {
                border: black solid 1px;
            }

        </style>
    </head>
    <body>
    <table>
        <tr>
            <th colspan="4">爬虫错误统计</th>
        </tr>"""
    input_suf = """</table>
         </body>
         </html>
         """
    pre_python = ""
    for site_country in list_crror_site_country:
        site = ''.join(site_country.keys())
        country = ''.join(site_country.values())
        time_error_day = '超过24小时没有数据入库'
        if country == '中国':
            time_error_day = '超过8小时没有数据入库'
        pre_python += '<tr><td><b>国家：</b>%s</td><td><b>平台：</b>%s</td><td><b>报错原因：</b>%s</td></tr><br>' % (
            country, site, time_error_day)

    inpuit_Text = inpuit_pre + pre_python + input_suf

    message = MIMEText(inpuit_Text, 'html', 'utf-8')  # 发送内容
    # message['From'] = Header(From, 'utf-8')#发件人联系地址
    message['To'] = Header(From, 'utf-8')  # 文章关键词
    subject = '爬虫监控系统'  # 主题
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        time.sleep(7200)
    except smtplib.SMTPException:
        print("邮件发送失败")


def run_mial():
    if error_list:
        list_crror_site_country = []
        for site in error_list:
            item = {}
            country = sql.select(
                'SELECT' + f' country FROM crawler_statistics_database.crawler_pre_statistics_tb where site = "{site}" GROUP BY 1')
            country = country[0].get("country")  # 获取国家
            item[site] = country
            list_crror_site_country.append(item)
        send_email(mail_host, mail_user, mail_pass, sender, receivers, list_crror_site_country)
    else:
        print("爬虫数据正常")


if __name__ == '__main__':
    sql = SqlQueue(host='10.86.0.107', user='root', password='wit123456',database='crawler_statistics_database')  # 调用操作sql类
    mail_host = "smtp.51helpdesk.com"  # 设置服务器
    mail_user = "witbigdata_notice@51helpdesk.com"  # 用户名
    mail_pass = "6kSLpeF8Sj9cFjXw"  # 口令 & 授权码
    sender = 'witbigdata_notice@51helpdesk.com'  # 发送者
    # receivers = ['lu_xian@51helpdesk.com',"yan_xingke@51helpdesk.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers_luxian = ['lu_xian@51helpdesk.com']
    receivers = ['lu_xian@51helpdesk.com',
                 "geng_xuekai@51helpdesk.com",
                 "yan_xingke@51helpdesk.com",
                 "wang_zheng@51helpdesk.com",
                 "Kelvin_zhang@51helpdesk.com"
                 ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    print("开始运行")
    time.sleep(2)
    while True:
        # current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # 当前日期
        # judge_time = datetime.datetime.strptime(current_date, '%Y-%m-%d')
        error_list = select_sql_error_site()  # 查询有哪些平台出现问题
        run_mial()
        time.sleep(7200)



