from main import CLASSES, CONFIDENCE_SETTING, END_POINT, MAX_DISTANCE, START_POINT, VEHICLE_CLASSES, YOLOV3_CFG, YOLOV3_HEIGHT, YOLOV3_WEIGHT, YOLOV3_WIDTH
import cv2
import numpy as np
import math

START_POINT = 80
END_POINT = 150

CLASSES = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
           "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
           "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
           "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
           "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
           "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
           "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
           "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
           "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
           "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

VEHICLE_CLASSES = [1,2,3,4,5,6,7]

YOLOV3_CFG = 'yolov3-tiny.cfg'
YOLOV3_WEIGHT = 'yolov3-tiny.weights'

CONFIDENCE_SETTING = 0.4
YOLOV3_WIDTH = 416
YOLOV3_HEIGHT = 416
MAX_DISTANCE = 80

