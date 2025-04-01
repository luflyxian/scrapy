import concurrent.futures
import os
import time

import requests


def my_get(url, headers, **kwargs):
    """ 发送 GET 请求，支持重试 """
    err = 0
    while True:
        try:
            response = requests.get(url, headers=headers, timeout=10, **kwargs)
            if response.status_code == 200:
                return response
            else:
                time.sleep(1)
                err += 1
                if err > 5:
                    return None
        except:
            err += 1
            if err > 5:
                return None
            time.sleep(0.5)


def get_download_url(video_url):
    """ 获取视频的下载链接 """
    api_url = "https://p.oceansaver.in/ajax/download.php"
    params = {"format": "1080", "url": video_url}
    headers = {
        "accept": "*/*",
        "referer": "https://y2down.cc/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    }

    response = my_get(api_url, headers=headers, params=params)
    if not response:
        print(f"❌ 获取下载链接失败: {video_url}")
        return None

    video_id = response.json().get("id")
    if not video_id:
        print(f"❌ 无法解析视频 ID: {video_url}")
        return None

    progress_url = "https://p.oceansaver.in/api/progress"
    response = my_get(progress_url, headers=headers, params={"id": video_id})
    if not response:
        print(f"❌ 获取进度失败: {video_url}")
        return None

    download_url = response.json().get("download_url")
    return download_url


def download_video(video_url, output_dir):
    """ 下载单个视频 """
    download_url = get_download_url(video_url)
    if not download_url:
        return

    # 生成唯一文件名（使用 YouTube 视频 ID）
    video_id = video_url.split("/")[-1]
    output_file = os.path.join(output_dir, f"{video_id}.mp4")

    os.makedirs(output_dir, exist_ok=True)

    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"✅ 下载完成: {output_file}")
    else:
        print(f"❌ 下载失败: {video_url}, 状态码: {response.status_code}")



if __name__ == "__main__":
    urls = [
        'https://www.youtube.com/shorts/IQ2XPtKY3Ts',
        'https://www.youtube.com/shorts/nUxCmJgokTc',
        'https://www.youtube.com/shorts/9Yr8k1UsEho',
        'https://www.youtube.com/shorts/l2QGpsMufwk',
        'https://www.youtube.com/shorts/CmACzLonZds',
        'https://www.youtube.com/shorts/92zsQE4z4_8',
        'https://www.youtube.com/shorts/vbKSdhSsIow',
        'https://www.youtube.com/shorts/gAGygA9FYOo',
        'https://www.youtube.com/shorts/nGnEvWd7XYw',
        'https://www.youtube.com/shorts/gAGygA9FYOo',
        'https://www.youtube.com/shorts/_PmVKjmb0Uw',
        'https://www.youtube.com/shorts/laA6RHy1s48',
        'https://www.youtube.com/shorts/ZOgTGvRdYjI',
        'https://www.youtube.com/shorts/KXtpmZwTOIE',
        'https://www.youtube.com/shorts/0HEaGUjFVJI',
        'https://www.youtube.com/shorts/VPOP_OiC94U',
        'https://www.youtube.com/shorts/nI8_pyask18',
        'https://www.youtube.com/shorts/-RkA2M6NPfw',
        'https://www.youtube.com/shorts/VFbOb1Ewxzg',
        'https://www.youtube.com/shorts/lSetw4_ZuV4',
        'https://www.youtube.com/shorts/LtivjrydyRs',
        'https://www.youtube.com/shorts/yAKnTcDPs6E',
        'https://www.youtube.com/shorts/niCDi8LWlGE',
        'https://www.youtube.com/shorts/Yn1NqYxahF0',
        'https://www.youtube.com/shorts/UZJrkD7SUIA',
        'https://www.youtube.com/shorts/HR43m319vfM',
        'https://www.youtube.com/shorts/sojM2oNF9Js',
        'https://www.youtube.com/shorts/2y1nuEiPO5M',
        'https://www.youtube.com/shorts/rfvOpMthi2Q',
        'https://www.youtube.com/shorts/DGbksIDxo2w',
        'https://www.youtube.com/shorts/LSyWtTE1_Os',
        'https://www.youtube.com/shorts/1lseFHum93w',
        'https://www.youtube.com/shorts/FKseUv6EHL8',
        'https://www.youtube.com/shorts/_lEkT9MYsAA',
        'https://www.youtube.com/shorts/ATEn-1uUDwE',
        'https://www.youtube.com/shorts/uQyaQx6EFgg',
        'https://www.youtube.com/shorts/SOYXhzjYUTo',
        'https://www.youtube.com/shorts/vJDrJKZKYyM',
        'https://www.youtube.com/shorts/U5QanE6UGt8',
        'https://www.youtube.com/shorts/KqSmIm9bYH8',
        'https://www.youtube.com/shorts/dUNl7Ykj9qY',
    ]
    output_dir = "./downloads"

    # 使用多线程加速下载
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda url: download_video(url, output_dir), urls)


