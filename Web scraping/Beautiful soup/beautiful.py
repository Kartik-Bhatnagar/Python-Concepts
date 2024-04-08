from fetchWebPage import scrapping_webpage
import file_fxns
from bs4 import BeautifulSoup
import time
import os

def gethtmlContent(html_path):
    with open(html_path,"r") as f:
        html_doc = f.read()
    return html_doc

def get_unix_str():
    return str(time.time()).split(".")[0] 

def make_prettify_file(soup,html_dir):
    unix_now = get_unix_str() 
    file_name = soup.title.string[0:min(10,len(soup.title.string))].replace(" ","-")+"_prettify_"+unix_now+".html"
    pretty_file = os.path.abspath(os.path.join(html_dir,"Prettify_files",file_name))
    with open(pretty_file,"w") as pf:
        pf.write(soup.prettify())

# def save_all_div(soup,html_dir):
#     pretty_file = os.path.abspath(os.path.join(html_dir,"div_files",file_name))

url = "https://groww.in/mutual-funds/filter"
data_directory = file_fxns.getDataDirectoryPath()
groww_amc = scrapping_webpage(url) #initiating the web scrapping class
groww_amc.setHtmlDataFilePath(data_directory,"grow_data.html")
html_doc_path = groww_amc.getHtmlDataFilePath()
html_doc = gethtmlContent(html_doc_path)
soup = BeautifulSoup(html_doc,'html.parser')
#make_prettify_file(soup,data_directory)
print(type(html_doc))
# print(soup.find_all("div"))

for link in soup.find_all("a"):
    print(link)