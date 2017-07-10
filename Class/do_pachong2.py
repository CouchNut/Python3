# coding=utf-8
# 保存到txt文件中
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import datetime
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def getHtml(url):
    page = urllib.request.urlopen(url)
    html_data = page.read()
    return html_data


def getImg(html_data):
    # src=" 开头 .jpg  "> 结尾
    reg = r'src="(.+?\.jpg)">'
    img_reg = re.compile(reg)
    img_list = re.findall(img_reg, html_data)
    return img_list


def cbk(a, b, c):
    """
    回调函数 
    @a:已经下载的数据块 
    @b:数据块的大小 
    @c:远程文件的大小 
    """
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


def downloadImg(img_list):
    x = 0
    for img_url in img_list:
        try:
            print('===== download =====')
            print('download image %s' % x)
            # python3 不能用原来的 urllib.urlretrieve 而要用 urllib.request.urlretrieve
            urllib.request.urlretrieve(img_url, 'data/%s.jpg' % x, cbk)
        except urllib.request.HTTPError as e:
            print('HTTPError:', e.code)
            print('HTTPError:', e.reason)
            continue
        except urllib.request.URLError as e:
            print('URLError:', e.reason)
            continue
    x += 1


def printImgUrlFromHtml(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    img_tag_list = soup.find_all('img')
    img_list = []
    x = 0
    for img_tag in img_tag_list:
        img_url = img_tag.get('src')
        print('image[%s]:' % x, img_url)
        # saveFile(img_url)
        img_list.append('image[%s]: %s \n' % (x, img_url))
        x += 1
    saveLinesFile(img_list)

def saveFile(data):
    save_path = 'data/images1.txt'
    # wb 写入二进制
    # w  写入文本
    # 1.打开文件
    file_point = open(save_path, 'w+')
    # 2.写入数据
    file_point.write(data)
    # 3.关闭文件
    file_point.close()


def saveLinesFile(lines_data):
    time_str = time.strftime("%Y-%m-%d", time.localtime())
    print(time_str)
    save_path = 'data/%s.txt' % time_str
    # wb 写入二进制
    # w  写入文本
    # 1.打开文件
    file_point = open(save_path, 'w')
    # 2.写入数据
    file_point.writelines(lines_data)
    # 3.关闭文件
    file_point.close()

html = getHtml('https://site.douban.com/120100/')
html_str = html.decode('utf-8')

# 正则匹配 查找图片
image_list = getImg(html_str)


# 打印图片地址
printImgUrlFromHtml(html_str)