import os
import sys
import yt_dlp
from yt_dlp import YoutubeDL


def down(detail: dict):
    if "pornhub" in detail["url"][0]:
        pornhub_down(detail)
    else:
        biliili_down(detail)


# b站爬虫
def biliili_down(detail: dict):
    """
    获取视频/音频
    """
    path = os.path.abspath(".")+"\\"
    URLS = detail["url"]

    ydl_opts = {
        'noplaylist': True,
        'format': 'bestaudio',
        "outtmpl": path + '%(title)s.%(ext)s'
    }

    if detail["type"] == "mp4":
        ydl_opts["format"] = None
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
    else:
        ydl_opts["outtmpl"] = path + '%(title)s.mp3'
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)


# P站爬虫
def pornhub_down(detail: dict):
    """
    视频直接获取
    """
    path = os.path.abspath(sys.argv[0]).replace("main.py", "")
    url = detail["url"]

    opts = {
        "format": "best",
        "outtmpl": path + '%(title)s.%(ext)s',
        "noplaylist": True
    }
    ydl = yt_dlp.YoutubeDL(opts)
    ydl.download(url)


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
