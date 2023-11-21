import requests


headers = {
    "authority": "api.m.jd.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://item.jd.com",
    "referer": "https://item.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-referer-page": "https://item.jd.com/100046392938.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    # "__jdu": "245517912",
    # "shshshfpb": "nvp45CqENKPZuV7uuAiCICw",
    # "shshshfp": "06de722a3f537a50efc5452a04c25cb7",
    # "shshshfpa": "cfaadd7f-943f-e2d2-a052-fded52d0c751-1679322163",
    # "shshshfpx": "cfaadd7f-943f-e2d2-a052-fded52d0c751-1679322163",
    # "TrackID": "1b52WODam4BvtsJKKHgvV86Vq43tFTf8DutXSiJ8J-tVEMHAsMfQumvK6bXwXMs5OzD61PAsKJYXKlr4fjqARzQdcaM-BeUk2F0EJwbdSEbU",
    # "pinId": "SQ-kJE3ACTzpgi8hQ--2K7V9-x-f3wj7",
    # "jcap_dvzw_fp": "WQkH9NcS052OetzXCiNpJcXyznd-8Jqzplf4A-oyfUo-34VzTJoWRC0rHR_xTQgRDnnjWw-mxu098xtNJIqJiA==",
    # "unpl": "JF8EAK5nNSttXUxXBBhSEkVHQ1xSW1xYSR5RaTcNVA1aTgAMHgcaFER7XlVdXxRKEB9uYhRVX1NKVg4fAisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAR4WFEtbXF5eOEonBF9XNVNUWE1WBysDKxMgCQkIXVsOQxUFImQAUFlYTVwFGDIaIhM",
    # "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_46202a8ff90740a38c7a91a34e84407e|1685819034100",
    # "areaId": "2",
    # "3AB9D23F7A4B3C9B": "GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUM",
    # "ipLoc-djd": "2-2830-51803-0",
    # "jsavif": "1",
    # "__jda": "122270672.245517912.1680357841.1685819034.1685973123.3",
    # "__jdc": "122270672",
    "token": "cba821f40298421f529237eb28885a62,2,936651",
    # "__tk": "gWhtRzhXkEpPSuIbgZIJSafYkWXPnuX6AdfJSrhXmsXQXZ4xAbkdSYI1AdIKXYX5AdIgRcMv,2,936651",
    # "3AB9D23F7A4B3CSS": "jdd03GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUMAAAAMIRPLC57YAAAAADKQ3UJGK5TIUJYX",
    # "_gia_d": "1",
    # "__jdb": "122270672.3.245517912|3.1685973123"
}
url = "https://api.m.jd.com/"
params = {
    "appid": "pc-item-soa",
    "functionId": "pc_detailpage_wareBusiness",
    "client": "pc",
    # "clientVersion": "1.0.0",
    # "t": "1685973250675",
    "body": "{\"skuId\":100056769283,\"cat\":\"9987,653,655\",\"area\":\"2_2830_51803_0\",\"shopId\":\"100056769283\",\"venderId\":1000107961,\"paramJson\":\"{\\\"platform2\\\":\\\"1\\\",\\\"specialAttrStr\\\":\\\"p0ppppppppp2p1ppppppppppppp\\\",\\\"skuMarkStr\\\":\\\"00\\\"}\",\"num\":1,\"bbTraffic\":\"\"}",
    # "h5st": "20230605215410776;5819525813062254;fb5df;tk03w95a71bdf18nYKjz9AgvNOHT1wpUE9iInmTaUoX91KA3Dhh8F8UQMnCGMTpGA_x8OEpBwNXAKkfzs_QX1dS6reKr;add912e337798fa1c32815ce9a50d4551fa0ad4d35ce3eb7ed204d8674e0cb5e;3.1;1685973250776;24c9ee85e67cf80746dd82817ecbeafc7a829b35c7f446a4c7d476cc9faa1d8834a93323ad7bce9bef1bba682b93d2e3ff9d06896271a0324cf28b8b6ba164c3d5b42ef99584252e724a107f3f4c775d709be8107766ec18c53edc7f512eca30",
    # "x-api-eid-token": "jdd03GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUMAAAAMIRPLC57YAAAAADKQ3UJGK5TIUJYX",
    "loginType": "3",
    # "uuid": "122270672.245517912.1680357841.1685819034.1685973123.3"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)