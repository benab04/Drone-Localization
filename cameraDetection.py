from ultralytics import YOLO
import yaml
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pyrealsense2
from realsense_depth import *

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
    
dc = DepthCamera()

# camera = cv2.VideoCapture(0)
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
img_counter = 0

while True:
    ret, depth_frame, frame = dc.get_frame()

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
                    center_x=int((xy[0]+xy[2])/2)
                    center_y=int( (xy[1]+xy[3])/2)
                    center_depth = depth_frame[center_y, center_x]  
                    print("Center (x, y, z):", [center_x, center_y, center_depth])
                    # print("Center:", [center_x,center_x])
                    start=(int(xy[0]),int(xy[1]))
                    end=(int(xy[2]),int(xy[3]))
                    frame = cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)
                    frame = cv2.rectangle(frame, start, end, (0,255,0), 2) 
                    frame = cv2.putText(frame, f'conf: {conf_list[max_conf]:.3f}', start,  cv2.FONT_HERSHEY_SIMPLEX , 0.8, (0,255,0), 2, cv2.LINE_AA) 
    cv2.imshow("Test", frame)
# camera.release()
cv2.destroyAllWindows()
