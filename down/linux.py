import os
from yt_dlp import YoutubeDL


# b站爬虫
def biliili_down(detail: dict):
    """
    视频通过视频和音频合并生成
    音频可直接获得最优音频
    """
    path = os.path.abspath(".") + "/"
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