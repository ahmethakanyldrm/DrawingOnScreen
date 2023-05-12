# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:57:02 2023

@author: Lenovo
"""
# Kütüphaneler

import cv2
import numpy as np
from collections import deque

cap = cv2.VideoCapture(0)

# morfolojik işlemler için oluşturduk
kernel = ((5, 5), np.uint8)

lower_blue = np.array([100, 60, 60])
upper_blue = np.array([140, 255, 255])

blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_index = 0

paintWindow = np.zeros((471, 636, 3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(paintWindow, "CLEAR", (49, 33),
            font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), font,
            0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), font,
            0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), font,
            0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), font,
            0.5, (255, 255, 255), 2, cv2.LINE_AA)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Paint Window", paintWindow)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
