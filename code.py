import time
import requests
from bs4 import BeautifulSoup
import urllib3
import re
import random
import os

def createFile():
    filePath = os.getcwd() + '\\图片'
    if os.path.exists(filePath):
        print('%s:已经存在' % filePath)
    else:
        try:
            os.mkdir(filePath)
            print('新建文件夹：%s' % filePath)
        except Exception as e:
            filePath = '%s %d' % (filePath, len(files))  # 统计文件夹中文件个数
            os.makedirs(filePath)
            # print('新建多层文件夹：%s' % filePath)  # 删除不符合的图片
    return filePath

def Download(l_url, file_name):
    global path
    global header
    global num
    try:
        urllib3.disable_warnings()
        r = requests.get(l_url, stream=True, headers=header, verify=False)  # 用这一命令，边下载边存储
        with open("%s\\%s" % (path, file_name), "wb") as f:
            for cc in r.iter_content(chunk_size=64):  # chunk_size=256 每次写入的字节数256
                f.write(cc)  # 不断写入
        # print("Saved %s" % file_name)  # 当前存下的图片名称
    except:
        time.sleep(3)
        num -= 1
        print('%s没有存下来' %file_name)


def Solve(target_url):
    global path
    global header
    global num
    try:
        urllib3.disable_warnings()
        html = requests.get(target_url, headers=header, verify=False).text
        soup = BeautifulSoup(html, 'lxml')
        # print(soup)  # soup查看，发现与F12内容大有不同
        img_ul = soup.find_all("img", {"class": 'illust-img'})
        for ul in img_ul:
            num += 1
            u = ul['src']
            url = u.split("_master1200")[0]
            if url[-1] != '0':
                url += '_p0'
            url = re.sub('regular', 'original', url) # 否则是缩略图
            url = re.sub('http', 'https', url)
            name = '%d %s' % (num, ul['alt'])
            Download(url + '.jpg', name + '.jpg')   # 图片格式有两种，直接两个都下
            Download(url + '.png', name + '.png')
            try:
                size_1 = os.path.getsize(path + '\\' + name + '.jpg')  # 先存两个，删掉小的那个，大的就是真图
                size_2 = os.path.getsize(path + '\\' + name + '.png')
                if size_2 >= size_1:
                    file = path + '\\' + name + '.jpg'
                    print('图片链接: %s.png\n图片名称: %s.png\n' % (url, name))
                else:
                    file = path + '\\' + name + '.png'
                    print('图片链接: %s.jpg\n图片名称: %s.jpg\n' % (url, name))
                os.remove(file)
                # print('Delete %s' % file)
            except:
                pass
    except Exception as error:
        print(error)
        pass



if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'}
    name_list = ['kiana', 'Bronya%20Zaychik', 'Theresa', 'yuri', 'Seele%20Vollerei', 'Elysia', '%E7%AC%A6%E5%8D%8E',
                 'Durandal', 'Raiden%20Mei', 'Yaezakura', 'Rita',
                 'Cecilia']
    base_url = "https://www.vilipix.com/tags/%s/illusts" % random.choice(name_list)  # 下载的目标网站(在name_list里面随机填一个)
    print('下载的目标网站为: %s' % base_url)
    path = createFile()
    files = os.listdir(path)  # 读入目标文件夹
    num = len(files)  # 统计未下载前文件夹中文件个数
    old_num = num
    Solve(base_url)
    files = os.listdir(path)
    print("共计存下%d张图片" % (len(files) - old_num))
