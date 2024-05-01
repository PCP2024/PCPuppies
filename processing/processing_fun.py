from PIL import ImageOps, ImageFilter

def rotate(original_image, degree):
    # Rotate image by the input Degree
    return original_image.rotate(degree)

def mirror(original_image):
    # Mirror image
    return ImageOps.mirror(original_image)