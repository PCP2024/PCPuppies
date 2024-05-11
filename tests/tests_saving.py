import unittest
import numpy as np
import os
from PIL import Image
from dataio.saving_fun import saveImage
from dataio.saving_fun import saveNumpyArrayAsImage

class Test_SaveFunctions(unittest.TestCase):
    """ Simple functionality tests. """

    def test_saveImage(self):        
        saveImage('example_pic.jpg', '.\saved_pics')
        self.assertTrue(os.path.exists('.\saved_pics\example_pic.jpg'), 'Image could not be saved')

    def test_saveNumpyArrayAsImage(self):     
        image_array = np.array(np.random.random(690, 786))
        saveNumpyArrayAsImage(image_array, '.\saved_pics\random_pixels.jpg')
        self.assertTrue(os.path.exists('.\saved_pics\random_pixels.jpg'), 'Numpy Array could not be saved as Image')
        
if __name__ == '__main__':
    unittest.main()
        