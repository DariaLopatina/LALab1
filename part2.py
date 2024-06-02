import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('cat.jpeg')
image = cv2.cvtColor(image, cv.COLOR_BGR2RGB)

def plot(object):
    plt.imshow(object)
    plt.axis(False)
    plt.show()

def scale(object, factor1, factor2):
    scale_object = cv2.resize(object, None, fx=factor1, fy=factor2, interpolation=cv2.INTER_LINEAR)

    return scale_object



def mirror(object, axis):
    if axis == 'x':
        mirror_object = cv2.flip(object, 0)
    elif axis == 'y':
        mirror_object = cv2.flip(object, 1)
    elif axis == 'xy':
        mirror_object = cv2.flip(object, -1)

    return mirror_object


plot(image)
result = scale(image, 2, 2)
plot(result)
result = mirror(image, 'x')
plot(result)


