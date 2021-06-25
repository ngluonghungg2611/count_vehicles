

import cv2


def darw_porediction(classes, colors, img, class_id, confidence, x, y, width, height):
    """
    Draw bbox and put classes text and confidence
    :param classes: name of objecct
    :param colors: color for object
    :param img: image
    :param class_id: class_id of this object
    :param confidence: confidence
    :param x: top, left
    :param y: top, left
    :param width: width of bbox
    :param height: height of bbox
    :return: None
    """
    try:
        label = str(classes[class_id])
        color = colors[class_id]
        center_x = int(x + width/2.0)
        center_y = int(y + height/2.0)
        x = int(x)
        y = int(y)
        width = int(width)
        height = int(height)
        
        cv2.rectangle(img, (x,y), (x + width, y + height), color, 1) 
        cv2.circle(img, (center_x, center_y), 2, (0,255,0), -1)
        cv2.putText(img, label + ": {:0.2f}%".format(confidence * 100), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    except(Exception, cv2.error) as e:
        print("Con;t draw prediction for class_id {}: {}".format(class_id, e))
             