import unittest
from dataio.image_loader import load_image_as_PILimage
from processing.processing_fun import rotate


class ProcessingTestCase(unittest.TestCase):
    def setUp(self):
        self.original_image = load_image_as_PILimage('.\demodata\example_pic.jpg')
        self.rotated = rotate(self.original_image, 90)
    def test_rotate_image(self):
        self.assertEqual(self.rotated.size, self.original_image.size, 'The image is not rotated')   
        
if __name__ == '__main__':
    unittest.main()   