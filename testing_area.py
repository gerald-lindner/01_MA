'''
Created on 06.07.2016
@author: Gerald Lindner
'''

#tips: response.status 
#C:\Program Files\Python35\Lib\site-packages\scrapy-1.1.0-py3.5.egg\scrapy\settings
import requests #no idea what it does
import time
from stem import Signal
import logging
import os #go get paths
import scrapy #the crawler import
import re #for finding patterns
import pandas as pd #for handling tables
from scrapy.crawler import CrawlerProcess #neccasary?
logger = logging.getLogger('mycustomlogger')

from stem import CircStatus
from stem import Signal
from stem.control import Controller
from random import randint
import time
from time import sleep
 #search engine
url_1="https://www.google.de/search?q=site%3A"
url="www.care.at"#list of url
path_cnames="D:/04_Dropbox/Dropbox/02_Main/04_Uni/02_MA Arbeit/final_output.xlsx"
cnames=pd.read_excel(path_cnames,"Sheet1")
cnames_out=(cnames['de_man'])

path_out = os.path.join(os.path.expanduser('~'), 'Documents', 'MA_output.xlsx')
#path1 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
#path2 = os.path.join(os.path.expanduser('~'), 'Documents', 'ODA_2014_names_test.csv')
number=[]
url_out=[]
all_urls=[]
#creating the urls, must be done in loop before: from 0 works; arrays start at 1 :-)
#for y in range(0,len(cnames_out)):
for y in range(0,100):
    all_urls.append(url_1+url+"+"+cnames_out[y])
def renew_connection():
    with Controller.from_port(port = 9151) as controller:
        controller.authenticate();
        print (controller.get_newnym_wait())
        time.sleep(controller.get_newnym_wait());
        controller.signal(Signal.NEWNYM);
    return;    
def get_tor_exit_ip():
    with Controller.from_port(port = 9151) as controller:
        controller.authenticate()
        for circ in controller.get_circuits():
            if circ.status != CircStatus.BUILT:
                continue
            exit_fp, exit_nickname = circ.path[-1]
            exit_desc = controller.get_network_status(exit_fp, None)
            exit_address = exit_desc.address if exit_desc else 'unknown'
            print(exit_address);

# def wait_id():
#     if controller.is_newnym_available()==False:
#         print (controller.is_newnym_available())
#         time.sleep(20)
#         wait_id()
#     else:
#         print (controller.is_newnym_available())
#         print ("FINAL")

#start of tor 
a = 0
while a < 5:
    a = a + 1;
    renew_connection();
    print (get_tor_exit_ip()); 


# if 
#     print(controller.signal(Signal.NEWNYM))
# else:
    