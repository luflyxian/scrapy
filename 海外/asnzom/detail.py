import requests
import time


timeStamp= int(time.time())

headers = {
    "authority": "www.amazon.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "device-memory": "8",
    "downlink": "1.3",
    "dpr": "1.25",
    "ect": "3g",
    "referer": "https://www.amazon.com/s?i=fashion-womens-clothing&rh=n%3A1045024&fs=true&page=399&qid=1681911524&ref=sr_pg_399",
    "rtt": "300",
    "sec-ch-device-memory": "8",
    "sec-ch-dpr": "1.25",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-viewport-width": "1536",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "viewport-width": "1536"
}
cookies = {
    # "session-id": "132-0457207-4788762",
    # "i18n-prefs": "USD",
    # "ubid-main": "131-6095297-7196553",
    # "session-id-time": "2082787201l",
    "lc-main": "en_US",
    # "sp-cdn": "\"L5Z9:HK\"",
    # "session-token": "5QzFquEWNqCps6BgN0Z1KCmNWTUwpG0UV+GcfgZ603lpbYBidqaf1TCvw7ozdES5ImMlcHR3V1e3lAbxTWqvddusFBLuoVHIYvoJWZBtznsy3cMK7g5Mm0zTcdcOU5znV4KHWQvg/OGHfiuNabDC4m0mYgUeKb/PU45/mQvFkWt0dOZooRqhK3vT3KkGaRpxc9HdXeDMisGSS0QhzXfK/ZzR8UxOqRlq/Z4APaM1PiQ=",
    # "csm-hit": "tb:GNKAAYPR18JJ3D635QE2+s-GNKAAYPR18JJ3D635QE2|1682357982054&t:1682357982055&adb:adblk_no"
}
url = "https://www.amazon.com/Womens-Solid-Sleeve-Summer-Dresses/dp/B09SM4M1LS/ref=sr_1_19105"
params = {
    "qid": f"{timeStamp}",
    "s": "apparel",
    "sr": "1-19105"
}
# url= "https://www.amazon.com/Micger-Galaxy-Ultra-Screen-Protector/dp/B0BNVKH3TY/ref=sr_1_1_sspa?qid=1685631129&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQWVRGNzVIR0pYREwmZW5jcnlwdGVkSWQ9QTEwMDg4NTExSjdTOURaNlJNSUg1JmVuY3J5cHRlZEFkSWQ9QTA0Njg1MjAySkk0SkRNMTlIUE1PJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
proxies = {"https":"127.0.0.1:7890"}
url ="https://www.amazon.com/Micger-Galaxy-Ultra-Screen-Protector/dp/B0BNVKH3TY/ref=sr_1_1_sspa?qid=1685631129&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQWVRGNzVIR0pYREwmZW5jcnlwdGVkSWQ9QTEwMDg4NTExSjdTOURaNlJNSUg1JmVuY3J5cHRlZEFkSWQ9QTA0Njg1MjAySkk0SkRNMTlIUE1PJndpZGdldE5hbWU9c3BfYXRmX2Jyb3dzZSZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
response = requests.get(url, headers=headers,  proxies=proxies,cookies=cookies)

print(response.text)
print(response)

#PLEASE ORDER 1-2 SIZE UP FOR A FITTED LOOK.❗❗❗Unique Style