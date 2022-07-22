import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'main.py',
    '-F',
    "--distpath=."
])


def rmdir(dir):
    # 判断是否是文件夹，如果是，递归调用rmdir()函数
    if (os.path.isdir(dir)):
        # 遍历地址下的所有文件及文件夹
        for file in os.listdir(dir):
            # 进入下一个文件夹中进行删除
            rmdir(os.path.join(dir, file))
        # 如果是空文件夹，直接删除
        if (os.path.exists(dir)):
            os.rmdir(dir)
            # print(dir,"文件夹删除成功")
    # 如果是文件，直接删除
    else:
        if (os.path.exists(dir)):
            os.remove(dir)
            # print(dir,"文件删除成功")


path = os.path.abspath(".") + "\\"
rmdir(path+"build")
rmdir(path+"main.spec")