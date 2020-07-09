#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 20:48:14 2020

@author: plkrishna2211
"""
import os as s
def delabo(di):
    tot=0
    ls=s.listdir(di)
    for i in ls:
        tot=tot+s.path.getsize(di+'//'+i)
    #print(tot)
    if tot>=3000:
        for i in ls:
            s.remove(di+'//'+i)
import time
if __name__=='__main__':
    ip='exp'
    while True:
        delabo(ip)
        time.sleep(1800)
        

        