from ultralytics import YOLO
import cv2
import os
model = YOLO(r'C:\Users\moham\PycharmProjects\Potholes_Detection\best2.pt')

cap=cv2.VideoCapture(r'C:\Users\moham\PycharmProjects\Potholes_Detection\mixkit-potholes-in-a-rural-road-25208-hd-ready.mp4')
while True:
    ret,frame=cap.read()
    if not ret:
        break
    results=model.track(frame,persist=True,conf=0.5)

    

    annotated_frame = results[0].plot()
    cv2.imshow("PotholesApp" ,annotated_frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
print('Done')
print("nourrr")
