from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from os import getcwd,sep

#-*-encoding:utf-8-*-
import csv
import urllib.request as urllib2
import urllib
import pandas as pd
import os

from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active




#data = pd.read_csv("new1.csv")
#for i in range(data.shape[0]):
#        print(i)

i=0
#读取csv文件，csv中每一行需要放入一条youtube链接
with open("new.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        i=i+1
        if(i>=441):
            print("NO.",i,"个：",row[0])
            # 当前进程的工作目录
            cwd = getcwd()
            # 设置chrome驱动器
            driver = webdriver.Chrome(f'{cwd}{sep}chromedriver')
            # 设置超时时间
            driver.set_page_load_timeout(13)
            # 访问
            driver.get(str(row[0]))
            # 等待几秒
#           sleep(3)

            html=driver.page_source
            x = html.find("此频道不存在")
            y = html.find("此帐号已被终止")
    #        f=open('./2.html',mode="w",encoding="utf-8")
    #        f.write(html)

            # 等待几秒
    #        sleep(3)
            rownew=row[0]
            # 推出驱动并关闭所关联的所有窗口
            driver.quit()
            print(x,y)
            if((x==-1)&(y==-1)):
                x=0
            else:
                x=1
            print(x)
            result0 = (rownew,x)
            ws.append(result0)
            if(i%10==0):
                wb.save("sample.xlsx")

print("OVER,准备保存")      
wb.save("sample.xlsx")

print("保存完毕")

