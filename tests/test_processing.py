import unittest
import numpy as np
import image_loader
import processing_fun 

class ProcessingTestCase(unittest.TestCase):
    def setUp(self):
      self.original_image = image_loader.load_image_as_PILimage('/content/image.png')
      self.rotated = processing_fun.rotate(self.original_image, 90)
      self.mirrored = processing_fun.mirror(self.original_image)
      self.blured = processing_fun.blur(self.original_image)

    def test_rotate_image(self):
      self.assertEqual(self.rotated.size, self.original_image.size, 'The image is not rotated')

    def test_mirror_image(self):
      mirrored = np.array(self.mirrored)
      image = np.array(self.original_image)
      self.assertEqual(np.array_equal(np.flip(image, axis=1), mirrored), True, 'The image is not mirrored')
      
        
if __name__ == "__main__":
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ProcessingTestCase)
    
    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)