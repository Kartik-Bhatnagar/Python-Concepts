import os

def _getFilePath(dir_path,file_name):
    #returns joining the dir_paht with the fileName
    return(os.path.abspath(os.path.join(dir_path,file_name)))

def _setDataDirectory(dir_name):
    dir_path = os.path.abspath(os.getcwd()+"./"+dir_name) #go one dir back 
    os.mkdir(dir_path)#create a directory there

def getDataDirectoryPath():
    dir_path = os.path.abspath(os.getcwd()+"./"+"data_webscrape")
    if os.path.exists(dir_path):
        return dir_path
    else:
        dir_name= "data_webscrape"
        _setDataDirectory(dir_name)
        return dir_path

