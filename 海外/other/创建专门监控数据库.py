import datetime
import time
from pprint import pprint
from queue import Queue
import hashlib
import pandas as pd
import pymysql
from tqdm import tqdm

'''
company_day_number_sql ="SELECT companyName,COUNT(1) FROM company.company_info LIMIT 100"
cursor.execute(company_day_number_sql)
company_day_number_sql_tuple = cursor.fetchone()
company_day_number = company_day_number_sql_tuple[1]  #查询有多少个公司
print("查询国内一共有多少招聘公司",company_day_number)
'''


class SqlQueue(object):  # mysql长连接类
    def __init__(self, host="localhost", user="root", password="123456", database="pa1", charset=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset or 'utf8'
        self.q = Queue(maxsize=3)
        for i in range(0, 3):
            db = pymysql.connect(host=host, user=user, password=password, database=database,
                                 charset='utf8')  # 打开数据库连接
            self.q.put(db)

    def test_conn(self, db):
        # noinspection PyBroadException
        try:
            db.ping()  # 运行ping函数，判断是否断开链接
            return True
        except BaseException:
            return False

    def select(self, sql, fetch_one=False, as_dict=True, as_pd=False):
        results = None
        # 获取数据链接
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        if not self.test_conn(db):
            db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.database, charset=self.charset)  # 重连数据库
        cursor = db.cursor(pymysql.cursors.DictCursor if as_dict else None)  # 使用cursor()方法获取操作游标
        try:
            if as_pd:
                return pd.read_sql(sql, db)
            cursor.execute(sql)  # 执行SQL语句
            if fetch_one:
                results = cursor.fetchone()
            else:
                results = cursor.fetchall()  # 获取所有记录列表
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

    def insert_many(self, sql, *args):
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
            cursor.executemany(sql, *args)  # 执行SQL语句
            db.commit()  # 提交到数据库执行
            # print('插入成功')
        except BaseException as e:
            print('Error: ', e)
            db.rollback()  # 发生错误时回滚
        finally:
            self.q.put(db)

    def __del__(self):
        try:
            while True:
                self.q.get().close()
                if self.q.empty():
                    break
        except BaseException as e:
            print(e)


class SQLAbroad:
    def sql_adroad_code(self):
        mysql_settings = {
            'host': '10.86.0.107',
            'user': 'root',
            'password': 'wit123456',
            'database': 'crawler_statistics_database',

        }
        db = SqlQueue(**mysql_settings)
        select_site_all = "SELECT" + " * from crawler_statistics_database.all_base_table where  country!='中国' and table_name not like '%_add%'"  # 查询国外的数据
        site_country_name = db.select(select_site_all, as_dict=False)  # 获取全部数据

        site_country_name_list = []
        for i in site_country_name:
            item = {}
            item["country_name"] = i[1]  # 国家名称
            item["database_name"] = i[2]  # 数据库名称
            item["tablb_name"] = i[3]  # 表名称
            item["site_name"] = i[4]  # 平台名称
            site_country_name_list.append(item)

        fbar = tqdm(site_country_name_list)
        fbar.set_description('Finished')  # 添加一个计时器

        for i in fbar:
            sql_select_last_time = "SELECT" + f" ADDDATE(MAX(get_Date),INTERVAL 1 hour) last_time from crawler_statistics_database.crawler_pre_statistics_tb where country='{i.get('country_name')}' and site ='{i.get('site_name')}'"
            site_getdate_Max_hour = db.select(sql_select_last_time)  # 获取全部数据
            m = datetime.date.today().strftime('%Y%m')  # 当前年月
            # m = (datetime.date.today()+datetime.timedelta(days=32)).strftime('%Y%m')  # 当前年月

            #如果数据库查不到当天的get_date.则使用今天的时间作为最大时间
            if not site_getdate_Max_hour[0]['last_time']:
                site_getdate_Max_hour[0]['last_time'] = datetime.date.today().strftime('%Y-%m-%d')
                last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),
                                                       '%Y-%m-%d %H')  # 当前时间，精确到小时
                sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE update_time>=CURRENT_DATE() and update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00');"
            else:  # 数据库有这个平台时间的时候,取数据库里最后存的时间，也就是最大值
                m = str(site_getdate_Max_hour[0]['last_time'])[:7].replace('-', '')# 当前年月
                last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),
                                                       '%Y-%m-%d %H')
                sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE update_time>={repr(str(site_getdate_Max_hour[0]['last_time']))} and update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00');"
                # print('boss第二条查询语句#######\n', sql_select_list)
            date_df = pd.DataFrame(
                {'get_date': pd.date_range(str(site_getdate_Max_hour[0]['last_time']), last_time, freq='H', closed='left')})
            if not date_df.shape[0]:
                continue
            list_df = db.select(sql_select_list, as_pd=True)  # 列表页数据
            date_df = pd.DataFrame({'get_date': pd.date_range(str(site_getdate_Max_hour[0]['last_time']), last_time, freq='H',closed='left')})
            print(date_df)
            list_df['get_date'] = list_df['get_date'].astype('datetime64[ns]')
            merge_df = date_df.merge(list_df, on=['get_date'], how='left').merge(list_df.loc[:, ['get_date']],
                                                                                 on=['get_date'], how='left')
            merge_df.country.fillna(i.get('country_name'), inplace=True)  # 遇到nat空值开始填充
            merge_df.site.fillna(i.get('site_name'), inplace=True)
            merge_df.jobNum.fillna(0, inplace=True)
            merge_df.jobInfo_num.fillna(0, inplace=True)
            merge_df.loc[:, 'job_id'] = merge_df.loc[:, ['get_date', 'country', 'site']].astype(str).apply(
                lambda x: hashlib.md5(''.join(x).encode()).hexdigest(), axis=1)
            insert_sql = "INSERt" + " INTO crawler_statistics_database.crawler_pre_statistics_tb (get_date,country, site,job_day_number, jobinfo_day_number,job_id) VALUES(%s,%s,%s,%s,%s,%s)"

            db.insert_many(insert_sql, merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                                                        'jobInfo_num', 'job_id']].values.tolist())
        fbar.close()


