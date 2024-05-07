import unittest
import sys
import cv2
import numpy as np
import PIL.Image
from PIL import Image
from dataio.save_Image import saveImage
from dataio.save_Image import saveNumpyArrayAsImage

class Test_SaveFunctions(unittest.TestCase):
    """ Simple functionality tests. """

    def test_saveImage(self):        
        saveImage('.\demodata\example_pic.jpg')
        self.assertIn(image.size, (690, 786), 'Image size is not correct')

    def test_saveNumpyArrayAsImage(self):        
        saveNumpyArrayAsImage('.\demodata\example_pic.jpg')
        self.assertIn(image.shape, (786, 690, 3), 'Image size is not correct')
        
if __name__ == '__main__':
    unittest.main()
        