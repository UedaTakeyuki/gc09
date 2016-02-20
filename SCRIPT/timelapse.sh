# http://qiita.com/riocampos/items/2f4fe927b5cf99aff767
# coding:utf-8 Copy Right Atelier UEDA🐸 © 2016 -
ffmpeg -f image2 -r 30 -i /boot/MEDIA/timelapse/image%06d.jpg -r 30 -an -vcodec mpeg4 -pix_fmt yuv420p /boot/MEDIA/timelapse/your_output.mp4
