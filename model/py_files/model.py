from keras import layers
from keras import models
from keras.applications.vgg19 import VGG19
import numpy as np
import os

labels = ['animal migration', 'angel', 'ambulance', 'alarm clock', 'airplane',
              'The Mona Lisa', 'The Great Wall of China', 'The Eiffel Tower',
              'aircraft carrier', 'ant', 'anvil', 'apple', 'arm', 'asparagus',
              'axe', 'backpack', 'banana', 'bandage']

PATH = os.getcwd()
FILE_NAME = 'First-epochs_005-val_acc_0.917.hdf5'

def get_model():
    vg19 = VGG19(weights='imagenet', include_top=False, input_shape=(32, 32, 3))
    model = models.Sequential()
    model.add(vg19)
    model.add(layers.Flatten())
    model.add(layers.Dense(18, activation='softmax'))
    model.load_weights(os.path.join(PATH, FILE_NAME))
    return model

def predict_draw(image, md1):
    output = mdl.predict(image)
    index = np.argmax(output, axis = 1)
    return labels[index[0]]
