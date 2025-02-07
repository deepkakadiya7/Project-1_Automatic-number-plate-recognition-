from ultralytics import YOLO
import cv2

import util
from sort.sort import *
from util import get_car, read_license_plate, write_csv

# load models
coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('license_plate_detector.pt')

# load video
cap = cv2.VideoCapture("E:\project\one again\dataset\sample.mp4")
vehicles = [2, 3, 5, 7]



#read Frames

frame_nmr = -1
ret = True
while ret:
    frame_nmr += 1
    ret, frame = cap.read()
    if ret:
        results[frame_nmr] = {}


# detect vehicles
        detections = coco_model(frame)[0]
        detections_ = []
        for detection in detections.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in vehicles:
                detections_.append([x1, y1, x2, y2, score])
# track vehicles
       track_ids = mot_tracker.update(np.asarray(detections_))
# detect license plates
       
# assign license plate to car
          
# crop license plate

# process license plate
                
# read license plate number
    
# write results
write_csv(results, './test.csv')
