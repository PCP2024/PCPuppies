import unittest
import sys
from dataio.image_loader import load_image_as_PILimage

class Test_LoadFunctions(unittest.TestCase):
    """ Simple functionality tests. """

    def test_load_image_as_PILimage(self):        
        image = load_image_as_PILimage('./demodata/johann.jpg')
        self.assertEqual(image.size, (3840, 2160), 'Image size is not correct')
        

if __name__ == '__main__':
    unittest.main()
        