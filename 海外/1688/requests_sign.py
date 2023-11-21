#encoding='utf-8'

#"6345ba3d8757197b7ad8d604bfe046bc&1686299611889&12574478&{"fcGroup":"cbu-seller-fc","fcName":"zgc-promotion-component","serviceName":"categoryBaseInfoService","params":"{\"cateId\":\"54\",\"leafCateId\":\"\"}"}"


# h(d.token + "&" + i + "&" + g + "&" + c.data)
# token + 13位数时间戳 + appKey + data
import time
import re
import execjs

with open(r'1.js', 'r', encoding='utf-8') as f:
    # 读取到调试到的js代码
    jscode = f.read()
# #
# signKey = '6345ba3d8757197b7ad8d604bfe046bc&1686299611889&12574478&{"fcGroup":"cbu-seller-fc","fcName":"zgc-promotion-component","serviceName":"categoryBaseInfoService","params":"{\\"cateId\\":\\"54\\",\\"leafCateId\\":\\"\\"}"}'
# # 将signKey参数传入js代码的h方法中
# ctx = execjs.compile(jscode).call('h', signKey)
# print(ctx)





import requests




headers = {
    "authority": "h5api.m.1688.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://sale.1688.com/",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
cookies = {
    "_m_h5_tk": "97d1baf5ab1e8af4c6b4b9f979fca006_1686314307054",
    "_m_h5_tk_enc": "7da66ca8e03bad32f0e58674fd4e5877",
}
url = "https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/"
params = {
    "jsv": "2.6.1",
    "appKey": "12574478",#12574478
    # "t": "1686296807269",
    # "sign": "5eea444b251d625c0791fe06fd111ee5",
    "type": "jsonp",
    "data": "{\"cid\":\"TpFacRecommendService:TpFacRecommendService\",\"methodName\":\"execute\",\"params\":\"{\\\"query\\\":\\\"mainCate=54&leafCate=\\\",\\\"sort\\\":\\\"mix\\\",\\\"pageNo\\\":\\\"1\\\",\\\"pageSize\\\":\\\"20\\\",\\\"from\\\":\\\"PC\\\",\\\"trafficSource\\\":\\\"pc_index_recommend\\\"}\"}"
}
#
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
#
# print(response.text)
# print(response)
#timestrsleep = str(int(time.time() * 1000)) #时间戳
# token + 13位数时间戳 + appKey + data
timestr = str(int(time.time() * 1000))
appKey= params.get('appKey')
data_str= params.get('data')
token_data = cookies.get('_m_h5_tk').split("_")[0]

signKey = token_data + "&" + timestr + "&" + appKey + "&" +data_str

sign = execjs.compile(jscode).call('h', signKey)

params['sign'] = sign
params['t'] = timestr

response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)

set_cookie_str = response.headers.get('Set-Cookie')
_m_h5_tk= re.search("_m_h5_tk=(.*?);",set_cookie_str).group(1)
_m_h5_tk_enc = re.search("_m_h5_tk_enc=(.*?);",set_cookie_str).group(1)
cookies = {
    "_m_h5_tk": _m_h5_tk,
    "_m_h5_tk_enc": _m_h5_tk_enc,
}

