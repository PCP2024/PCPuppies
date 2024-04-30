from PIL import Image
import numpy as np

def load_image_as_PILimage(path):
    '''
    return image specified in the given path
    :param path: path to image
    :return: image
    '''
    image = Image.open(path)
    return image

def load_image_as_numpy_array(path):
    '''
    return image specified in the given path as numpy array
    :param path: path to image
    :return: numpy array
    '''
    image = Image.open(path)
    return np.array(image)

def load_image_as_PILimage_from_numpy_array(numpy_array):
    '''
    return image specified in the given numpy array
    :param numpy_array: numpy array to convert
    :return: image
    '''
    return Image.fromarray(numpy_array)

def load_image_as_numpy_array_from_PILimage(image):
    '''
    return image specified in the given image as numpy array
    :param image: image to convert
    :return: numpy array
    '''
    return np.array(image)