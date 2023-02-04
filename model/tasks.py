from __future__ import absolute_import, unicode_literals
from .celery import app
from django.conf import settings
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import cv2
from PIL import Image
import base64
import os
from io import BytesIO


# Celery task
@app.task
def descison(image):
    image = np.array(image)
    args = {'model': 'model/garbage.model', 'labelbin': 'model/garbage_lb.pickle'}
    
    image = image.astype("float") / 255.0
    
    image = img_to_array(image)
    image = np.expand_dims(image, axis = 0)
    
    model = load_model(args["model"])
    lb = pickle.loads(open(args["labelbin"], "rb").read())
    proba = model.predict(image)[0]
    idx = np.argsort(-proba)[:3]
    label = lb.classes_[idx]

    proba = proba[idx].astype(np.float64)
    proba = np.floor(proba*1000)/10
    
    image_name_list = {'Garbage':label[0],'Accuracy':proba[0]}
    
    return image_name_list



    
