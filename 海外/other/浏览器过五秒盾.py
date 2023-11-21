import os
import random
import shutil
from functools import partial
import re
import threading
import requests
from urllib import parse
import time
import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import redis
import warnings
from concurrent.futures import ThreadPoolExecutor
import traceback
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    )


def recode(*args, info_type='INFO', **kwargs):
    info_type_pro = ' '.join(str(_) for _ in args)
    info_type_suf = json.dumps(kwargs)

    if info_type.upper() == 'INFO':
        logging.info(info_type_pro + ' ' + info_type_suf)
    elif info_type =='DEBUG':
        logging.debug(info_type_pro + ' ' + info_type_suf)
    elif info_type =='ERROR':
        logging.error(info_type_pro + ' ' + info_type_suf)
    else:
        logging.debug(info_type_pro + ' ' + info_type_suf)

# warnings.filterwarnings('ignore')
# ls = []
# ThreadPoolExecutor(4).submit(sum, [14153])

def check_error(func):
    def check(*args, **kwargs):
        for x in range(1):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as e:
                recode(e)
                recode(traceback.print_exc())
                continue
        return False
    return check

def check_flag(p, flag):
    if not flag.result():
        recode('没有cookie')
        p.shutdown(wait=False)
        return
    recode('有cookies')

def say(params, proxy):
    try:
        pool = ThreadPoolExecutor(1)
        add = partial(check_flag, pool)
        while True:
            pool.submit(get_token, params, proxy).add_done_callback(add)
            time.sleep(2.5)
    except:
        return False

@check_error
def get_token(params, proxy):
    try:
        headers = {
            "authority": "www.indeed.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.indeed.com",
            "referer": params['request']['headers']['Referer'],
            "sec-ch-ua": "\"Chromium\";v=\"114\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"114\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        cookies = {}
        data = {key: val[-1] for key, val in parse.parse_qs(params['request']['postData']).items()}
        proxies = {'https': proxy, 'http': proxy}
        response = requests.post(url, headers=headers, cookies=cookies, data=data, proxies=proxies, timeout=30)
        cookies = requests.utils.dict_from_cookiejar(response.cookies)

        # 数据正常
        if 'cf_clearance' not in cookies:
            return False

        # 保存cookie
        start_urls = [
            ["https://jp.indeed.com/", "https://sg.indeed.com/", "https://it.indeed.com", "https://in.indeed.com/",
             "https://www.indeed.com/stc"],
            ["https://ca.indeed.com/", "https://de.indeed.com/", "https://fr.indeed.com", "https://au.indeed.com/",
             "https://www.indeed.com/stc", "https://uk.indeed.com/"],
            ["https://www.indeed.com/stc"],
        ]
        all_site_urls = set()
        [all_site_urls.update(x) for x in start_urls]
        # recode(proxy, '################\n', cookies)

        if re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$', proxy):
            # json_cookie = json.dumps({proxy: cookies})
            pat = re.compile(r'//([a-z]+)\.', re.I)
            cookie_str = json.dumps({proxy: cookies})
            for _url in all_site_urls:
                if pat.search(_url).group(1) == 'www':
                    client.lpush('indeed_try', cookie_str)
                    recode('查看cookies', cookie_str)
                else:
                    client.lpush(pat.search(_url).group(1) + '_indeed_cookies', cookie_str)

            a_time = datetime.datetime.now().strftime('%H:%M:%S')
            recode(f'cookies获取成功,ip{proxy},时间{a_time}'.center(100, '#'))

        return True

    except Exception as e:
        recode(e,info_type='error')
        recode(traceback.print_exc(),info_type='error')
        return False


def get_proxy():
    # url = "https://share.proxy.qg.net/pool?key=600BBDD2&num=5&area=&isp=&format=txt&seq=%5Cn&pool=1"
    url = "https://share.proxy.qg.net/pool?key=EB373AD0&num=10&area=&isp=&format=txt&seq=%5Cn&pool=1"

    proxies_data = requests.get(url).text.strip().splitlines()

    proxies_pool.extend(proxies_data)
    redis_data = redis.Redis(host='10.86.0.107', port=6379,decode_responses=True)
    redis_data.ltrim('sub_proxies',1,0)
    redis_data.lpush("sub_proxies",*proxies_data)

@check_error
def set_cookies(proxy):
    driver = None
    req_params = None
    try:
        try:
            path_user_data_dir = r"C:\Users\lu.xian\Desktop\try\selenium_cookie_data\user_log"+ f"/{threading.current_thread().name}"
            if os.path.exists(path_user_data_dir):
                print('清空文件夹', shutil.rmtree(path_user_data_dir))
        except Exception as e:
            print(e)
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--proxy-server=%s" % proxy)
        # chrome_options.add_argument("--window-size=300,300")
        recode(proxy)
        chrome_options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})

        driver = uc.Chrome(
            options=chrome_options,
            enable_cdp_events=True,
            auto_config=False,
            driver_executable_path=r"C:\Users\lu.xian\AppData\Local\Programs\Python\Python37\chromedriver.exe",
            headless=False, user_data_dir=path_user_data_dir
        )
        # driver.minimize_window()
        driver.get(url)
        # recode(driver.get_cookies())
        time.sleep(3)
        while True:
            try:
                # driver.implicitly_wait(20)
                WebDriverWait(driver, 45).until(EC.visibility_of_element_located((By.TAG_NAME, 'iframe')), '')
                driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
                # WebDriverWait(driver,20).until(EC.visibility_of_any_elements_located((By.ID, 'cf-stage')),'cf-stage未找到')
                # driver.find_element(By.ID, 'cf-stage').click()

                WebDriverWait(driver, 15).until(EC.visibility_of_any_elements_located((By.XPATH, '//span[@class="mark"]')), '')
                driver.find_element(By.ID, 'cf-stage').click()
                # driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
                break  # //input[@type="checkbox"]
            except Exception as e:
                print(e)
                recode("没有点击验证框，刷新页面",info_type='error')
                # content = driver.page_source
                # if '未连接到互联网' in content or '无法访问此网站' in content or '代理服务器出现问题' in content or '您的 IP 存在异常访问行为' in content:
                recode("网络出错")
                driver.service.stop()
                driver.quit()
                return

        start_time = int(time.time())
        is_break = False

        while True:  # '//*[@id="cf-stage"]/div[6]/label/input'
            logs = driver.get_log('performance')
            for log in logs:
                logjson = json.loads(log["message"])["message"]
                if logjson['method'] == 'Network.requestWillBeSent':
                    params = logjson['params']
                    try:
                        requestUrl = params['request']['url']

                        if requestUrl == url and 'POST' == params['request']['method']:
                            req_params = params
                            is_break = True
                            break
                        else:
                            continue
                    except:
                        requestUrl = "None"
                        recode("没找到requestUrl：{}".format(requestUrl),info_type='error')
                        continue
                else:
                    continue

            if is_break:
                break
            if time.time() - start_time > 60:
                break
        if driver:
            driver.service.stop()
            driver.quit()
        else:
            pass
        return req_params

    except Exception as e:
        if isinstance(e,ConnectionResetError) and req_params:
            return req_params
        recode(e,info_type='error')
        try:
            driver.service.stop()
            driver.quit()

        except Exception as e:
            recode(e,info_type='error')
            pass
        return None


