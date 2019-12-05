#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:18:19 2019

@author: comp1
"""
import sys
import cv2

tracker = cv2.TrackerGOTURN_create()

vid = cv2.VideoCapture(0)

if not vid.isOpened():
    print("[INFO] Could not open feed.")
    sys.exit()
    
ok, frame = vid.read()
if not ok:
    print("[INFO] Cannot read video file")
    sys.exit()
    
#bbox = (276, 23, 86, 320)

bbox = cv2.selectROI(frame, False)

ok = tracker.init(frame, bbox)

while True:
    ok, frame = vid.read()
    if not ok:
        print("[INFO] Cannot read video file")
        sys.exit()
    
    timer = cv2.getTickCount()
    
    ok, bbox = tracker.update(frame)
    
    fps = cv2.getTickFrequency()/cv2.getTickCount()
    
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 255, 0), 2, 1)
        
    else:
        cv2.putText(fraem, "Tracking failed", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
        
    cv2.putText(frame, "FPS: " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    
    cv2.imshow("GOTURN Tracking", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
vid.release()