import sys
sys.path.append("gubaSpider/gubaSpider/")

import os,json,requests,datetime,xlrd

save_path = "gubaSpider/data/page_num_spider_result.json"
base_dir = "gubaSpider/data/page_num_spider"
files = os.listdir(base_dir)
files.sort()

#截取前一百
files = files[:1000]



#一个items
def get_items(path):
    with open(path) as f:
        items = f.readlines()
        items = [json.loads(i.strip()) for i in items]
        items = sorted(items,key=lambda x : x["page"])
        #剔除不是资讯的文章
        print(len(items))
        items = [i for i in items if "资讯"==i["Item_Author"][-2:]]
    return items

#读取年份
from proxy import Proxy_request
from useragent import USER_AGENT
import re
true = True
false = False
null = None

pr = Proxy_request()
pr.hds = USER_AGENT

def get_date(link):
    resp = pr.get_request("https://guba.eastmoney.com"+link)
    print("https://guba.eastmoney.com"+link)
    html = resp.text
    result = re.findall("var post_article = ({.*?});",html)
    if result:
        result = eval(result[0])
        post_time = result["post"]["post_publish_time"]
        post_time = datetime.datetime.fromisoformat(post_time)
        return post_time
    else:
        return None

       
#获取指定范围的数据
def get_range(items,target):
    target = datetime.datetime.fromisoformat(target) 
    if get_date(items[-1]["Item_URL"])>=target:
        return items
    length = len(items)
    l = 0
    r = length-1
    mid_date = None
    mid = (l+r)//2+1
    while (l<r):
        mid = (l+r)//2
        mid_date = get_date(items[mid]["Item_URL"])
        print("###",mid_date)
        
        #当日期为空，剔除数据，因为可能页面不存在，如：https://guba.eastmoney.com/news,000001,750827856.html
        if not mid_date:
            items.pop(mid)
            length = len(items)
            r -= 1
            continue
        
        if(mid_date>target):
            l = mid+1
        elif(mid_date<target):
            r = mid-1
        else:
            break
        
    while not mid_date and mid<length:
        items.pop(mid)
        length = len(items)
        mid_date = get_date(items[mid]["Item_URL"])
    
    if not mid_date:
        return items[:mid]
    
    while(mid_date>=target and mid<length):
        mid+=1
        old = mid_date
        mid_date = get_date(items[mid]["Item_URL"])
        if not mid_date:
            items.pop(mid)
            mid_date = old
            mid-=1
        
        
        print(":::",mid)
    return items[:mid]

import json
from tqdm import tqdm
for path in tqdm(files): 
    path = os.path.join(base_dir,path)
    items = get_items(path)
    if not items:
        continue

    try:
        new_item = get_range(items,target="2017-01-01")
    except:
        continue
    with open(save_path,"a") as f:
        for i in new_item:
            item = {}
            item["page"] = i["page"]
            item["code"] = i["code"]
            item["Item_Views"] = i["Item_Views"]
            item["Item_Title"] = i["Item_Title"]
            item["Item_DownloadDate"] = i["Item_DownloadDate"]
            item["Item_Author_url"] = i["Item_Author_url"]
            item["Item_Author"] = i["Item_Author"]
            item["Item_URL"] = i["Item_URL"]

            f.write(json.dumps(item)+"\n")
            


      
      
      
            
