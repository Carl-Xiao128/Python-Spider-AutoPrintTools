#coding = utf-8
import requests
from lxml import etree
import random
import time
import json

class Wdb():#####这只是写入数据库的一个类

	def __init__(self,host = '192.168.10.200',user = 'webroot',password = 'root1234',database = 'analysis'):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	def connection(self):
		self.conn = pymssql.connect(host = self.host,user = self.user,password = self.password,database = self.database)
		self.cur = self.conn.cursor()

	def execute(self,sql):
		self.cur.execute(sql)

	def close(self):
		self.cur.close()
		self.conn.close()


def spider(url,headers,data):  ####这个就是爬虫的主体，发请求，response.text就是服务器响应的回复内容

	response = requests.post(url = url,headers = headers,data = data)
	return response.text

######下边都是处理响应数据之类或者调用spider之类的函数

########################################################################################

def deal_general_data(req_data):
	req_data = json.loads(req_data)
	yesterday_data = req_data['data']['items'][1][1:]
	return yesterday_data

def deal_general_visit_page_data(req_data):
	req_data = json.loads(req_data)
	ok_data = {}
	page_url = []
	detailed_data = []
	for i in req_data['data']['items'][0]:
		page_url.append(i[0]['name'])
	for d in req_data['data']['items'][1]:
		detailed_data.append(d)
	# print(dict(zip(page_url,detailed_data)))
	return dict(zip(page_url,detailed_data))


#处理概况
def execute_general_data():
	headers = {
	'Accept':'text/plain, */*; q=0.01',
	# 'Accept-Encoding': 'gzip, deflate, br',
	# 'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Content-Length':'62',
	'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie':'BAIDUID=98C5DB4C3F4FA25B3B9F51040928019E:FG=1; BIDUPSID=98C5DB4C3F4FA25B3B9F51040928019E; PSTM=1523155525; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1421_21120_22159; PSINO=5; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02731835677; uc_login_unique=317a590fc68f00734af4984d795dc7a1; uc_recom_mark=cmVjb21tYXJrXzM0MTkzNDA%3D; SFSSID=5fs0efcm5r3dv3rf1h0qauikr1; __cas__st__=fce8849da6798a97aec23bedce93b4ea55651a3eb3510ede49ac5ddbdd0c20fa85c277f1e41cf29f252f17cf; __cas__id__=3419340; Hm_lvt_41fc030db57d5570dd22f78997dc4a7e=1523171122; Hm_lpvt_41fc030db57d5570dd22f78997dc4a7e=1523171122; Hm_ct_41fc030db57d5570dd22f78997dc4a7e=306*1*3419340',
	'Host':'tongji.baidu.com',
	'Origin':'http://tongji.baidu.com',
	'Referer':'http://tongji.baidu.com/web/overview/index?castk=7a65dor7063908a08d052',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
	}

	url ='https://tongji.baidu.com/web/3419340/ajax/post'

	data = {
	'siteId':948879,
	'reportId':1,
	'method':'overview/getOutline',
	'queryId':""
	}
	print(json.dumps(data))
	json_data = spider(headers = headers,url = url,data = data)
	ok_data = deal_general_data(json_data)
	# write_database(ok_data)
	print("pv_count","visitor_count","ip_count","bounce_ratio","avg_visit_time","trans_count")
	print(ok_data)
	# sql = "insert into analysis.dbo.visit_page ('',)"
	#添加写入数据库




#处理受访数据
def execute_general_visit_page_data():
	headers = {
	"Accept": "text/plain, */*; q=0.01",
	# "Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Connection": "keep-alive",
	"Content-Length": "255",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": "BAIDUID=98C5DB4C3F4FA25B3B9F51040928019E:FG=1; BIDUPSID=98C5DB4C3F4FA25B3B9F51040928019E; PSTM=1523155525; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1421_21120_22159; PSINO=5; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a02731835677; uc_login_unique=317a590fc68f00734af4984d795dc7a1; uc_recom_mark=cmVjb21tYXJrXzM0MTkzNDA%3D; SFSSID=5fs0efcm5r3dv3rf1h0qauikr1; __cas__st__=fce8849da6798a97aec23bedce93b4ea55651a3eb3510ede49ac5ddbdd0c20fa85c277f1e41cf29f252f17cf; __cas__id__=3419340; Hm_lvt_41fc030db57d5570dd22f78997dc4a7e=1523171122; Hm_ct_41fc030db57d5570dd22f78997dc4a7e=306*1*3419340; locale=zh; Hm_lpvt_41fc030db57d5570dd22f78997dc4a7e=1523175943",
	"Host": "tongji.baidu.com",
	"Origin": "https://tongji.baidu.com",
	"Referer": "https://tongji.baidu.com/web/3419340/visit/toppage?siteId=948879",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"
	}

	url = 'https://tongji.baidu.com/web/3419340/ajax/post'
	num = 0

	while num<=2980:
		data = {
		"siteId": "948879",
		"st": "1523030400000",
		"et": "1523030400000",
		"indicators": "exit_count,average_stay_time,ip_count,visit1_count,pv_count,visitor_count",
		"order": "pv_count,desc",
		"offset": num,
		"target": -1,
		"flag": "overview",
		"reportId": 14,
		"method": "visit/toppage/a",
		"queryId": ""
		}
		json_data = spider(headers = headers,url = url,data = data)
		ok_data = deal_general_visit_page_data(json_data)
		print(ok_data)
		#添加写入数据库	
		for purl,pd in ok_data.items():
			# sql = "insert into analysis.dbo.visit_page (page_url,page_pv_num,page_uv_num,page_ip_num,entry_page_num,exit_page_num,average_stay_time,data_time) values('%s','%d','%d','%d','%d','%d','%d','%s')"%(purl,pd[0],pd[1],pd[2],pd[3],pd[4],pd[5],pd[6])
			print(purl,pd[0],pd[1],pd[2],pd[3],pd[4],pd[5],pd[6])
		num = num + 20

#处理趋势
def execute_trend_data():
	pass



####主函数
if __name__ == '__main__':
	req = execute_general_visit_page_data()
	# f = open('t.json','w',encoding = 'utf-8')
	# f.write(req)
