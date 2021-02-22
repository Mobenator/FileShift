import os


import os

def getFolderNames():
    foldersArray = [f.path for f in os.scandir(parentFolder) if f.is_dir()]
    return foldersArray

parentFolder = r'C:\Users\moben'

print(getFolderNames())

