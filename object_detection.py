# -*- coding: utf-8 -*-
"""
@author: yeshvini
"""

#import necessary packages
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

# read image
im = cv2.imread('img.jpg')

# returns bounding box with confidence scores for detected image
bbox, label, conf = cv.detect_common_objects(im)

# draw bounding box over detected objects
output_image = draw_bbox(im, bbox, label, conf)

# display output
# press any key to close window  
cv2.imshow("object_detection", output_image)
cv2.waitKey()

# save output
cv2.imwrite("object_detection.jpg", output_image)

# release resources
cv2.destroyAllWindows()
