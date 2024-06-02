import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot(object):
    plt.imshow(object)
    plt.axis(False)
    plt.show()

def scale(image, factor1, factor2):
    scale_object = cv2.resize(image, None, fx=factor1, fy=factor2, interpolation=cv2.INTER_LINEAR)
    return scale_object



def mirror(object, axis):
    if axis == 'x':
        mirror_object = cv2.flip(object, 0)
    elif axis == 'y':
        mirror_object = cv2.flip(object, 1)
    elif axis == 'xy':
        mirror_object = cv2.flip(object, -1)
    return mirror_object