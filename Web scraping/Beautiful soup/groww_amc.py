#kartik env (local machine)
#pip install free-proxy
import requests
import os
import urllib

import ip_fxns
import file_fxns
class scrapping_webpage:

    def __init__(self,url) -> None:
        self.url = url

    def setHtmlDataFilePath(self,dir_path,file_name):
        self.file_path =  file_fxns._getFilePath(dir_path,file_name)

    def fetchAndSave_withProxy(self,user_proxy):
        r= requests.get(self.url,proxies=user_proxy)        
        #file path
        with open(self.file_path,"w",encoding="utf-8") as file:
            file.write(r.text)

    def fetchAndSave(self):
        r= requests.get(self.url)
        with open(self.file_path,"w",encoding="utf-8") as file:
            file.write(r.text)        


url = "https://groww.in/mutual-funds/filter"
data_directory = file_fxns.getDataDirectoryPath()
groww_amc = scrapping_webpage(url)
groww_amc.setHtmlDataFilePath(data_directory,"grow_data.html")
print("hello")

try:
    proxies = ip_fxns.getProxies()# //returns {"http":"","https":""}
    ip_fxns.get_my_ip(proxies) 
    # groww_amc.fetchAndSave_withProxy(proxies)

except Exception as e:
    print(e)
    groww_amc.fetchAndSave()





