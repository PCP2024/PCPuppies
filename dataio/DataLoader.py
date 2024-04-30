from PIL import Image

def imageLoader(path):
    '''
    return image specified in the given path
    :param path: path to image
    :return: image
    '''
    image = Image.open(path)
    return image

im = imageLoader(r'C:\Users\bonni\Bonnie\Studium\Master\Master - Computational Neuroscience\PCP\johann.jpg')
im.show()
print('size:' + str(im.size) + ', type: ' + str(type(im))+ ', format: ' + str(im.mode))