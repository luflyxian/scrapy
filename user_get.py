import requests
from lxml import etree
import random
from concurrent.futures import ThreadPoolExecutor
import os
import hashlib
import time
import re

# 获取当前时间戳（秒级）
timestamp = str(int(time.time()))
md5_hash = hashlib.md5(timestamp.encode('utf-8')).hexdigest()

# 你的多个 token
tokens = [
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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",
    "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"
]

headers = {
    "accept": "application/vnd.github.v3+json",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": f"W/\"{md5_hash}\"",
    "referer": "https://github.com",
    "User-Agent": "your-user-agent",
}

# 代理池
PROXIES = [
    'http://10.252.64.29:8890',
    'http://10.252.19.49:8890',
    'http://10.252.17.29:8890'
]


def process_url(url):
    """抓取页面中的 Git 项目 URL 并保存到文件"""
    global request_count  # 使用全局计数器
    proxy = random.choice(PROXIES)
    proxies = {'http': proxy, 'https': proxy}
    retry_count = 15  # 设置重试次数

    token = random.choice(tokens)  # 随机选择一个 token
    headers["Authorization"] = f"Bearer {token}"  # 设置 Authorization 头

    while retry_count > 0:
        try:
            response = requests.get(url=url, headers=headers, proxies=proxies, timeout=30)
            status_code = response.status_code
            if status_code != 200:
                print('程序休息60秒', status_code)
                time.sleep(60)
                continue

            list_url = re.findall('"html_url":"(.*?)"', response.text)
            with open('ures_url_two.txt', 'a') as f:
                for detail in list_url:
                    f.write(detail + '\n')
            print('写入成功', url)
            break  # 成功则跳出重试循环

        except Exception as e:
            retry_count -= 1
            if retry_count == 0:
                print(f"重试次数用尽，放弃请求页面 {url}")
            else:
                time.sleep(1)


if __name__ == '__main__':
    urls = [
        f"https://api.github.com/users?since={i}"
        for i in range(1, 200001111, 30)
    ]
    with ThreadPoolExecutor(max_workers=31) as executor:  # 可调整线程数
        executor.map(process_url, urls)
    print('处理完成')
#wc -l ures_url.txt
