from A_set_class import CONFIDENCE_SETTING, VEHICLE_CLASSES
import numpy as np  
import cv2
def get_output_layer(net):
    """
    get output layer
        :param net: Model
        :return: ouput layer
    """    
    try:
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
        return output_layers
    except:
        print("Can't get output layers")
        return None

def detections_yolov3(net, image, confifedence_setting, yolo_w, yolo_h, frame_w, frame_h, classes = None):
    """
    Detect object usr yolov3 model
        intput
            :param net: Model
            :param image: iamge
            :param confidence_setting: confidence setting
            :param yolo_w: dimension of yolo input
            :param yolo_h: dimension of yolo inpput
            :param yolo_w: actual dimension of frame
            :param yolo_h: actual dimension of frame
            :param classes: name of object
        return: 
    """
    img = cv2.resize(image, (yolo_w, yolo_h))
    blob = cv2.dnn.blobFromImage(img, 0.00392, (yolo_w, yolo_h), swapRB = True, crop = False)
    net.setInput(blob)
    layer_output = net.forward(get_output_layer(net))
    
    boxes = []
    class_ids = []
    confidences = []
    for out in layer_output:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > CONFIDENCE_SETTING and class_id in VEHICLE_CLASSES:
                print("object name: " + classes[class_id] + " - confidence: {:0.2f}".format(confidence*100))
                center_x = int(detection[0] * frame_w)
                center_y = int(detection[1] * frame_h)
                w = int(detection[3] * frame_w)
                h = int(detection[4] * frame_h)
                x = center_x - w/2
                y = center_y - h/2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x,y,w,h])
    return boxes, class_ids, confidences


        