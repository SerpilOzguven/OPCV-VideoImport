# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:01:10 2023

@author: Serpil ÖZGÜVEN
"""

import cv2
import time


#video ismi
video_name = "MOT17-04-DPM.mp4"

#video ice aktarma: capture, cap
cap = cv2.VideoCapture(video_name) 


print("Genislik :", cap.get(3))
print("Yükseklik:", cap.get(4))


if cap.isOpened() == False:
    print("Hata")
    
    
while True:
    ret, frame = cap.read()


    if ret == True:
        time.sleep(0.01) #Uyari: Kullanmazsak cok hizli akar.
        
        cv2.imshow("video", frame)
        
    else:break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    
cap.release() #stop capture
cv2.destroyAllWindows()    