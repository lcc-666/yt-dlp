import os
import sys
import yt_dlp


def down(url, path):
    if path is "":
        res = os.path.abspath(sys.argv[0])
        path = res.replace("win.py", "")
    url = url
    path = path + "\\"
    opts = {
        "outtmpl": path + '%(title)s.%(ext)s',
        # 'listformats': True,
        'noplaylist': True
    }
    ydl = yt_dlp.YoutubeDL(opts)
    ydl.download([url])
    # result = ydl.extract_info(
    #     url,  # 视频链接
    #     download=True,  # 不下载只是抽取信息
    # )
    print()


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
    down(Url, Path)
