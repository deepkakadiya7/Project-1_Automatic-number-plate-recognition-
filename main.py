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

# detect vehicles
       
# track vehicles
       
# detect license plates
       
# assign license plate to car
          
# crop license plate

# process license plate
                
# read license plate number
    
# write results
write_csv(results, './test.csv')
