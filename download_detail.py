#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Time ： 2025/2/25 下午5:52
@Auth ： v_lvxian
@File ：get_download_detail.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import time
import requests
from lxml import etree
import random
from concurrent.futures import ThreadPoolExecutor
import os
import hashlib
import time

# 获取当前时间戳（秒级）
timestamp = str(int(time.time()))
md5_hash = hashlib.md5(timestamp.encode('utf-8')).hexdigest()


# 请求头
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": f"W/\"{md5_hash}\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

# 代理池
PROXIES = [
    'http://10.252.64.29:8890',
    'http://10.252.19.49:8890',
    'http://10.252.17.29:8890'
]

# 结果保存路径
OUTPUT_FILE = 'url_list.txt'
output_dir = os.path.dirname(OUTPUT_FILE)
if output_dir:
    os.makedirs(output_dir, exist_ok=True)
open(OUTPUT_FILE, 'a').close()


def process_url(url):
    """抓取页面中的 Git 项目 URL 并保存到文件"""
    proxy = random.choice(PROXIES)
    proxies = {'http': proxy, 'https': proxy}
    retry_count = 15  # 设置重试次数

    while retry_count > 0:
        try:
            url = url + "?tab=repositories"
            response = requests.get(url=url, headers=headers, proxies=proxies, timeout=30)
            status_code = response.status_code

            # 处理特定的状态码
            if status_code == 429:
                time.sleep(60)
                continue
            elif status_code >= 500:
                time.sleep(10)
                continue
            elif status_code == 404:
                break
            elif status_code != 200:
                break

            # 解析页面内容
            tree = etree.HTML(response.text)
            numbers = tree.xpath("//h3[@class='wb-break-all']/a/@href")

            # 将结果写入文件
            with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
                for numbers_all in numbers:
                    pdf_url = f'https://github.com{numbers_all}.git'
                    f.write(f'{pdf_url}\n')
                    print(f'写入成功: {pdf_url}')
            break  # 成功则跳出重试循环

        except Exception as e:
            retry_count -= 1
            if retry_count == 0:
                print(f"重试次数用尽，放弃请求页面 {url}")
            else:
                time.sleep(1)


if __name__ == '__main__':
    # 示例：定义待爬取的 URL 和语言列表
    with open("ures_url.txt", 'r') as file:
        print('开始运行...')
        urls = [line.strip() for line in file]
        with ThreadPoolExecutor(max_workers=31) as executor:
            executor.map(process_url, urls)
        print('处理完成')
    print("所有任务已完成！")
