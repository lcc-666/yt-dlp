from down.win import down
"""
开始文件
"""
if __name__ == '__main__':
    # url:youtube视频链接
    Url = input("请输入视频地址\n")
    # Path:存储目录，最好是空的
    Path = input("请输入存储目录(默认当前文件目录)\n")
    down(Url, Path)
