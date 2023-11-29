import sys
import os
import unittest
from PIL import Image
from face_detection.mtcnn import count_faces

class TestFaceDetection(unittest.TestCase):
    def test_detect_faces(self):
        # Test case 1: image with 4 faces
        image_path = 'images/4_faces_2.jpg' 
        num_faces = count_faces(image_path)
        # Read the real number of faces from the file name
        filename = os.path.basename(image_path)
        true_num_faces = int(filename.split('_')[0])
        self.assertEqual(num_faces, true_num_faces)

        # Test case 2: image with 16 faces
        image_path = 'images/16_faces_1.jpeg'  
        num_faces = count_faces(image_path)
        # Read the real number of faces from the file name
        filename = os.path.basename(image_path)
        true_num_faces = int(filename.split('_')[0])
        self.assertEqual(num_faces, true_num_faces)

if __name__ == '__main__':
    unittest.main()
