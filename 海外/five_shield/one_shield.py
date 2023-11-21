
import threading
import time
import json
import undetected_chromedriver as uc
import datetime
import redis
import traceback
import os
import shutil
import re


def check_error(func):
    def check(*args, **kwargs):
        for x in range(1):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                print(e)
                print(traceback.print_exc())
                continue
        return False

    return check


@check_error
def set_cookies(proxy):
    driver = None
    try:

        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--proxy-server=%s" % proxy)
        # print(thread_names.getName())

        try:
            path_user_data_dir = r"E:\ProgramData\Spider_all\test_log" + fr"\{threading.current_thread().name}"
            if os.path.exists(path_user_data_dir):
                print('清空文件夹', shutil.rmtree(path_user_data_dir))

        except Exception as e:
            print(e)
        chrome_options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
        driver = uc.Chrome(
            options=chrome_options, enable_cdp_events=True, auto_config=False,
            driver_executable_path=r"E:\ProgramData\Anaconda3\envs\spider\chromedriver.exe",
            headless=False, user_data_dir = path_user_data_dir )
        driver.get(url)
        time.sleep(15)
        cookies_list = driver.get_cookies()
        indeed_cookies = '; '.join(item for item in [item["name"] + "=" + item["value"] for item in cookies_list])
        # print("查看cookies:",indeed_cookies)
        if 'cf_clearance' not in indeed_cookies:
            for i in range(1,4):
                driver.refresh()
                time.sleep(15)
                cookies_list = driver.get_cookies()
                indeed_cookies = '; '.join(item for item in [item["name"] + "=" + item["value"] for item in cookies_list])
                # print(indeed_cookies)
                if 'cf_clearance' in indeed_cookies:
                    #判断是否返回了正确的cookies，正确则跳出循环
                    break
            if 'cf_clearance' not in indeed_cookies:
                #当三次循环都没有获取正确的cookies时，则直接跳出函数，关闭浏览器
                driver.service.stop()
                driver.quit()
                return False
        if 'rjc' in indeed_cookies:
            indeed_cookies = re.search("cf_clearance=(.*)", indeed_cookies).group()
        cookie_str = json.dumps({proxy: indeed_cookies})
        client.lpush('careessma_cookies', cookie_str)
        print('查看cookies', cookie_str)
        a_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'cookies获取成功,ip{proxy},时间{a_time}'.center(100, '#'))
        time.sleep(3)

        driver.service.stop()
        driver.quit()
        return cookie_str

    except Exception as e:
        print(e)
        try:
            driver.service.stop()
            driver.quit()

        except Exception as e:
            # print(e)
            pass
        return None




def run(proxy_redis_key):
    """
    程序的入口
    :param proxy_redis_key:
    :return:
    """
    proxy = client.get(proxy_redis_key)
    while True:
        cookie_str = set_cookies(proxy)
        if not cookie_str:
            proxy = client.get(proxy_redis_key)
            time.sleep(3)


if __name__ == '__main__':
    url = "https://careesma.in/jobs?q=java"

    order_list = ['proxy_DD20229145910YN1Rqy',
                  'proxy_DD20206286711MrI5oz',
                  'proxy_DD20229148333RQkwU0',
                  'proxy_DD202212152327c0cbhj',
                   'proxy_DD20221215869092oGdq'
                  ]

    client = redis.Redis('10.86.0.107', decode_responses=True)
    thread_names = []
    print("开始运行")
    pool = []
    for i, _proxy_key in enumerate(order_list):
        f = threading.Thread(target=run, args=(_proxy_key,), name=f'indeed_{i}')
        thread_names.append(f'caressma_{i}')
        f.start()
        pool.append(f)
    for f in pool:
        f.join()
    # say({'aa':'bb'}, proxy)
