import re
import execjs
import requests


headers = {
    "authority": "www.youzhicai.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://www.youzhicai.com/sn/15022E858978-A7C0-4D99-A602-967A31FB4828.html",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url = "https://www.youzhicai.com/sn/15022E858978-A7C0-4D99-A602-967A31FB4828.html"
session = requests.Session()
response = session.get(url, headers=headers)

content = response.text

pattern = re.compile(r'<\b[^>]*>([\s\S]*?)<\/script>')
matches = pattern.findall(content)
response_jscode = ''.join(matches).strip()

head_js = """ 
window = global

window.location ={
    "ancestorOrigins": {},
    "href": "https://www.youzhicai.com/sn/15022E858978-A7C0-4D99-A602-967A31FB4828.html",
    "origin": "https://www.youzhicai.com",
    "protocol": "https:",
    "host": "www.youzhicai.com",
    "hostname": "www.youzhicai.com",
    "port": "",
    "pathname": "/sn/15022E858978-A7C0-4D99-A602-967A31FB4828.html",
    "search": "",
    "hash": "",
	reload: function () {},
}
window.navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    bluetooth: {},
    clipboard:{},
    language: "zh-CN",
    languages: ['zh-CN', 'zh'],
    userAgen:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    webdriver: false
}
const CryptoJS = require('crypto-js')
document ={}
"""
fux_js = """
function get_token() {
	return ck
}"""
full_js = head_js + '\n '+  response_jscode + '\n '  + fux_js

cookie_str = execjs.compile(full_js).call("get_token")

cookies_dict = {c.split("=")[0]: c.split("=")[1] for c in cookie_str.strip().split(";") if len(c.split("=")) == 2}
# cookies = {
#     "__root_domain_v": ".youzhicai.com",
#     "_qddaz": "QD.302187946913308",
#     "ASP.NET_SessionId": "xzy22nh51gswopao4abffrh3",
#     "Hm_lvt_9511d505b6dfa0c133ef4f9b744a16da": "1687946913,1687949246,1688023476",
#     "_qddab": "3-2w522d.ljgtldx7",
#     "Hm_lpvt_9511d505b6dfa0c133ef4f9b744a16da": "1688023999",
# }
# cookies_dict.update(cookies)
print(cookies_dict)
response = session.get(url, headers=headers,cookies=cookies_dict)
print(response.text)