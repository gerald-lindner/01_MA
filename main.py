'''
Created on 06.07.2016

@author: geri
'''
#this version is for desktop pcs
import os #go get paths
import scrapy #the crawler import
import re #for finding patterns
import pandas as pd #for handling tables
from scrapy.crawler import CrawlerProcess #neccasary
url=[]#list of url
number=[1] #the actual counting number

path1 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
path2 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
path3 = os.path.join(os.path.expanduser('~'), 'Documents', 'MA_output.xlsx')

names=pd.read_csv(path1, encoding='latin1',sep=';')
url_1="https://www.google.de/search?q=site%3Awww.care.at+"
url_2="&gws_rd=cr&ei=oJmHV6myLYeUaI38tZgD"
for y in range(0,len(names)):#creating the urls, must be done in loop before: from 0 works

    url_t=url_1+names['rename'][y]+url_2
    url.append(url_t)
    
class googlengo(scrapy.Spider): #scrapy class, contains everything
    name = 'googlengo'
    start_urls = url
    def parse(self,response):
        try:
            number_t=response.xpath('//div[@id="resultStats"]/text()').extract()
            number_t=re.findall("(\d*) ",number_t[0])
            number.append(number_t[1])
        except:
            number.append("0")
process = CrawlerProcess()
process.crawl(googlengo)
process.start()

number_df=pd.DataFrame(number)
#print(number_df)
#print(names)
frames=[names,number_df]
all_df=pd.concat(frames,axis=1,join='outer')
#writing all_df to xlsx
writer=pd.ExcelWriter(path3)
all_df.to_excel(writer,'Sheet1')
writer.save()
print(all_df)