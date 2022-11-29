import os,json
import xlrd


def load_start():
    xlsx = xlrd.open_workbook("something/codes.xlsx")
    sh = xlsx.sheet_by_index(0)
    codes = sh.col_values(0)[1:]
    return codes

codes = load_start()[:100]
files = os.listdir("gubaSpider/data/result")
files = [i.split("_")[0] for i in files]

#检测未下载的数据
undo = []
for code in codes:
    if code not in files:
        undo.append(code)
        print(code)
        
print(undo)
        
        

        
        