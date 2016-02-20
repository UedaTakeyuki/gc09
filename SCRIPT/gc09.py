# coding:utf-8 Copy Right Atelier UEDA🐸 © 2016 -
#
import sys 
sys.path.append("/home/pi/SCRIPT")
import datetime 
import time
import subprocess
import logging
import traceback
import os.path
import glob

import ConfigParser
import inspect

import videodevices
import led

# 定数
postpic = "/home/pi/SCRIPT/postpic_uvc.sh"
configfile = '/home/pi/SCRIPT/config.ini'
reboot = 'sudo reboot'

# グローバル
g_count_of_file_ioerrors=0   # File IOERROR の回数。３回連続する場合、再起動する


# ログファイルの設定
logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename='/home/pi/LOG/gal4.engine.log',level=logging.DEBUG)

def msg_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.info(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def msg_err_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.error(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def inc_file_ioerror():
    global g_count_of_file_ioerrors
    g_count_of_file_ioerrors += 1
    if g_count_of_file_ioerrors == 3:
        subprocess.Popen(reboot, shell=True)

def dec_file_ioerror():
    global g_count_of_file_ioerrors
    if g_count_of_file_ioerrors > 0:
        g_count_of_file_ioerrors -= 1

# LED を開く
led = led.LED()
led.use(0) # green
led.use(1) # red

# /boot/MEDIA/timelapse に .jpg ファイルがあって your_output.mp4 がなければ
# timelapse 動画を作成し、led で終了ブリンク
if os.path.exists('/boot/MEDIA/timelapse') and len(glob.glob('/boot/MEDIA/timelapse/*.jpg')) > 0 and not os.path.exists('/boot/MEDIA/timelapse/your_output.mp4'):
    # 連番ファイル名に変換
    command_str = "python rename2serialnumber.py"
    subprocess.check_call(command_str, shell=True)
    # timelapse 動画の作成
    command_str = "./timelapse.sh"
    p = subprocess.Popen(command_str, shell=True)
    isFinish = False
    while True:
        # Popen を polling し、継続中なら継続中ブリンクを、終了すると終了ブリンクを行う
        if not isFinish:
            if not (p.poll() is None): # None でなければ終了
                isFinish = True
            led.short(0) # green
            led.short(1) # red
        else :
            led.long(0)
else :
    while True:
        now = datetime.datetime.now() # 時刻の取得

        # 設定の取得
        ini = ConfigParser.SafeConfigParser()
        ini.read(configfile) #繰り返し毎に設定を取得
        if ini.get("main","run") == "1":
            # UVC カメラデバイスの数だけ
            for e in videodevices.videodevices_basename():
                command_str = postpic + " " + e
#               if (ini.get("camera", "camera_dev")): # 設定値が空でないなら
                try:
                    # 写真の撮影及び送信
#                   subprocess.Popen(postpic, shell=True)
                    subprocess.check_call(command_str, shell=True)
                    dec_file_ioerror()
                except IOError:
                    info=sys.exc_info()
                    msg_err_log ("IOError:"+ traceback.format_exc(info[0]))
                    msg_err_log (traceback.format_exc(info[1]))
                    msg_err_log (traceback.format_exc(info[2]))
                    inc_file_ioerror()
                except:
                    info=sys.exc_info()
                    msg_err_log ("Unexpected error:"+ traceback.format_exc(info[0]))
                    msg_err_log (traceback.format_exc(info[1]))
                    msg_err_log (traceback.format_exc(info[2]))

        # 赤LED を一回点灯
        led.short(1) # red

        #現在時刻を取得
        now_after=datetime.datetime.now()
        elapsed=(now_after - now).seconds +  float((now_after - now).microseconds)/1000000
        msg_log ("Elapsed: "+str(elapsed))
        if (elapsed < int(ini.get("main","duration"))):
            time.sleep(int(ini.get("main","duration"))-elapsed) # need to adjusting.
#       time.sleep(90) # 30 + 90 = 120



