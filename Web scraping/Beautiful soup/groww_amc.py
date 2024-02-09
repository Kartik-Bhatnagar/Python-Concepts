#kartik env (local machine)
#pip install free-proxy
import requests
import os
import urllib

import ip_fxns
import file_fxns

def fetchAndSave_withProxy(url,dir_path,file_name,user_proxy):
    r= requests.get(url,proxies=user_proxy)
    file_path =  file_fxns._getFilePath(dir_path,file_name)
    with open(file_path,"w",encoding="utf-8") as file:
        file.write(r.text)

def fetchAndSave(url,dir_path,file_name):
    r= requests.get(url)
    file_path =  file_fxns._getFilePath(dir_path,file_name)
    with open(file_path,"w",encoding="utf-8") as file:
        file.write(r.text)        

proxies = ip_fxns.getProxies()# //returns {"http":"","https":""}
ip_fxns.get_my_ip(proxies) 
url = "https://groww.in/mutual-funds/filter"
data_directory = file_fxns.getDataDirectoryPath()
fetchAndSave_withProxy(url,data_directory,"grow_data.html",proxies)





