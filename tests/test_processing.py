import unittest
import numpy as np
from dataio import image_loader
from processing import processing_fun 

class ProcessingTestCase(unittest.TestCase):
    def setUp(self):
      self.original_image = image_loader.load_image_as_PILimage('.\demodata\example_pic.jpg')
      self.rotated = processing_fun.rotate(self.original_image, 90)
      self.mirrored = processing_fun.mirror(self.original_image)
      self.blurred = processing_fun.blur(self.original_image)
      self.edge_enhance = processing_fun.edge_enhance(self.original_image)
      self.edges = processing_fun.find_edges(self.original_image)
      self.invert = processing_fun.invert(self.original_image)
      self.threshold = processing_fun.apply_threshold(self.original_image, 100)
      
    #If rotating by 360°, we should have the same image.
    def test_rotate_image(self):
      self.assertTrue(np.array_equal(np.array(self.original_image), np.array(self.rotated)), 'The image is not rotated')

    #The flipped version of the image should lead to the same mirrored image.
    def test_mirror_image(self):
      mirrored = np.array(self.mirrored)
      image = np.array(self.original_image)
      self.assertTrue(np.array_equal(np.flip(image, axis=1), mirrored), 'The image is not mirrored')
    
    #Blurred image should have less variance than the original one.
    def test_blurred(self):
      self.assertTrue(np.var(self.blurred) < np.var(self.original_image), "The image is not blurred")
    
    #The enhanced image should be brighter due to the edge enhancement process
    def test_edge_enhance(self):
      def get_brightness(image):
        image = image.convert('L')
        total_brightness = sum(image.getdata())
        num_pixels = image.width * image.height
        return total_brightness / num_pixels
      self.assertTrue(get_brightness(self.edge_enhance) > get_brightness(self.original_image), "The image's edges are not enhanced")
  
    #The new image should be darker because only edges remain bright
    def test_edges(self):
      def get_brightness(image):
        image = image.convert('L')
        total_brightness = sum(image.getdata())
        num_pixels = image.width * image.height
        return total_brightness / num_pixels
      self.assertTrue(get_brightness(self.edges) < get_brightness(self.original_image), "The image's edges were not properly identified")
    
    #Check every pixel of both images, if any of the pair of pixels are equal, image is not properly inverted.
    def test_invert(self):
      correct_inversion = True
      for y in range(self.original_image.height):
        for x in range(self.original_image.width):
            original_pixel = self.original_image.getpixel((x, y))
            inverted_pixel = self.invert.getpixel((x, y))
            if original_pixel == inverted_pixel:
                correct_inversion = False
      self.assertTrue(correct_inversion, 'The image is not inverted')

    #The sum of all the pixels in the original image should be higher than the one of the modifier image.
    def test_apply_threshold(self):
      self.assertTrue(np.sum(self.original_image) > np.sum(self.threshold), 'The image was not modified according to the threshold')

if __name__ == '__main__':
    unittest.main()   