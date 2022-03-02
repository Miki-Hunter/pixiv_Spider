import time
import requests
from bs4 import BeautifulSoup
import urllib3
import re
import os
def Download(l_url,file_name):
    global path
    global he
    global num
    try:
        urllib3.disable_warnings()
        r = requests.get(l_url, stream=True, headers=he, verify=False)  # 用这一命令，边下载边存储
        with open("%s\\%s" % (path, file_name), "wb") as f:
            for cc in r.iter_content(chunk_size=64):  # chunk_size=256 每次写入的字节数256
                f.write(cc)  # 不断写入
        print("Saved %s" % file_name)
    except:
        time.sleep(3)
        num-=1
        print('没有存下来')
def Solve(target_url):
    global path
    global he
    global num
    try:
        urllib3.disable_warnings()
        html = requests.get(target_url, headers=he, verify=False).text
        soup = BeautifulSoup(html, 'lxml')
        img_ul = soup.find_all("img", {"class": 'illust-img'})
        for ul in img_ul:
            num+=1
            u = ul['src']
            url = u.split("_master1200")[0]
            if url[-1]!='0':
                url+='_p0'
            url = re.sub('regular', 'original', url)
            url = re.sub('http', 'https', url)
            name ='%d %s' %(num,ul['alt'])
            print(url,name)
            Download(url + '.jpg', name + '.jpg')
            Download(url + '.png', name + '.png')
            try:
                size_1 = os.path.getsize(path +'\\'+ name + '.jpg')  # 先存两个，删掉小的那个，大的就是真图
                size_2 = os.path.getsize(path +'\\' + name + '.png')
                if size_2 >= size_1:
                    file = path +'\\' + name + '.jpg'
                else:
                    file = path +'\\' + name + '.png'
                os.remove(file)
                print('Delete %s' %file)
            except:
                pass
    except Exception as error:
        print(error)
        pass
if __name__ == '__main__':
    he = {
        'User-Agent': 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'}
    base_url = "https://www.vilipix.com/tags/Rita/illusts"  # 下载的目标网站
    path = "C:\\Users\\吴华\\Desktop\\python练习\\spider\\pixiv_img"
    files = os.listdir(path)  # 读入目标文件夹
    num = len(files)  # 统计文件夹中文件个数
    old_num=num
    Solve(base_url)
    print("共计存下%d张图片" %(len(files)-old_num))
