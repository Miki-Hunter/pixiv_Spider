# pyinstaller -F -w -i min.ico code.py
# filePath = os.getcwd()
# cd filePath
"""
首先在命令行(在pycharm的终端即可)输入cd filePath
filePath 就是code.py所在地址(复制即可)
然后键入 pyinstaller -F -w -i min.ico code.py(要事先添加Pyinstaller)
这里 -i min.ico 用于修改exe文件的图标,可以不添加，(与code.py处于同一目录下)

详细可查看此图：
https://github.com/Miki-Hunter/pixiv_Spider/blob/main/img_files/py%E6%96%87%E4%BB%B6%E8%BD%AC%E4%B8%BAexe%E6%96%87%E4%BB%B6%E6%AD%A5%E9%AA%A4.jpg


生成3个文件,双击dist里面的exe文件即可运行
若要打包在其他电脑使用，把exe文件和pyc文件放在同一个文件夹即可，对方电脑不需要安装相关环境

打包样例：
https://github.com/Miki-Hunter/pixiv_Spider/blob/main/img_files/%E6%89%93%E5%8C%85exe.zip
"""
