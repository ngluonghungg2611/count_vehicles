from main import CLASSES, CONFIDENCE_SETTING, END_POINT, MAX_DISTANCE, START_POINT, YOLOV3_CFG, YOLOV3_HEIGHT, YOLOV3_WEIGHT, YOLOV3_WIDTH, check_location, check_start_line, detections_yolo3, draw_prediction
import numpy as np 
import cv2
import math
def counting_vehicle(video_input, video_output, skip_frame=1):
    colors = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    
    #Load yolo model 
    net = cv2.dnn.readNetFromDarknet(YOLOV3_CFG, YOLOV3_WEIGHT)
    
    #read first frame
    cap = cv2.VideoCapture(video_input)
    ret_val, frame = cap.read()
    width = frame[1]
    height = frame[0]
    
    #define format of output
    video_format = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_output, video_format, 25, (width, height))
    
    #define tracking object 
    list_object = []
    number_frame = 0
    number_vehicle = 0
    
    while cap.isOpened():
        number_frame += 1
        #read frame 
        ret_val, frame = cap.read()
        if frame is None:
            break
        #Tracking old object
        tmp_list_object = list_object
        list_object = []
        for object in tmp_list_object:
            tracker = object['tracker']
            class_id = object['id']
            confidence = object['confidence']
            check, box = tracker.update(frame)
            if check:
                box_x, box_y, box_width, box_height = box
                draw_prediction(CLASSES, colors, frame, class_id, confidence,
                                box_x, box_y, box_width, box_height)
                object['tracker'] = tracker
                object['box'] = box
                if check_location(box_y, box_height, height):
                    #This object passed the end line
                    number_vehicle += 1
                else:
                    list_object.append(object)
        if number_frame % skip_frame == 0:
            #Detect object and check new object
            boxes, class_ids, confidences = detections_yolo3(net, frame, CONFIDENCE_SETTING, YOLOV3_WIDTH, YOLOV3_HEIGHT,
                                                             width, height, classes=CLASSES)
            for idx, box in enumerate(boxes):
                box_x, box_y, box_width, box_height = box
                if not check_location(box_y, box_height, height):
                    #This object doesn't pass the end line
                    box_center_x = int(box_x + box_height/2.0)
                    box_center_y = int(box_y + box_height/2.0)
                    check_new_object = True
                    for tracker in list_object:
                        # Check exist object 
                        current_box_x, current_box_y, current_box_width, current_box_height = tracker['box']
                        current_box_center_x = int(current_box_x + current_box_width/2.0)
                        current_box_center_y = int(current_box_y + current_box_height/2.0)
                        # Calculate distance between 2 object:
                        distance = math.sqrt((box_center_x - current_box_center_x)**2 + 
                                             (box_center_y - current_box_center_y)**2)
                        if distance < MAX_DISTANCE:
                            # Object is existed
                            check_new_object = False
                            break
                    if check_new_object and check_start_line(box_y, box_height):
                        # Append new object to list
                        new_tracker = cv2.TrackerKCF_create()
                        new_tracker.init(frame, tuple(box))         
                        new_object = {
                            'id': class_ids[idx],
                            'tracker': new_tracker,
                            'confidence': confidences[idx],
                            'box': box                            
                        }       
                        list_object.append(new_object)
                        #Draw new object 
                        draw_prediction(CLASSES, colors, frame, new_object['id'], new_object['confidence'], box_x, box_x, box_width, box_height)
        # Put sumarytext
        cv2.putText(frame, "Number: {:3d}".format(number_vehicle), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        
        # Draw start line
        cv2.line(frame, (0, START_POINT), (width, START_POINT), (204,90,208), 1)
        
        # Draw end line
        cv2.line(frame, (0, height - END_POINT), (width, height - END_POINT), (255,0,0), 2)
        
        # Show frame
        cv2.imshow("Counting", frame) 
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    counting_vehicle('highway.mp4', 'vehicles.avi')
    
                        