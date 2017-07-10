# 1.最简单的爬虫

# 导入库
from urllib import request

def simple_pachong():	
	# 请求
	response = request.urlopen('http://www.baidu.com')
	# 解码
	content = response.read().decode('utf-8')
	# 输出
	print(content)

# 2. 增加搜索参数
# 在百度中搜索‘中国’

import urllib.request
def searchKeyWorlds_pachong():
	data = {}
	data['word'] = '中国'
	url_values= urllib.parse.urlencode(data)
	url = 'http://www.baidu.com/s?'
	# 组合搜索的get请求
	full_url = url + url_values
	# 请求
	data = urllib.request.urlopen(full_url).read()
	# 解码
	data = data.decode('UTF-8')
	# 打印
	print(data)