def get_param(proxy_redis_key):
    while True:

        if not len(proxies_pool):
            get_proxy()
            print("关闭全部浏览器")
            time.sleep(30)
            os.system('taskkill /im chrome.exe /F')
            time.sleep(2)
        proxy = random.choice(proxies_pool)
        time.sleep(2)
        # proxy = "127.0.0.1:7890"
        if proxy in recode_mapping[proxy_redis_key] and recode_mapping[proxy_redis_key][proxy] >= 3:
            recode('代理ip失效：', proxy)
            time.sleep(1)
            continue
        elif proxy not in recode_mapping[proxy_redis_key]:
            recode_mapping[proxy_redis_key].clear()
            recode_mapping[proxy_redis_key][proxy] = 0

        params = set_cookies(proxy)
        if params:
            recode_mapping[proxy_redis_key][proxy] = 0
            break
        recode_mapping[proxy_redis_key][proxy] += 1
        time.sleep(2)
        if proxy in proxies_pool:
            proxies_pool.remove(proxy)
        recode('代理ip【{}】连续：【{}】次失败'.format(proxy, recode_mapping[proxy_redis_key][proxy]))

    return params, proxy


def run(proxy_redis_key):
    """
    程序的入口
    :param proxy_redis_key:
    :return:
    """
    params, proxy = get_param(proxy_redis_key)
    # recode(params,proxy)
    # 循环生成cookie
    while True:
        say(params, proxy)
        params, proxy = get_param(proxy_redis_key)


if __name__ == '__main__':
    url = "https://www.indeed.com/jobs?q=java&l="
    proxies_pool = list()
    order_list = ['one', 'two', 'three','four','five']
    # order_list = ['one']
    client = redis.Redis('10.86.0.107', decode_responses=True)
    recode_mapping = {k: {client.get(k): 0} for k in order_list}
    if not len(proxies_pool):
        get_proxy()
    thread_names = []
    recode("开始运行")
    for i, _proxy_key in enumerate(order_list):
        f = threading.Thread(target=run, args=(_proxy_key,), name=f'indeed_{i}')
        thread_names.append(f'indeed_{i}')
        f.start()
    # say({'aa':'bb'}, proxy)
    # requests.get(url,proxies=[],auth=(username,password))