# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:12:49 2020

@author: Lenovo
"""
'''from pathlib import path'''
import shutil
import os
import re
print(os.getcwd())
def transferFiles(source,destination)
    entries=os.scandir(source)
    l=[]
    for entry in entries:
        l.append(entry.name)
    arr=[]
    for i in l:
        x=re.search("^[0-9]{4}[a-z A-Z ]+",i)
        if x:
            arr.append(i)
    months={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    for i in arr:
        source_dummy=source
        destination_dummy=destination
        name=i.split('.')
        month=name[0][-7:-5:1]
        source_dummy+='\\'+i
        destination_dummy+=i[0:4]+'\\correspondence'+'\\'+months[month]
        if os.path.isdir(destination):    
            new_path=shutil.move(source_dummy,destination_dummy)
        else:
            os.mkdir(destination_dummy)
            new_path=shutil.move(source_dummy,destination_dummy)
'''entries1=path('D:/')
for entry in entries1.iterdir():
    print(entry.name)'''
