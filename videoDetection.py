import torch
from ultralytics import YOLO
import yaml
import glob
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np

model = YOLO("runs/detect/train2/weights/200_epoch.pt")
config = {
    "path": "/drone_dataset",
    "train": "/drone_dataset/train",
    "val": "/drone_dataset/valid",
    "nc": 1,
    "names": ["drone"],
}

with open("data.yaml", "w") as file:
    yaml.dump(config, file, default_flow_style=False)

video_path = "videos/df_5.mp4"
camera = cv2.VideoCapture(video_path)
img_counter = 0

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    

    key = cv2.waitKey(1)
    
    if key % 256 == 27:
        print("Escape hit, closing...")
        break
    
    outs = model(frame)
    
    if outs:
        for result in outs:
            boxes = result.boxes 
            for box in boxes:
                conf_list=box.conf.tolist()
                conf_list=np.array(conf_list)
                max_conf=np.argmax(conf_list)
                xy = box.xyxy[max_conf].tolist()
                if conf_list[max_conf] >0.30:
                    print("Center:", [(xy[0]+xy[2])/2, (xy[1]+xy[3])/2])
                    start=(int(xy[0]),int(xy[1]))
                    end=(int(xy[2]),int(xy[3]))
                    
                    frame = cv2.rectangle(frame, start, end, (0,255,0), 2) 
                    frame = cv2.putText(frame, f'conf: {conf_list[max_conf]:.3f}', start,  cv2.FONT_HERSHEY_SIMPLEX , 0.8, (0,255,0), 2, cv2.LINE_AA) 
    cv2.imshow("Test", frame)
camera.release()
cv2.destroyAllWindows()
