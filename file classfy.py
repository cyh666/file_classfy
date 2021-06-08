# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:25:21 2021

@author: Hulk
"""

import os
import shutil

# Which folder you want to classfy
os.chdir(r'C:\Users\Hulk\Downloads')

formats = {
        '音頻':['.mp3','.wav'],
        '視頻':['.mp4','.avi','.kmp','.mov','.webm'],
        '圖片':['.jpeg','.jpg','.png','.gif','.bmp'],
        '文檔':['.txt','.pdf','.doc','.docx','.xlsx','.xls','.ppts','.ppt','.csv'],
        '程序':['.exe','.msi'],
        '壓縮':['.zip','.rar','.7z'],
        }


for f in os.listdir():
    ext=os.path.splitext(f)[-1].lower()
    
    for d,exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(f, '{0}/{1}'.format(d,f))
            
print("整理完成")