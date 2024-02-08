#kartik env (local machine)
import requests
import os
def setDataDirectory(dir_name):
    dir_path = os.path.abspath(os.getcwd()+"./"+dir_name) #go one dir back 
    os.mkdir(dir_path)#create a directory there

def getDataDirectoryPath():
    dir_path = os.path.abspath(os.getcwd()+"./"+"data_webscrape")
    if os.path.exists(dir_path):
        return dir_path
    else:
        dir_name= "data_webscrape"
        setDataDirectory(dir_name)
        return dir_path

def fetchAndSave(url,dir_path,file_name):
    r= requests.get(url)
    file_path =  os.path.abspath(os.path.join(dir_path,file_name))
    with open(file_path,"w",encoding="utf-8") as file:
        file.write(r.text)

def get_my_ip():
    print(requests.get("https://api.ipify.org?format=json").json())
    


url = "https://groww.in/mutual-funds/filter"
data_directory = getDataDirectoryPath()
# fetchAndSave(url,data_directory,"grow_data.html")
get_my_ip()



