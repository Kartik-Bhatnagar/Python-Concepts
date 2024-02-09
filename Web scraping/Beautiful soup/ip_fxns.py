import requests
import file_fxns
from fp.fp import FreeProxy

def get_my_ip(user_proxies):
    ip_address = (requests.get("https://api.ipify.org?format=json",proxies=user_proxies).json())
    _ip_log(ip_address)

def _ip_log(ip_add):
    dir_path = file_fxns.getDataDirectoryPath()
    file_name = "ip_address.txt"
    log_file_path = file_fxns._getFilePath(dir_path,file_name)
    with open(log_file_path,"a",encoding="utf-8")as lfile:
        lfile.write(str(ip_add)+"\n")

def getProxies():
    print("getting a proxy id")
    http_proxy = FreeProxy(rand=True).get()
    # print(http_proxy)
    proxies = {"http":http_proxy}#,"https":http_proxy}
    return proxies
       

""" Why proxy ::
 
 A proxy is an intermediary server that routes requests from clients looking for resources to servers that provide
   those resources.

Because web scraping requires a large number of requests to a server from a single IP address, the server may 
detect too many requests  and block that IP address to prevent further information collection."""       