import os
import sys
import yt_dlp
import shutil
from merge.m4a.mp4 import merge


def down(detail: dict):
    if "pornhub" in detail["url"]:
        pornhub_down(detail)
    else:
        biliili_down(detail)


# b站爬虫
def biliili_down(detail: dict):
    if detail["path"] == "":
        path = os.path.abspath(sys.argv[0]).replace("main.py", "")
    else:
        path = detail["path"] + "\\"
    res = os.path.abspath(sys.argv[0]).replace("main.py", "down\\")
    url = detail["url"]
    inputs = {}
    down_type = {"mp4": ["bestvideo", "bestaudio"], "mp3": ["bestaudio"]}
    for item in down_type[detail["type"]]:
        opts = {
            "format": item,
            "outtmpl": res + '%(title)s.%(ext)s',
            "noplaylist": True
        }
        ydl = yt_dlp.YoutubeDL(opts)
        # ydl.download([url])
        result = ydl.extract_info(
            url,  # 视频链接
        )
        title = result["title"]
        item_type = result['ext']
        inputs[res + title + "." + item_type] = None
    if len(inputs) == 2:
        ffmpeg = detail["ffmpeg"]
        merge(inputs, path, title, ffmpeg)
    else:
        for i in inputs.keys():
            shutil.copy(i, path + title + ".mp3")

    for i in inputs:
        os.remove(i)

def pornhub_down(detail: dict):
    if detail["path"] == "":
        path = os.path.abspath(sys.argv[0]).replace("main.py", "")
    else:
        path = detail["path"] + "\\"
    res = os.path.abspath(sys.argv[0]).replace("main.py", "down\\")
    url = detail["url"]
    down_type = {"mp4": "best", "mp3": "worst"}
    item=down_type[detail["type"]]
    opts = {
        "format": item,
        "outtmpl": res + '%(title)s.%(ext)s',
        "noplaylist": True
    }
    ydl = yt_dlp.YoutubeDL(opts)
    # ydl.download([url])
    result = ydl.extract_info(
        url,  # 视频链接
    )


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
