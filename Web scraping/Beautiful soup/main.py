from fetchWebPage import scrapping_webpage
import file_fxns
import ip_fxns

url = "https://groww.in/mutual-funds/filter"
data_directory = file_fxns.getDataDirectoryPath()
groww_amc = scrapping_webpage(url) #initiating the web scrapping class
groww_amc.setHtmlDataFilePath(data_directory,"grow_data_1.html")
groww_amc.fetchData()



# url2 = "https://python-course.eu/oop/inheritance.php"
# python_course = scrapping_webpage(url2)
# python_course.fetchData()
