import os
import sys
import yt_dlp
from merge.m4a.mp4 import merge

def down(detail:tuple):
    if detail["path"]=="":
        path=os.path.abspath(sys.argv[0]).replace("main.py","")
    else:
        path=detail["path"]+"\\"
    res = os.path.abspath(sys.argv[0]).replace("main.py","down\\")
    url = detail["url"]
    inputs={}
    for item in ["bestvideo", "bestaudio"]:
        opts = {
            "format": item,
            "outtmpl": res + '%(title)s.%(ext)s',
            "noplaylist":True
        }
        ydl = yt_dlp.YoutubeDL(opts)
        # ydl.download([url])
        result = ydl.extract_info(
            url,  # 视频链接
        )
        title = result["title"]
        type = result['ext']
        inputs[res+title+"."+type]=None
    ffmpeg=detail["ffmpeg"]
    merge(inputs,path,title,ffmpeg)
    for i in inputs:
        os.remove(i)


if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认文件目录)\n")
    down(Url, Path)
