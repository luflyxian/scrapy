from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import parse
from datetime import datetime, timedelta
import redis
import requests
import time, random
from check_proxy import CheckProxies
import threading

MAX_PROXY_NUM = 2


class ProxyPool(object):
    def __init__(self):
        self.check = CheckProxies()
        self.proxies_key = ['use_proxies', ]
        self.redis_key = 'use_proxies'
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
        self.proxy_url = f"http://www.zdopen.com/ShortProxy/GetIP/?api=202103311108292560&akey=32960bbe0f10ab17&count=10&timespan=1&type=1"
        self.proxy_url1 = f"https://api.xiaoxiangdaili.com/ip/get?appKey=785790964479709184&appSecret=JdNyfUdM&cnt=5&wt=text"
        self.one_proxy_url = "http://api.xdaili.cn/xdaili-api//privateProxy/getDynamicIP/DD20206286711MrI5oz/a1ba37fc971b11e9af127cd30abda612?returnType=1"

        self.check_url = "http://www.xdaili.cn/ipagent/checkIp/ipList?ip_ports%5B%5D="
        self.status = False
        self.proxy_urls = [self.proxy_url, self.proxy_url1]

    # @sched.scheduled_job('interval', id='my_job_id', minutes=10)
    def change_proxies(self):
        """
        更换新的代理ip
        @return: None
        """

        print('%s : 开始更换代理ip' % (datetime.now()))
        for url in self.proxy_urls:
            for x in range(3):
                try:
                    response = requests.get(self.proxy_url, headers=self.headers, timeout=15)

                    # result = response.get("RESULT")
                    # proxy_list = []
                    # for item in result:
                    #     proxy_list.append(item.get('ip') + ':' + item.get('port'))
                    if 'msg' not in response.text:
                        proxy_list = [proxy.strip() for proxy in response.text.split('\n') if proxy.strip() != '']
                        print(proxy_list)
                        # error_proxy = self.client.lpop('proxies')
                        self.client.lpush(self.redis_key, *proxy_list)
                    break
                except Exception as e:
                    print(e)
                    time.sleep(5)

        print('%s : 代理ip更换完成' % (datetime.now()))

    def change_proxy(self):
        """
        更换新的代理ip
        @return: None
        """
        try:
            print('%s : 开始更换代理ip' % (datetime.now()))
            for x in range(5):
                response = requests.get(self.one_proxy_url, headers=self.headers, timeout=15)
                print(response.status_code)
                print(response.text)
                if "拨号" in response.text:
                    time.sleep(10)
                    continue
                elif '10001' in response.text:
                    time.sleep(10)
                    continue
                elif '参数' in response.text:
                    time.sleep(10)
                    continue
                proxy = response.text.strip()
                try:
                    self.client.lpop('proxies')
                except Exception as e:
                    pass
                self.client.lpush('proxies', proxy)
                break

            print('%s : 代理ip更换完成' % (datetime.now()))
        except Exception as e:
            print(e)

    def check_proxies_status(self):
        for proxy_key in self.proxies_key:
            proxies = self.client.lrange(proxy_key, 0, -1)
            res = self.check.check_proxies(proxies)
            for proxy in res:
                self.client.lrem(proxy_key, 0, proxy)

    def check_status(self):
        """
        检查代理ip是否超时
        @return:如果代理ip超时，返回True， 否则返回False
        """

        for proxy_key in self.proxies_key:
            proxies = self.client.lrange(proxy_key, 0, -1)
            if len(proxies):
                proxy_str = '&ip_ports5B%%5D='.join([parse.quote(proxy, encoding='utf-8') for proxy in proxies])
                # print(proxy)
                response = requests.get(self.check_url + proxy_str, headers=self.headers, timeout=15).json()
                # print(response)
                print('%s : 开始检测' % (datetime.now()))
                result = response.get("RESULT")
                for item in result:
                    if "超时" in item.get("time"):
                        timeout_proxy = item.get('ip') + ':' + item.get('port')
                        print('%s : 检测完成，代理ip超时，删除代理ip：%s' % (datetime.now(), timeout_proxy))
                        if proxy_key != 'proxies':
                            self.client.lrem(proxy_key, 0, timeout_proxy)
                        else:
                            self.status = True
                        # return True
                    else:
                        print('%s : 检测完成，代理ip可用。' % (datetime.now()))
                        # return False
            else:
                print("当前代理IP为空")
                if proxy_key == 'proxies':
                    self.change_proxy()
                else:
                    self.change_proxies()

    def run(self):
        """
        代理ip池主流程
        @return: None
        """
        # 检测代理 ip 的是否超时

        # self.check_status()
        # self.check_proxies_status()
        # 查询数据库中代理IP剩余的数量
        # if self.status:
        #     # self.change_proxy()
        #     self.status = False
        # len_proxies = self.count()

        self.change_proxies()

    def count(self):
        """
        @return: 返回数据库中代理IP的数量
        """
        return self.client.llen(self.redis_key)

    def __del__(self):
        """
        程序运行结束关闭redis数据库的链接
        @return: None
        """""
        self.client.close()


if __name__ == '__main__':
    import os

    # sched = BlockingScheduler()
    # proxy_pool = ProxyPool()
    # proxy_pool.run()
    # sched.add_job(proxy_pool.run, 'cron', minute='*/2')
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))
    #
    # sched.start()
    proxy_pool = ProxyPool()
    proxy_pool.run()
    index = 0
    while True:
        time.sleep(15)
        if proxy_pool.count() < 70:
            proxy_pool.change_proxies()
        index += 1
        if index == 3:
            threading.Thread(target=proxy_pool.check_proxies_status).start()

        if index == 4:
            index = 0
