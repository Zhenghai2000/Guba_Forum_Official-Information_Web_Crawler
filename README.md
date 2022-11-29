# Guba_Forum_Official-Information_Web_Crawler
Instruction for Guba forum comment web-crawler
2022-10-07
Prepared by Zhenghai Chi
目录
1. Introduction	1
2. Background Information	1
3. Technical Details	2


1. Introduction

This document is an instruction for the use of Guba forum comment web-crawler, which is a web-crawler project for “资讯” and its text as well as the comment. We collect data based on the list of the Chinese listed firms since 2017.01.01. We scrape the “Item URL”, “Item_Author”, “Item_Author_url”, “Item_PostDate”, “Item_DownloadDate”, “Item_Title”, “Item_Views”, “Item_Likes”, “Item_Comments”, “Item_Comment_Description”, “Item_Comment_Author”, “Item_Comment_Author_url”, “Item_Comment_PostDate”, “news_source”, “news_author”, “news_text” (16 variables in total). The estimated time of overall collection is about 10 days. The final data will be saved in directory “Guba forum comment web-crawler\gubaSpider\data\final_data”. Furthermore, please clear up all data in “article”、”comment”、”page_num_spider” as well as JSON documents under the directory “Guba forum comment web-crawler\gubaSpider\data”.

2. Background Information

1. Data Source:  Eastmoney – Guba forum – “资讯”
2. Source Website: 平安银行(000001)资讯_平安银行最新消息—东方财富网股吧 (eastmoney.com) (sample: 平安银行 - 000001) 
3. Starting cut-off date for the crawling: 2017.01.01 for Eastmoney Guba forum
4. Variable Definitions (there is only one sheet in each CSV file):
5. Final data will be saved in “~\Guba forum comment web crawler\gubaSpider\data\final data”
Table 1
Variable	Definition
Item URL	The website link of news
Item_Author	Name of news poster
Item_Author_url	Personal page link of 
Item_PostDate	Date of post
Item_DownloadDate	Download date
Item_Title	news title
Item_Views	How many people see click this news
Item_Likes	How many people like this news
Item_Comments	The number of comments within the news
Item_Comment_Description	The content of the comment. If it is not applicable, we mark None
Item_Comment_Author	The author of the comment. If it is not applicable, we mark None
Item_Comment_Author_url	The personal page of news comment. If it is not applicable, we mark None
Item_Comment_PostDate	the post date of each comment. If it is not applicable, we mark None
news_source	The source of news. If it is not applicable, we mark None
news_author	The author of news. If it is not applicable, we mark None
news_text	The text of news (we only collect text, excluding table and data)

3. Technical Details

Before running the code, please check if your environment has installed some packages (the suggested Python version is 3.8).
Or you can install these packages in the command interface in advance:
pip install xlrd==1.2.0
pip install Scrapy

The idea of web-crawler design:
1. We record the existing page of “资讯” and then acquire the link to the relevant website.
2. As per the website link we have downloaded before, we scrape the data and cut out the correct period, where we can use multiprocessing. However, limited by the extraction of proxy IP, this method may cause congestion in IP extraction and execution, which can omit some important data.
3. Scraping the comment and textual information following the previously collected link.
4. parsing and combining the downloaded data into a CSV file.
5. Due to unknown reasons, some data are being left out so I develop one code to detect this situation, which will return a list of omitted codes. Copying and pasting the list to “gubaSpider\data\page_num_spider” and running again.

Note:
1. The comment will be recorded as below if it uses some emoji. E.g.,
 
The comment will be recorded as “[怒] [怒] [怒]” in our final dataset.
2. Among extant data omissions, some are induced by the inevitable anti-crawler mechanism, and others are data omissions in Guba’s database.

The detail of the use of the code
1. firstly, typing “D:” in cmd (WIN+R to open the cmd, and confirm after typing “cmd”) interface
 
 
Changing directory to: cd ~/Guba forum comment web-crawler\gubaSpider
And then run the command “scrapy crawl page_num_spider”. Note: to speed up the program, there is not any cache mechanism, so the interruption means the loss and restart.
2. Changing directory to: cd ~/Guba forum comment web-crawler
And then run the command “python gubaSpider/page_num_spider_parse.py”. The data in this part will be saved in JSON format, which is convenient for parsing later.
3. Changing directory to: cd ~/Guba forum comment web-crawler\gubaSpider
Run the command “scrapy crawl article_spider”, which will start web-crawler to scrape pertinent comments and textual information.
4. Changing directory to: cd ~/Guba forum comment web-crawler
Run the command “python gubaSpider/combine_data.py” to start the python program, which will parse the data we have scraped and then combine them into a CSV file.
5. Due to some reasons, there may be omission after crawling. Therefore, I develop one code to detect the anomaly.
Changing directory to: cd ~/Guba forum comment web-crawler
Run the command “python gubaSpider/ find_download_failure.py”, which will return the list of omitted code. Copying and pasting in the 19th line within program ” page_num_spider.py” and duplicating the previous command.
 
The missions are due to the data loss in Guba’s database, which is because of delisting (68 in total)。
