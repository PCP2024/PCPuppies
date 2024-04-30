from PIL import Image

def saveImage(image, path):
    '''
    save image to specified path
    :param image: image to save
    :param path: path to save image
    '''
    image.save(path)

def saveNumpyArrayAsImage(numpy_array, path):
    '''
    save numpy array as image to specified path
    :param numpy_array: numpy array to save
    :param path: path to save image
    '''
    image = Image.fromarray(numpy_array)
    image.save(path)

