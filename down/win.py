import os
import sys
import yt_dlp
import shutil
from merge.m4a.mp4 import merge
from merge.m4a.mp4 import tomp3


def down(detail: dict):
    if "pornhub" in detail["url"]:
        pornhub_down(detail)
    else:
        biliili_down(detail)


# b站爬虫
def biliili_down(detail: dict):
    """
    视频通过视频和音频合并生成
    音频可直接获得最优音频
    """
    if detail["path"] == "":
        path = os.path.abspath(sys.argv[0]).replace("main.py", "")
    else:
        path = detail["path"] + "\\"
    res = os.path.abspath(sys.argv[0]).replace("main.py", "down\\")
    URL = detail["url"]

    title = ""
    down_type = {"mp4": ["bestvideo", "bestaudio"], "mp3": ["bestaudio"]}
    for url in URL:
        inputs = {}
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
            for i in inputs.keys():
                os.remove(i)
        else:
            for i in inputs.keys():
                shutil.move(i, path + title + ".mp3")


# P站爬虫
def pornhub_down(detail: dict):
    """
    视频直接获取
    音频通过ffmepg转换
    """
    path = os.path.abspath(sys.argv[0]).replace("main.py", "")
    res = os.path.abspath(sys.argv[0]).replace("main.py", "down\\")
    url = detail["url"][0]
    down_type = {"mp4": "best", "mp3": "worst"}
    item = down_type[detail["type"]]
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
    if detail['type'] is "mp3":
        inputs = {res + title + "." + item_type: None}
        ffmpeg = detail["ffmpeg"]
        tomp3(inputs, path, title, ffmpeg)
        os.remove(res + title + "." + item_type)
    else:
        shutil.move(res + title + "." + item_type, path + title + "." + item_type)


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
