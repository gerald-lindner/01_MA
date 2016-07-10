'''
Created on 06.07.2016

@author: geri
'''
#this version is for desktop pcs
import scrapy #the crawler import
import re #for finding patterns
import pandas as pd #for handling tables
from scrapy.crawler import CrawlerProcess #neccasary
url=[]#list of url
number=[1] #the actual counting number

names_path="D:/Dropbox/Dropbox/2_BTSync Sync/04_Uni/02_MA Arbeit/ODA_2014_names_test.csv"
names=pd.read_csv(names_path, encoding='latin1',sep=';')

for y in range(0,6):#creating the urls, must be done in loop before: from 0 works
    url_t="https://www.google.at/search?q=site%3Awww.care.at+"+names['rename'][y]
    url.append(url_t)
    
class googlengo(scrapy.Spider): #scrapy class, contains everything
    name = 'googlengo'
    start_urls = url
    def parse(self,response):
        number_t=response.xpath('//div[@id="resultStats"]/text()').extract()
        number_t=re.findall("(\d*) ",number_t[0])
        number.append(number_t[1])
process = CrawlerProcess()
process.crawl(googlengo)
process.start()

number_df=pd.DataFrame(number)
#print(number_df)
#print(names)
frames=[names,number_df]
all_df=pd.concat(frames,axis=1,join='outer')
#writing all_df to xlsx
writer=pd.ExcelWriter('D:/Dropbox/Dropbox/2_BTSync Sync/04_Uni/02_MA Arbeit/output.xlsx')
all_df.to_excel(writer,'Sheet1')
writer.save()
print(all_df)
#undone printing
#wusel dusel