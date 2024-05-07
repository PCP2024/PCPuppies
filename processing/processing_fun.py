from PIL import ImageOps
from PIL.ImageFilter import (BLUR, EDGE_ENHANCE, FIND_EDGES, SMOOTH_MORE)


def rotate(original_image, degree):
    # Rotate image by the input Degree
    return original_image.rotate(degree)

def mirror(original_image):
    # Mirror image
    return ImageOps.mirror(original_image)

def blur(original_image):
    # Make the image BLUR 
    return original_image.filter(BLUR)

def edge_enhance(original_image):
    return original_image.filter(EDGE_ENHANCE)

def find_edges(original_image):
    return original_image.filter(FIND_EDGES)

def smooth(original_image):
    return original_image.filter(SMOOTH_MORE)



