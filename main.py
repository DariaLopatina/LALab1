import numpy as np
import matplotlib.pyplot as plt

vector = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
#vector = np.array([[0, 0], [4, 5]])
#print(vector)
# m = np.array([[3, 0], [0, 3]]) збільшення
# m = np.array([[-1, 0], [0, -1]]) відзеркалення по х = у
#m = np.array([[-1, 0], [0, 1]]) відзеркалення по у

def rotate(object, angle):
    radians = np.radians(angle)
    rotate_matrix = np.array([[np.cos(radians), -np.sin(radians)],
                                [np.sin(radians), np.cos(radians)]])
    return object @ rotate_matrix.T


def scale(object, factor):
    scale_matrix = np.array([[factor, 0], [0, factor]])
    return object @ scale_matrix.T


def mirror(object, axis):
    if axis == 'x':
        mirror_matrix = np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        mirror_matrix = np.array([[-1, 0], [0, 1]])
    return object @ mirror_matrix.T
bc vbfv



def universal (object, matrix):
    return object @ matrix



m = np.array([[-1, 0], [0, 1]])
vector = vector @ m
plt.plot(vector[:, 0], vector[:, 1])

plt.show()