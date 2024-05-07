import unittest
import sys
import cv2
import numpy as np
import PIL.Image
from PIL import Image
from dataio.save_Image import saveImage
from dataio.save_Image import saveNumpyArrayAsImage

class Test_LoadFunctions(unittest.TestCase):
    """ Simple functionality tests. """

    def test_saveImage(self):        
        image = load_image_as_PILimage('.\demodata\example_pic.jpg')
        self.assertEqual(image.size, (690, 786), 'Image size is not correct')

    def test_saveNumpyArrayAsImage(self):        
        image = load_image_as_numpy_array('.\demodata\example_pic.jpg')
        self.assertEqual(image.shape, (786, 690, 3), 'Image size is not correct')
        
    

if __name__ == '__main__':
    unittest.main()
        