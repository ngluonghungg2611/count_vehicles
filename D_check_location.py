from A_set_class import END_POINT
def check_location(box_y, box_height, height):
    """
    Check center point of object that passing end line or not 
    :param box_y: y value of bbox
    :param box_height: height value of bbox
    :param height: heoght of image
    :return Boolen
    """
    center_y = int ( box_y + box_height/2.0)
    if center_y > height - END_POINT:
        return True
    else:
        return False
    
    