from keras import layers
from keras import models
from keras.applications.vgg19 import VGG19
import numpy as np
import os
from keras import backend as K
import tensorflow as tf

class dp_model:
    
    def __init__(self):
        PATH = os.getcwd()
        FILE_NAME = 'First-epochs_005-val_acc_0.917.hdf5'

        self.sess = tf.Session()
        self.graph = tf.get_default_graph()

        self.labels = ['animal migration', 'angel', 'ambulance', 'alarm clock', 'airplane',
                    'The Mona Lisa', 'The Great Wall of China', 'The Eiffel Tower',
                    'aircraft carrier', 'ant', 'anvil', 'apple', 'arm', 'asparagus',
                    'axe', 'backpack', 'banana', 'bandage']

        tf.python.keras.backend.set_session(self.sess)
        vg19 = VGG19(weights=None, include_top=False, input_shape=(32, 32, 3))
        self.model = models.Sequential()
        self.model.add(vg19)
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(18, activation='softmax'))
        self.model.load_weights(os.path.join(PATH, 'model', FILE_NAME))


    def predict_draw(self, image):
        with self.graph.as_default():
            tf.python.keras.backend.set_session(self.sess)
            output = self.model.predict(image)
            index = np.argmax(output, axis = 1)
        return self.labels[index[0]]
