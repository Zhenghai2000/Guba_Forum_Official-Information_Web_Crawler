
import os,re,json

save_path = "gubaSpider/data/result"
base_dir = "gubaSpider/data/result"


codes = os.listdir("gubaSpider/data/article")

#读取页面链接
with open("gubaSpider/data/page_num_spider_result.json") as f:
    num_page = [json.loads(i.strip()) for i in f.readlines()]
#解析命名
names = {}
a = {}
for i in num_page:
    _id = i["Item_URL"].split(',')[-1].split(".")[0]
    a[_id] = i
    #添加命名
    names[i['code']] = i["Item_DownloadDate"]+" eastmoney guba zixun text_"+i['code']+".csv"
        
for code in codes:
    #读取文章
    with open(os.path.join("gubaSpider/data/article",code)) as f:
        article = [json.loads(i.strip()) for i in f.readlines()]
    #读取评论
    if os.path.exists(os.path.join("gubaSpider/data/comment",code)):
        with open(os.path.join("gubaSpider/data/comment",code)) as f:
            comment = [json.loads(i.strip()) for i in f.readlines()]
    else:
        comment = []
    
    #以article_id连接
    b,c = {},{}
    for i in num_page:
        _id = i["Item_URL"].split(',')[-1].split(".")[0]
        a[_id] = i
    
    for i in article:
        if i['article_code'] in b:
            b[i['article_code']].append(i)
        else:
            b[i['article_code']] = [i]
            
    for i in comment:
        if i['article_code'] in c:
            c[i['article_code']].append(i)
        else:
            c[i['article_code']] = [i]

    #融合
    from tqdm import tqdm
    header = ["Item_URL","Item_Author","Item_Author_url","Item_PostDate","Item_DownloadDate","Item_Title","Item_Views","Item_Likes","Item_Comments","Item_Comment_Description","Item_Comment_Author","Item_Comment_Author_url","Item_Comment_PostDate","news_source","news_author","news_text"]
    if code.split(".")[0] not in names:
        continue
    with open(os.path.join(save_path,names[code.split(".")[0]].replace("*",".")),"w+",encoding="utf8") as f:
        f.write(",".join(header))
        f.write("\n")
        for i in tqdm(b):
            for article in b[i]:
                if i not in c:
                    d={"Item_Comments":"0","Item_Comment_Description":"None","Item_Comment_Author":"None","Item_Comment_Author_url":"","Item_Comment_PostDate":"None"}
                    c[i] = [d]
                if i in c: 
                    for comment in c[i]:
                        line = ""
                        line += '"https://guba.eastmoney.com'+a[i]["Item_URL"]+'",'
                        line +=  a[i]["Item_Author"]+","
                        line += '"https://guba.eastmoney.com'+a[i]["Item_Author_url"]+'",'
                        line += article["Item_PostDate"]+",";
                        line += a[i]["Item_DownloadDate"]+","
                        line += a[i]["Item_Title"]+","
                        line += a[i]["Item_Views"]+","
                        
                        line += str(article["Item_Likes"])+",";
                        line += str(comment["Item_Comments"])+","
                        line += '"'+comment["Item_Comment_Description"]+'",'
                        line += comment["Item_Comment_Author"]+","
                        if comment["Item_Comment_Author_url"]:
                            line += '"https://i.eastmoney.com/'+comment["Item_Comment_Author_url"]+'",'
                        else:
                            line += 'None,'
                            
                        line += comment["Item_Comment_PostDate"]+","
                        
                        if article["news_source"]:
                            line += '"'+article["news_source"][3:]+'",';
                        else:
                            #来源是否存在于文本中判断
                            if "来源"== article["news_text"][:2]:
                                article["news_source"] = article["news_text"].split("  　　")[0]
                                line += '"'+article["news_source"][3:]+'",';
                            else:
                                line += 'None,';
                        if article["news_author"]:
                            line += '"'+article["news_author"][4:]+'",';
                        else:
                            line += 'None,';
                        article["news_text"] = re.sub("\.[a-z]* {.*}",'',article["news_text"])
                        line += '"'+article["news_text"]+'"';
                        line = line.replace("\n","")
                        line+="\n"
                        f.write(line)
                        
                    
    
    
    
        
    
    
        
