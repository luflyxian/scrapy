import requests


headers = {
    "authority": "www.amazon.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "device-memory": "8",
    "downlink": "1.3",
    "dpr": "1.25",
    "ect": "3g",
    # "referer": "https://www.amazon.com/s?i=fashion-womens-clothing&rh=n%3A1045024&fs=true&page=2&qid=1681910703&ref=sr_pg_1",
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
    "lc-main": "enUS",
    # "skin": "noskin",
    # "sp-cdn": "\"L5Z9:JP\"",
    # "session-token": "\"QTdnDE9fPV9wkYtqgHVCvcCitlpGY/6DDsP8h+YXbp6hjmuHn6ioACcjonSpT2Pu8qeqopDR3fW4WZPS3wWRlHvI1JO0f5yPcfgWpI19l+Efc/lj1ov/Exvptp18N9rQWUFE3wCUYkiE6VQe3nK4nWBvZzGlM9s6Lmkwp3QqWvM0lR0BJFhWUDk97+3EoIe3Rs7AkzYaRCPxSM1jw4Cz1sTlniGx5D/73/K4vPOGgzM=\"",
    # "csm-hit": "tb:6X384B5J1ZDVHQST57MW+s-6X384B5J1ZDVHQST57MW|1682521926831&t:1682521926831&adb:adblk_no"
}

# url = "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A281407%2Cn%3A172435&dc&page=2&qid=1682521797&rnid=281407&ref=sr_pg_1"
url = "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A281407%2Cn%3A172435&dc&page=10&qid=1682521942&rnid=281407&ref=sr_pg_3"
url ="https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A281407&ref=nav_em__nav_desktop_sa_intl_accessories_and_supplies_0_2_5_2%5C"
proxies = {"https":"127.0.0.1:7890"}
response = requests.get(url, headers=headers, proxies=proxies,cookies=cookies)

print(response.text)
print(response)