#kartik env (local machine)
#pip install free-proxy
import requests
import os
import urllib

import ip_fxns
import file_fxns
class scrapping_webpage:

    def __init__(self,url,file_name="data.html") -> None:
        self.url = url
        self.html_file_path =  file_fxns._getFilePath(file_fxns.getDataDirectoryPath(),file_name) # by default

    def setHtmlDataFilePath(self,dir_path,file_name):
        self.html_file_path =  file_fxns._getFilePath(dir_path,file_name)

    def getHtmlDataFilePath(self):
        return self.html_file_path

    def _fetchAndSave_withProxy(self,user_proxy):
        r= requests.get(self.url,proxies=user_proxy)        
        #file path
        with open(self.html_file_path,"w",encoding="utf-8") as file:
            file.write(r.text)
        print(f"fetched {self.url} with proxy Ip {user_proxy}" )    

    def _fetchAndSave(self):
        r= requests.get(self.url)
        with open(self.html_file_path,"w",encoding="utf-8") as file:
            file.write(r.text)  
        print(f"fetched {self.url} without proxy Ip")
        
    def fetchData(self):
        try:
            proxies = ip_fxns.getProxies()# //returns {"http":"","https":""}
            ip_fxns.get_my_ip(proxies) 
        except :
            print("unable to log new proxy")    
        try :    
            self._fetchAndSave_withProxy(proxies)

        except Exception as e:
            print(e)
            self._fetchAndSave()

if __name__ == "__main__":
    # sample web scrape 
    url1 ="https://realpython.com/"
    web = scrapping_webpage(url1,"real_python.html")
    web.fetchData()

            








