import unittest
import numpy as np
from dataio import image_loader
from processing import processing_fun 

class ProcessingTestCase(unittest.TestCase):
    def setUp(self):
      self.original_image = image_loader.load_image_as_PILimage('.\demodata\example_pic.jpg')
      self.rotated = processing_fun.rotate(self.original_image, 90)
      self.mirrored = processing_fun.mirror(self.original_image)
      self.blured = processing_fun.blur(self.original_image)
      self.edge_enhance = processing_fun.edge_enhance(self.original_image)
      self.edges = processing_fun.find_edges(self.original_image)
      

    def test_rotate_image(self):
      self.assertEqual(self.rotated.size, self.original_image.size, 'The image is not rotated')

    def test_mirror_image(self):
      mirrored = np.array(self.mirrored)
      image = np.array(self.original_image)
      self.assertEqual(np.array_equal(np.flip(image, axis=1), mirrored), True, 'The image is not mirrored')
      
    def test_edge_enhance(self):
      self.assertEqual(self.edge_enhance.size, self.original_image.size, "The image size has changed after applying edge enhance filter")
    
       
  
if __name__ == '__main__':
    unittest.main()   

'''      
if __name__ == "__main__":
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ProcessingTestCase)
    
    # Run the test suite
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    '''