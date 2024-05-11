from PIL import ImageOps
from PIL.ImageFilter import (BLUR, EDGE_ENHANCE, FIND_EDGES, SMOOTH_MORE)

# Rotate image by the input Degree
def rotate(original_image, degree):
    return original_image.rotate(degree)

# Mirror image
def mirror(original_image):
    return ImageOps.mirror(original_image)

# Make the image BLUR 
def blur(original_image):
    return original_image.filter(BLUR)

# Enhances edges
def edge_enhance(original_image):
    return original_image.filter(EDGE_ENHANCE)

# Finds edges
def find_edges(original_image):
    return original_image.filter(FIND_EDGES)

# Makes image smooth
def smooth(original_image):
    return original_image.filter(SMOOTH_MORE)

# Inverts image
def invert(original_image):
    return ImageOps.invert(original_image.convert('RGB'))

# Applies threshold to image
def apply_threshold(original_image, threshold):
    return ImageOps.autocontrast(original_image.convert('RGB'), cutoff=threshold)

