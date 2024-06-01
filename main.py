import numpy as np
import matplotlib.pyplot as plt

vector = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
#vector = np.array([[0, 0], [4, 5]])
#print(vector)
# m = np.array([[3, 0], [0, 3]]) збільшення
# m = np.array([[-1, 0], [0, -1]]) відзеркалення по х = у
#m = np.array([[-1, 0], [0, 1]]) відзеркалення по у

def plot(object, title):
    plt.plot(object[:, 0], object[:, 1], marker='o')
    plt.title(title)
    plt.grid(True)
    plt.show()

def rotate(object, angle):
    radians = np.radians(angle)
    rotate_matrix = np.array([[np.cos(radians), -np.sin(radians)],
                              [np.sin(radians), np.cos(radians)]])
    title = f"rotation {angle}"
    return object @ rotate_matrix.T, title

def scale(object, factor):
    scale_matrix = np.array([[factor, 0], [0, factor]])
    title = f"scale {factor}"
    return object @ scale_matrix.T, title

def mirror(object, axis):
    if axis == 'x':
        mirror_matrix = np.array([[1, 0], [0, -1]])
    else:
        mirror_matrix = np.array([[-1, 0], [0, 1]])

    title = f"mirror {axis}"
    return object @ mirror_matrix.T, title

def tilt(object, axis, factor):
    if axis == 'x':
        tilt_matrix = np.array([[1, factor], [0, 1]])
    else:
        tilt_matrix = np.array([[1, 0], [factor, 1]])

    title = f"tilt {axis, factor}"
    return object @ tilt_matrix.T, title

def universal (object, matrix):
    title = f"universal change {matrix}"
    return object @ matrix, title

def object_manipulation(object):
    title = "vector"
    plot(object, title)

    result, title = rotate(object, 90)
    plot(result, title)

    result, title = scale(object, 2)
    plot(result, title)

    result, title = mirror(object, 'x')
    plot(result, title)

    result, title = tilt(object, 'x', 3)
    plot(result, title)

    matrix = np.array([[1, 2], [3, 4]])
    result, title = universal(object, matrix)
    plot(result, title)





object_manipulation(vector)




#def ThreeD_manipulation():







#m = np.array([[-1, 0], [0, 1]])
#vector = vector @ m
#plt.plot(vector[:, 0], vector[:, 1])
#plt.show()