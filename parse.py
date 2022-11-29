import json,requests
import urllib

# urllib.request.unquote(resp.request.__dict__['body'])      
# 'param=postid=1178033003&sort=1&sorttype=1&p=1&ps=30'

#link
url = "https://guba.eastmoney.com/interface/GetData.aspx?path=reply/api/Reply/ArticleNewReplyList"
#header
header = {}
header["Referer"] = "https://guba.eastmoney.com/news,000001,1178033003.html"
header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
#data
data = {}
data["param"] = "postid=1178033003&sort=1&sorttype=1&p=1&ps=30"
#post
resp = requests.post(url,headers=header,data=data)
#parse data
data = json.loads(resp.text)

i = 10
#评论总条数（包含子评论）
data["reply_total_count"] #
#评论条数（主评论）
len(data["re"])
#评论的整体
data['re'][i]
#评论文本
data['re'][i]["reply_text"] #
#评论日期
data['re'][i]["reply_time"] #
#评论点赞
data['re'][i]["reply_like_count"] 
#评论用户信息
data['re'][i]["reply_user"]
#评论用户名
data['re'][i]["reply_user"]["user_nickname"] #
#评论用户ID
data['re'][i]["reply_user"]["user_id"] #
#评论用户年份
data['re'][i]["reply_user"]["user_age"]
#子评论
list(data['re'][i]['child_replys'])

list(data["re"])




#:::::::::::::::::::::::::::::::::::::::::::::::::::::::
import re
import json
url = "https://guba.eastmoney.com/news,000001,1226665075.html"
resp = requests.get(url)
true = True
false = False
null = None
result = re.findall("var post_article = ({.*?});",resp.text)[0]
result = eval(result)

list(result)
#文章数据主要保存
list(result['post'])

#标题
result["post"]["post_title"]
#发布日期
result["post"]["post_publish_time"] #
#点赞数
result["post"]["post_like_count"] #
#文章id
result["post"]["post_id"]

#文本提取
from lxml import etree
content = result["post"]["post_content"]
parse = etree.HTML(content)
text = "".join(parse.xpath("//text()")) #
source = parse.xpath("//span[@class='source']/text()")  
author = parse.xpath("//span[@class='author']/text()")
source = source[0] if source else ""  #
author = author[0] if author else ""  #
print(text)
print(author)
print(source)

