import unittest
import sys
import cv2
import numpy as np
import PIL.Image
from PIL import Image
from dataio.image_loader import load_image_as_PILimage
from dataio.image_loader import load_image_as_numpy_array
from dataio.image_loader import load_image_as_PILimage_from_numpy_array
from dataio.image_loader import load_image_as_numpy_array_from_PILimage

class Test_LoadFunctions(unittest.TestCase):
    """ Simple functionality tests. """

    def test_load_image_as_PILimage(self):        
        image = load_image_as_PILimage('.\demodata\example_pic.jpg')
        self.assertEqual(image.size, (690, 786), 'Image size is not correct')

    def test_load_image_as_numpy_array(self):        
        image = load_image_as_numpy_array('.\demodata\example_pic.jpg')
        self.assertEqual(image.shape, (786, 690, 3), 'Image size is not correct')
        
    def test_load_image_as_PILimage_from_numpy_array(self):
        image_array = np.array(cv2.imread('.\demodata\example_pic.jpg'))
        image = load_image_as_PILimage_from_numpy_array(image_array)
        self.assertEqual(type(image), PIL.Image.Image, 'Image is not a PIL Image')

    def test_load_image_as_numpy_array_from_PILimage(self):
        image_PIL = Image.open('.\demodata\example_pic.jpg')
        image = load_image_as_numpy_array_from_PILimage(image_PIL)
        self.assertEqual(type(image), np.ndarray, 'Image is not a numpy array')


if __name__ == '__main__':
    unittest.main()
        