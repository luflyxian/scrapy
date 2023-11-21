import requests


headers = {
    "authority": "data.p4psearch.1688.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://p4psearch.1688.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
cookies = {
    # "cna": "qu3GHHtjUh8CAWiVoV3z04eu",
    # "xlly_s": "1",
    # "_m_h5_tk": "624bbd520155c8f1129aba6fc4e6bb6c_1685640089663",
    # "_m_h5_tk_enc": "4a076ed8142c6fad90537ad385c6a702",
    # "cookie2": "12cb840e52e3b56c922bab232c50a5b7",
    # "t": "273ff9845b0791172ea9d97d66461993",
    # "_tb_token_": "e8763348bd366",
    # "__cn_logon__": "false",
    # "isg": "BKWlkF_lLdygDkmj8-kQF45JtGHf4ll0xjwFb6eKYVzrvsUwbzJpRDNcSCLIpXEs",
    # "l": "fBQLVlNuNuW5WpgsBOfaFurza77OSIRYYuPzaNbMi9fP_u1B5IjVW1a9sQT6C3GVFsgeR3kOuRA9BeYBq3xonxvO-8aKbckmndLHR35..",
    # "tfstk": "cHLGBB4s2hS6xbuvdd_s5QgYlN3RwPnNCE8e8jvpb98YN7CmnkrPWDhhBYMac" #固定一体杯高强度防
}
url = "https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json"
params = {
    "beginpage": "2",
    # "asyncreq": "4",
    "keywords": "服饰内衣",
}
# proxies = {"https":"127.0.0.1:7890"}
# response = requests.get(url, headers=headers, cookies=cookies,proxies=proxies, params=params)
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)