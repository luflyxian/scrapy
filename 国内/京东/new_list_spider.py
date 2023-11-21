import requests


headers = {
    "authority": "search.jd.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://search.jd.com/search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
cookies = {
    "__jdu": "245517912",
    "shshshfpb": "nvp45CqENKPZuV7uuAiCICw",
    "shshshfp": "06de722a3f537a50efc5452a04c25cb7",
    "shshshfpa": "cfaadd7f-943f-e2d2-a052-fded52d0c751-1679322163",
    "shshshfpx": "cfaadd7f-943f-e2d2-a052-fded52d0c751-1679322163",
    "TrackID": "1b52WODam4BvtsJKKHgvV86Vq43tFTf8DutXSiJ8J-tVEMHAsMfQumvK6bXwXMs5OzD61PAsKJYXKlr4fjqARzQdcaM-BeUk2F0EJwbdSEbU",
    "pinId": "SQ-kJE3ACTzpgi8hQ--2K7V9-x-f3wj7",
    "unpl": "JF8EAK5nNSttXUxXBBhSEkVHQ1xSW1xYSR5RaTcNVA1aTgAMHgcaFER7XlVdXxRKEB9uYhRVX1NKVg4fAisSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAR4WFEtbXF5eOEonBF9XNVNUWE1WBysDKxMgCQkIXVsOQxUFImQAUFlYTVwFGDIaIhM",
    "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_46202a8ff90740a38c7a91a34e84407e|1685819034100",
    "areaId": "2",
    "ipLoc-djd": "2-2830-0-0",
    "shshshsID": "4432a7196062a0aa758342e00a7bf3aa_1_1685819039702",
    "jsavif": "1",
    "__jda": "122270672.245517912.1680357841.1680357842.1685819034.2",
    "__jdc": "122270672",
    "rkv": "1.0",
    "avif": "1",
    "qrsc": "3",
    "3AB9D23F7A4B3C9B": "GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUM",
    "3AB9D23F7A4B3CSS": "jdd03GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUMAAAAMIQKUJUXQAAAAAD7OEEYL6IABLAIX",
    "_gia_d": "1",
    "__jdb": "122270672.6.245517912|2.1685819034",
    "xapieid": "jdd03GSZNRMHTOJHQB3QFPF3U7ZGUPYAIFY73RT2FC7XRAK7BXJ4D7X7KRZ5EYV4G2IR6QPG6NXWYBJ2W4OWWESFOCGDIUMAAAAMIQKUJUXQAAAAAD7OEEYL6IABLAIX"
}
url = "https://search.jd.com/search"
params = {
    "keyword": "手机",
    "wq": "手机",
    "cid3": "13768"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)