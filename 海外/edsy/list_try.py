import requests


headers = {
    "authority": "www.ebay.co.uk",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9",
    # "referer": "https://www.ebay.co.uk/b/Dried-Artificial-Flowers-Plants/4959/bn_2316857?rt=nc&_pgn=99",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-full-version": "\"112.0.5615.121\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
cookies = {
    "ak_bmsc": "651AB733889F831C5B6C8DB5C1F9773B~000000000000000000000000000000~YAAQJQwtF7g/HYOHAQAAazAJmhNYfZu6RzXSHXxqAWD8apnkjC53nzhGEpMrJeveXxtLpYTbGacqxIFph/8QtsRZtuDyBNIbiD9I3JI3fT9gUO67Jf40B1kHRkppw6ZQwwT20Y4pcmY02qM/YFqj2Zj2I4rrhtZmifyZV5Gp/AroSEVrej9waB+0rZzoM2OWm48Lxds+3OvKjOGE+7Zje+NKj86Xk5p+/LwS9drt/8FaVXjRwVxU8ojLxRlY2qbu7hgWgPwk1JcInSOlEYIATTrLXghGdv49k/hZQIAhssr+ws6HBj08VBfro4Ix53i5416rwiu/EGNzaaHU0nNBXS7DI1g9bhdCl5CBSsqv5D9n5Oz69yd2/7+VOjpskJw9nG9oAAR4XlRAuFY=",
    "__ssds": "3",
    "__uzma": "be301fee-438a-46f3-bfa5-d7e9a9b61b5f",
    "__uzmb": "1681916508",
    "__uzmc": "847241047489",
    "__uzmd": "1681916508",
    "__uzme": "1393",
    "__uzmf": "7f6000ed190c17-01d8-48d1-9998-59dade3a88bc16819165088490-cfa86327ab9bfe9710",
    "__ssuzjsr3": "a9be0cd8e",
    "__uzmaj3": "ead61900-31c9-416a-aa86-bf3c8bae6781",
    "__uzmbj3": "1681916509",
    "s": "CgAD4ACBkQVWFOWEwOTMwMWIxODcwYTc0NDlkYTA4YTBmZmZmZWIwMTBZa35k",
    "dp1": "bu1p/QEBfX0BAX19AQA**68026b0e^bl/US68026b0e^",
    "bm_sv": "5583246CB19CE5CFDDD3A59266716530~YAAQJQwtFyfTHYOHAQAAlNcPmhP8ul7iT6ZtxawdAcQfEwfyDw5pH2lGya63sA+TisHywMHVvixqpp3LOrqNEWsAWFlCmmM+8+xhejWIs4YISkuCWB95tHhlbDymSM4nRamgxyhw4avR1Ntejz5lJsemTIIGRwgFBi7iku9MP8A5dPTFIqr/q8DXSldJs6Z8gxdemIcwwlMemMv4jNt7OIdMxYFbqV/Rs2Fkwf/GDZeE4QrceYrZPinOdHNV+5fd9Q==~1",
    "__uzmcj3": "414297982835",
    "__uzmdj3": "1681916942",
    "nonsession": "BAQAAAYZC69hsAAaAADMABWYhN445MDAxNwDKACBoAmsOOWEwOTMwMWIxODcwYTc0NDlkYTA4YTBmZmZmZWIwMTAAywADZEALFjE0MFxtEIS5VQR9aIrlQ/3DVD0NmzK4",
    "__deba": "QudESfJXufWgnKYxtu8TKO4q8ucLMC737sFdd-s5xtrKTY8sKzQkpvKBanbtxfyNXR8UW1J2_XMwSXzXGqPFGMiJNWqNIPlDO8hhYVfqwfnWfJ-2HZfGGubvoLUnekNmI2wieAbN9SX70rUj1eLmEg==",
    "ebay": "%5Ejs%3D1%5Esbf%3D%23000000%5Epsi%3DAD7Sjx2A*%5E",
    "ds2": "sotr/b9Votz13lNfz^"
}
url = "https://www.ebay.co.uk/b/Dried-Artificial-Flowers-Plants/4959/bn_2316857"
params = {
    "rt": "nc",
    "_pgn": "100"
}
# proxies = {"https":"127.0.0.1:7890"}
# response = requests.get(url, headers=headers,  params=params, proxies=proxies)
response = requests.get(url, headers=headers, params=params)
print(response.text)
print(response)