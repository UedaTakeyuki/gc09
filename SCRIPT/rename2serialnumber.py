# coding:utf-8 Copy Right Atelier UEDA🐸 © 2016 -
import sys
import os
import re
a = 1
#指定する画像フォルダ
files = os.listdir('/boot/MEDIA/timelapse')
for file in files:
    jpg = re.compile("jpg")
    if jpg.search(file):
        print file
        os.rename('/boot/MEDIA/timelapse/'+file, "/boot/MEDIA/timelapse/image%06d.jpg" %(a))
        a+=1
    else:
        pass
