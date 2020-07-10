import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  #如果发送了一个失败请求(非200响应),#我们可以通过 Response.raise_for_status() 来抛出异常:
        r.encoding= r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*?\"',html) #正则表达式来匹配 "view_price":"\d\."类型的字符串
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)#正则表达式来匹配 "raw_title":".*?"类型的字符串,.*?是任意字符的最小匹配
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print ("")


def PrintGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print (tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print (tplt.format(count,g[0],g[1]))
def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList=[]
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html= getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue

    PrintGoodsList(infoList)

main()