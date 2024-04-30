from PIL import Image

def imageLoader(path):
    '''
    return image specified in the given path
    :param path: path to image
    :return: image
    '''
    image = Image.open(path)
    return image