class SQLDomestic:
    def sql_domestic_code(self):
        mysql_settings = {
            'host': '10.86.0.107',
            'user': 'root',
            'password': 'wit123456',
            'database': 'crawler_statistics_database',

        }
        db = SqlQueue(**mysql_settings)
        select_site_all = "SELECT" + " * from crawler_statistics_database.all_base_table where  country='中国' and table_name not like '%_add%'"  # 查询国内的数据
        site_country_name = db.select(select_site_all, as_dict=False)  # 获取全部数据

        site_country_name_list = []
        for i in site_country_name:
            item = {}
            item["country_name"] = i[1]  # 国家名称
            item["database_name"] = i[2]  # 数据库名称
            item["tablb_name"] = i[3]  # 表名称
            item["site_name"] = i[4]  # 平台名称
            site_country_name_list.append(item)

        fbar = tqdm(site_country_name_list)
        fbar.set_description('Finished')  # 添加一个计时器

        for i in fbar:
            # for i in list_a:
            sql_select_last_time = "SELECT" + f" ADDDATE(MAX(get_Date),INTERVAL 1 hour) last_time from crawler_statistics_database.crawler_pre_statistics_tb where country='{i.get('country_name')}' and site ='{i.get('site_name')}'"
            site_getdate_Max_hour  = db.select(sql_select_last_time)  # 获取全部数据
            m = datetime.date.today().strftime('%Y%m')  # 当前年月

            # boss直聘
            if 'boss' in i.get('site_name'):
                if not site_getdate_Max_hour[0]['last_time']:  # 数据库没有这个平台时间的时候,取CURRENT_DATE()默认00:00:00
                    site_getdate_Max_hour[0]['last_time'] = datetime.date.today().strftime('%Y-%m-%d')
                    last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),
                                                           '%Y-%m-%d %H')  # 当前时间，精确到小时
                    sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00');"
                    # print('boss第一条查询语句#######', sql_select_list)
                else:  # 数据库有这个平台时间的时候,取数据库里最后存的时间，也就是最大值
                    m = str(site_getdate_Max_hour[0]['last_time'])[:7].replace('-', '')  # 取前七位并把-去掉
                    last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),
                                                           '%Y-%m-%d %H')
                    sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE update_time>={repr(str(site_getdate_Max_hour[0]['last_time']))} and update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00');"
                    # print('boss第二条查询语句#######', sql_select_list)
                date_df = pd.DataFrame(
                    {'get_date': pd.date_range(str(site_getdate_Max_hour[0]['last_time']), last_time, freq='H', closed='left')})
                # print(date_df)
                if not date_df.shape[0]:
                    continue
                list_df = db.select(sql_select_list, as_pd=True)  # 列表页数据
                # date_df = pd.DataFrame({'get_date': pd.date_range(str(all[0]['last_time']),last_time, freq='H',closed='left')})
                list_df['get_date'] = list_df['get_date'].astype('datetime64[ns]')
                merge_df = date_df.merge(list_df, on=['get_date'], how='left').merge(list_df.loc[:, ['get_date']],on=['get_date'], how='left')
                merge_df.country.fillna(i.get('country_name'), inplace=True)  # 遇到nat空值开始填充
                merge_df.site.fillna(i.get('site_name'), inplace=True)
                merge_df.jobNum.fillna(0, inplace=True)
                merge_df.jobInfo_num.fillna(0, inplace=True)

                merge_df.loc[:,'job_id'] = merge_df.loc[:,['get_date','country','site']].astype(str).apply(lambda x: hashlib.md5(''.join(x).encode()).hexdigest(),axis=1)
                insert_sql = "INSERt" + " INTO crawler_statistics_database.crawler_pre_statistics_tb (get_date,country, site,job_day_number, jobinfo_day_number,job_id) VALUES(%s,%s,%s,%s,%s,%s)"

                db.insert_many(insert_sql, merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                                                            'jobInfo_num','job_id']].values.tolist())

                print(f"{i.get('country_name')}'country,'{i.get('site_name')}",
                      len(merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                                           'jobInfo_num']].values.tolist()))
                # insert_sql = "INSERt" + " INTO crawler_statistics_database.crawler_pre_statistics_tb (get_date,country, site,job_day_number, jobinfo_day_number) VALUES(%s,%s,%s,%s,%s)"
                # db.insert_many(insert_sql, merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                #                                             'jobInfo_num']].values.tolist())
                #
                # print(f"{i.get('country_name')}'country,'{i.get('site_name')}",
                #       len(merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                #                            'jobInfo_num']].values.tolist()))
            else:
                if not site_getdate_Max_hour[0]['last_time']: #如果出现新表没有最大存入时间则走这里
                    site_getdate_Max_hour[0]['last_time'] = datetime.date.today().strftime('%Y-%m-%d')
                    last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),'%Y-%m-%d %H')
                    sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE  update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00')"
                    # print('第3条查询语句#######\n', sql_select_list)

                else:
                    m = str(site_getdate_Max_hour[0]['last_time'])[:7].replace('-', '') #查看当前年月
                    last_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d %H'),'%Y-%m-%d %H')#当前的时间，精确到小时
                    sql_select_list = "SELECT" + f" DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00') get_date,'{i.get('country_name')}'country,'{i.get('site_name')}'site,COUNT(id)jobNum,0 jobInfo_num FROM {i.get('database_name')}.{i.get('tablb_name')}_{m}  WHERE update_time>={repr(str(site_getdate_Max_hour[0]['last_time']))} and update_time <'{str(last_time)}' GROUP BY DATE_FORMAT(update_time,'%Y-%m-%d %H:00:00');"

                    # print('第4条查询语句#######\n', sql_select_list)
                date_df = pd.DataFrame({'get_date': pd.date_range(str(site_getdate_Max_hour[0]['last_time']), last_time, freq='H', closed='left')})
                # print(date_df)
                if not date_df.shape[0]:
                    continue
                list_df = db.select(sql_select_list, as_pd=True)  # 列表页数据
                list_df['get_date'] = list_df['get_date'].astype('datetime64[ns]')
                merge_df = date_df.merge(list_df, on=['get_date'], how='left').merge(list_df.loc[:, ['get_date']],on=['get_date'], how='left')
                merge_df.country.fillna(i.get('country_name'), inplace=True)  # 遇到nat空值开始填充
                merge_df.site.fillna(i.get('site_name'), inplace=True)
                merge_df.jobNum.fillna(0, inplace=True)
                merge_df.jobInfo_num.fillna(0, inplace=True)
                # print(merge_df)

                merge_df.loc[:,'job_id'] = merge_df.loc[:,['get_date','country','site']].astype(str).apply(lambda x: hashlib.md5(''.join(x).encode()).hexdigest(),axis=1)
                insert_sql = "INSERt" + " INTO crawler_statistics_database.crawler_pre_statistics_tb (get_date,country, site,job_day_number, jobinfo_day_number,job_id) VALUES(%s,%s,%s,%s,%s,%s)"

                db.insert_many(insert_sql, merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                                                            'jobInfo_num','job_id']].values.tolist())

                print(f"{i.get('country_name')}'country,'{i.get('site_name')}",
                      len(merge_df.loc[:, ['get_date', 'country', 'site', 'jobNum',
                                           'jobInfo_num']].values.tolist()))

        fbar.close()


if __name__ == '__main__':
    S = SQLAbroad()
    T = SQLDomestic()
    while True:
        S.sql_adroad_code()
        T.sql_domestic_code()
        a_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'程序运行完毕，当前时间时间{a_time}'.center(100, '#'))

        time.sleep(3600)

