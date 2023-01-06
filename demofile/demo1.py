'''import os
dir=os.getcwd()
file=os.listdir(dir)
files=[f for f in file if os.path.isfile(dir+'/'+f)]
print(files)
if text_file1==files:
    print("file is existed")
else:
    print("file not existed")'''
import os,fnmatch
def find(filename,path):
    res=[]
    for root,dirs,files in os.walk(path):
        for names in files:
            if name==filename:
                print("file exist")
                break
            else:
                print("file not exist")
name=input("enter the file name:")
dir="c://Capstronproject"
find(name,dir)