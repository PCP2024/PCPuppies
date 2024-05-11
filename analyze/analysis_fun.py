import numpy as np

def imageToNumpyArray(image):
    '''
    convert image to numpy array
    :param image: image to convert
    :return: numpy array
    '''
    return np.array(image)

def get_image_shape(image):
    '''
    get the shape of the image
    :param image: image to get the shape of, as numpy array
    :return: shape of the image
    '''
    return image.shape

