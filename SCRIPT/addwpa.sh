#!/bin/sh -eu 
# http://qiita.com/youcune/items/fcfb4ad3d7c1edf9dc96
#trap 'echo NG' ERR

addwpafile=/boot/addwpa.txt #wpa追加定義ファイル
wpaconf=/etc/wpa_supplicant/wpa_supplicant.conf
if [ -e $addwpafile ]; then #wpa追加定義ファイルがあれば
  nkf -Lu --overwrite $addwpafile #改行コードを LF にする
  echo hello
  ssid=`head -n 1 $addwpafile`
  psk=`head -n 2 $addwpafile | tail -n 1`
  echo $ssid
  echo $psk
  if [ -n "$ssid" -a -n "$psk" ]; then #両方とも長さが0でなければ
    # wpa_supplicant.conf の末尾に network 定義を追加
    nn=`wpa_cli add_network | tail -n 1` # 追加した network number
    wpa_cli set_network $nn ssid \"$ssid\"
    wpa_cli set_network $nn psk \"$psk\"
    wpa_cli enable_network $nn
    wpa_cli save_config
    # wpa追加定義ファイル の削除
    rm $addwpafile
    # reboot
  fi
fi
