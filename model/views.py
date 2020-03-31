from django.shortcuts import render
from django.http import HttpResponse
import cv2
import json
import numpy as np
from .apps import ModelConfig
from .static.model.py_files import extract_image as ex

cnvs = np.full((500, 1200, 3), 255, np.uint8)

def writeImage(strokes):
    for item in strokes:
        cv2.circle(cnvs, (item['x'], item['y']), 5, (0, 0, 0), -1)

    return cnvs

def predImg(request):
    if request.method == 'GET':
        stroke = json.loads(request.headers['stroke'])
        img = writeImage(stroke)
        img = ex.get_crop(img)
        img = ex.resize_image(img)
        prediction = ModelConfig.model_obj.predict_draw(img)
        return HttpResponse(prediction, content_type='text/html')

def resetImg():
    global cnvs
    cnvs = np.full((500, 1200, 3), 255, np.uint8)