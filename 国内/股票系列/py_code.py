import execjs
import requests
import json


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "http://www.iwencai.com",
    "Pragma": "no-cache",
    "Referer": "http://www.iwencai.com/unifiedwap/result?w=5G%E6%A6%82%E5%BF%B5%E8%82%A1&querytype=fund&issugs&sign=1687746408541",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    # "hexin-v": "A8PJ6zJ2o7J0LG_GErjxDqpNUoxuOFXOkcSbrvWlHz6YHO16fQjnyqGcK94G"
}
with open(r'js_code.js', "r", encoding='utf8') as f:
    js_hexin = f.read()
cookies_v = execjs.compile(js_hexin).call('token')

cookies = {
    "v": f"{cookies_v}"
}
url = "http://www.iwencai.com/customized/chart/get-robot-data"
data = {
    "source": "Ths_iwencai_Xuangu",
    "version": "2.0",
    "query_area": "",
    "block_list": "",
    "add_info": "{\"urp\":{\"scene\":1,\"company\":1,\"business\":1},\"contentType\":\"json\",\"searchInfo\":true}",
    "question": "5G概念股",
    "perpage": 50,
    "page": 1,
    "secondary_intent": "fund",
    "log_info": "{\"input_type\":\"click\"}",
    "rsh": "Ths_iwencai_Xuangu_3wff331igbydvbeza1kfkk25lawsk0wp"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)
print(response.text)
print(response)