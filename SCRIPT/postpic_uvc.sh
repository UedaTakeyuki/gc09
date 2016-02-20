#!/bin/bash
# coding:utf-8 Copy Right Atelier UEDA🐸 © 2016 -

if [ $# -ne 1 ]; then
	device="video0"
else
	device=$1
fi

# 定数
pics_path="/boot/MEDIA/photo"

#LOG=/boot/LOG/postpic.log
LOG=/home/pi/LOG/postpic.log

now=`date +%Y%m%d%H%M%S`
echo "now:"$now>>$LOG &

# 撮影
#fswebcam /tmp/$now.jpg -d /dev/${device} --set framerate=30 2>>$LOG
#fswebcam /tmp/$now.jpg -d /dev/${device} -D 1  2>>$LOG
#fswebcam /tmp/$now.jpg -d /dev/${device} -S 20  2>>$LOG
fswebcam /tmp/$now.jpg -d /dev/${device} -S 20 -r 640x480 2>>$LOG
#fswebcam /tmp/$now.jpg -d /dev/${device} -r 640x480 2>>$LOG

# デバイス名で保存フォルダを（なければ）つくる
folder_name=${now:0:8}
if [ -e ${pics_path}/${device} ]; then
  :
else
  mkdir ${pics_path}/${device} 2>>$LOG
fi

# 年月日で保存フォルダを（なければ）つくる
folder_name=${now:0:8}
if [ -e ${pics_path}/${device}/${folder_name} ]; then
  :
else
  mkdir ${pics_path}/${device}/${folder_name} 2>>$LOG
fi
mv -f /tmp/$now.jpg ${pics_path}/${device}/${folder_name}/. 2>>$LOG &
echo $? >>$LOG &
echo " " >>$LOG &
