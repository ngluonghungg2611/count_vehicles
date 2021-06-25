from A_set_class import START_POINT
def check_start_line(box_y, box_height):
    """
    Check center oint of object that passing start line or not
    :param box_y: y value of bbox
    :param box_height: height value of bbox
    :return: Boolen 
    """
    center_y = int(box_y + box_height/2.0)
    if center_y > START_POINT:
        return True
    else: 
        False