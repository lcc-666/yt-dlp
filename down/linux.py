import os
import shutil
import sys

import yt_dlp


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
    res = os.path.abspath(sys.argv[0]).replace("main.py", "down/")
    url = detail["url"]
    inputs = {}
    title = ""
    down_type = {"mp4": None, "mp3": "bestaudio"}
    item=down_type[detail["type"]]
    opts = {
        #'listformats': True,
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
    # if detail["type"] is "mp3":
    #     shutil.move(res+title+"."+item_type,path+title+"."+detail["type"])
    shutil.move(res + title + "." + item_type, path + title + "." + detail["type"])


if __name__ == '__main__':
    # url:B站视频
    Url = input("请输入视频网址\n")
    # Path:存储目录，最好是空的
    Path = ""
    ffmpeg = r"E:\ffmpeg\bin\ffmpeg.exe"
    Type = "mp4"
    detail_inputs = {
        "url": Url,
        "path": Path,
        "ffmpeg": ffmpeg,
        "type": Type
    }
    biliili_down(detail_inputs)