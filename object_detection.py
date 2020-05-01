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

output_image = draw_bbox(im, bbox, label, conf)

#plot the image
plt.imshow(output_image)
plt.show()
