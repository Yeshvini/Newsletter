# Object Detection

Necessary Packages ->

opencv-python

cvlib

matplotlib

tensorflow

cvlib is a simple, high level, easy to use, open source Computer Vision library for Python.

Detecting common objects is enabled through a single function call detect_common_objects(). 
It will return the bounding box co-ordinates, corrensponding labels and confidence scores for the detected objects in the image.

Underneath it uses YOLOv3 model trained on COCO dataset capable of detecting 80 common objects in context.
