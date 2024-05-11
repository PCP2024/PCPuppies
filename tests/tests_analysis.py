import unittest
import sys
import cv2
import numpy as np
import PIL.Image
from PIL import Image
from analyze.analysis_fun import *

class Test_AnalysisFunctions(unittest.TestCase):
    ''' Simple functionality tests. '''

    def test_imageToNumpyArray(self):
        image = Image.open('.\demodata\example_pic.jpg')
        image_array = imageToNumpyArray(image)
        self.assertEqual(type(image_array), np.ndarray, 'Image is not a numpy array')

    def test_get_image_shape(self):
        image = Image.open('.\demodata\example_pic.jpg')
        image_array = imageToNumpyArray(image)
        shape = get_image_shape(image_array)
        self.assertEqual(shape, image.shape, 'Shape is not correct')


if __name__ == '__main__':
    unittest.main()