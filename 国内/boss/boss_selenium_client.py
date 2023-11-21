# -*- coding: utf-8 -*-
import os
import random
import re
import sys
import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import requests
from flask import Flask, request
from selenium import webdriver
from datetime import date, datetime
from selenium.common.exceptions import JavascriptException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
from urllib3.exceptions import MaxRetryError
import redis
import pynput
from pynput.mouse import Button
from hashlib import md5
from gevent import pywsgi

app = Flask(__name__)

mouse = pynput.mouse.Controller()


# 单例模式函数，用来修饰类
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64': base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


@singleton
class Chrome:
    def __init__(self):
        self.current_city = '101010100'
        self.host_url = 'https://www.zhipin.com'
        self.start_page = 'https://www.zhipin.com/web/geek/job?city={}'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.proxies_key_recode = {}.fromkeys(self.client.keys('proxy_DD*'), 0)
        self.is_reload = False
        self.chaojiying = Chaojiying_Client('13311860036', 'Welcome2022', '96001')
        self.driver = self.init()
        self.current_date = date.today()
        self.last_change_url_time = datetime.now()
        self.token = ''
        threading.Thread(target=self.auto_reload, daemon=True).start()

    def auto_reload(self):
        while True:
            time.sleep(60)
            if self.check_error_page():

                self.init()
            self.check_search_page()
            if date.today() != self.current_date:
                self.init()

    def get_proxy(self):
        max_val = max(self.proxies_key_recode.values())
        if max_val > 10:
            min_val = min(self.proxies_key_recode.values())
            self.proxies_key_recode = {key: val - min_val for key, val in self.proxies_key_recode.items()}
        proxy = sorted(self.proxies_key_recode.items(), key=lambda item: item[1])[0][0]
        self.proxies_key_recode[proxy] += 1
        return self.client.get(proxy)

    def get_proxy_test(self):
        return random.choice(self.client.lrange('use_proxies', 0, -1))

    def check_search_page(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'search-btn')), '找不到元素')
        except Exception as e:
            if self.driver.current_url == 'https://www.zhipin.com/web/user/safe/verify-slider':
                if self.verification_code():
                    self.driver.get(self.start_page.format(self.current_city))
            else:
                self.driver.refresh()
                time.sleep(20)

        try:
            self.driver.find_element(By.CLASS_NAME, 'search-btn')
            return True
        except Exception as e:
            if self.driver.current_url == 'https://www.zhipin.com/web/user/safe/verify-slider':
                if self.verification_code():
                    self.driver.get(self.start_page.format(self.current_city))
            else:
                self.driver.refresh()

    def init(self):
        self.close()
        time.sleep(1)
        if not getattr(self, 'driver', None):
            self.is_reload = False
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_argument("--disable-blink-features=AutomationControlled")

            service = ChromeService()

            proxy = self.get_proxy()
            # print(proxy)
            options.add_argument('--proxy-server=http://' + proxy)
            options.add_argument('--user-agent=' + self.user_agent)

            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            try:
                self.driver.get(self.start_page.format(self.current_city))
                time.sleep(5)
                self.check_search_page()
                if self.check_error_page():
                    return self.init()


            except Exception as e:
                self.close()
                print(e)
                time.sleep(5)
                return self.init()
        self.is_reload = True

        return self.driver

    def verification_code(self):
        # 获取验证码按钮
        validate_button_click = self.driver.find_element(By.CLASS_NAME, 'btn')

        # 点击获取取验证码
        validate_button_click.click()
        # 等待验证码加载
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'geetest_item_img')),
                                             '元素没有找到')
        # 获取验证码
        code_element = self.driver.find_element(By.CLASS_NAME, 'geetest_item_wrap')
        code_url = re.search('url\("(.*?)"', code_element.get_attribute('style')).group(1)
        headers = {'user-agent': self.user_agent}
        image_content = requests.get(code_url, headers=headers,timeout=30).content
        with open('code_img.png', 'wb') as f:
            f.write(image_content)
        # 发送打码平台获取验证码坐标
        print(image_content)
        # self.driver.quit()
        # 移动鼠标点击验证码
        img_location = self.driver.find_element(by=By.XPATH, value='//div[@class="geetest_item_wrap"]').location
        print(img_location)
        mouse.position = img_location.get('x') + 1 - 17, img_location.get('y') + 73 - 17
        xx = img_location.get('x') + 1 - 17
        yy = img_location.get('y') + 73 - 17
        mouse.position = xx, yy

        result = self.chaojiying.PostPic(image_content, 9004)
        time.sleep(3)
        pos_list = [[int(_) for _ in x.split(',')] for x in result['pic_str'].split('|')]
        for i, (pos_x, pos_y) in enumerate(pos_list):
            mouse.position = xx + pos_x, yy + pos_y
            mouse.click(Button.left)
            time.sleep(2)

        # 提交 验证验证码
        self.driver.find_element(by=By.XPATH, value='//div[@class="geetest_commit_tip"]').click()
        # 访问列表页面
        try:
            WebDriverWait(self.driver, 15).until(EC.url_changes('https://www.zhipin.com/web/user/safe/verify-slider'),
                                                 '验证失败')
        except Exception:
            self.chaojiying.ReportError(result['pic_id'])
            return False
        return True

    def check_error_page(self):
        try:
            if self.driver.current_url == 'https://www.zhipin.com/web/user/safe/verify-slider':
                self.verification_code()

            content = self.driver.page_source
            if '检查代理服务器' in content or '尝试次数过多' in content or '代理服务器出现问题' in content or '您的 IP 存在异常访问行为' in content:
                self.close()
                time.sleep(5)

                print('网络连接失败，重新启动浏览器')
                return True
        except Exception as e:
            self.close()
            return True

    def get_token(self, seed, ts):

        self.token = self.driver.execute_script(
            f'return encodeURIComponent((new document.zhipinFrame[0].contentWindow.ABC).z({repr(seed)}, parseInt({repr(ts)}) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3))')

        #encodeURIComponent((new document.zhipinFrame[0].contentWindow.ABC).z('lXhb2C9vhqoc6+CKl9o0/BXaEsTpZG0aqsXzreUeuFw=', parseInt('1685974978182')))
        return self.token

    def change_url(self):
        if (datetime.now() - self.last_change_url_time).seconds >= 60 * 60 * 8:
            self.driver.get(self.start_page.format(self.current_city))
            self.last_change_url_time = datetime.now()
            time.sleep(10)

    def __del__(self):
        try:
            self.driver.quit()
        except:
            pass

    def close(self):
        try:
            self.driver.quit()
            self.driver = None
            self.is_reload = False
        except Exception as e:

            pass


@app.route('/getToken')
def get_encrypt():
    params = request.args.to_dict()
    seed, ts = params.get('enc').split(',')
    city_code = params.get('cityCode')

    try:
        if chrome.is_reload:
            token = chrome.get_token(seed, ts)
        else:
            token = chrome.token
            time.sleep(10)
        return token
    except Exception as e:
        print(e)
        time.sleep(10)
        traceback.print_exc()
        return chrome.token


if __name__ == '__main__':
    chrome = Chrome()
    time.sleep(10)
    app.run('0.0.0.0', port=8888)
    # server = pywsgi.WSGIServer(('0.0.0.0', 8888), app)
    # server.serve_forever()
    # app.run('10.86.0.104', port=8888)

#geng_xuekai@51helpdesk.com;yan_xingke@51helpdesk.com;wang_zheng@51helpdesk.com