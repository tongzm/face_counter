import sys
import os
import unittest
from PIL import Image
from mtcnn.mtcnn import count_faces

class TestFaceDetection(unittest.TestCase):
    def test_detect_faces(self):
        # 测试用例1：有4个人脸的图片
        image_path = 'images/4_faces_2.jpg' 
        num_faces = count_faces(image_path)
        # 从文件名中读取真实的人脸数量
        filename = os.path.basename(image_path)
        true_num_faces = int(filename.split('_')[0])
        self.assertEqual(num_faces, true_num_faces)

        # 测试用例2：有16人脸的图片
        image_path = 'images/16_faces_1.jpeg'  
        num_faces = count_faces(image_path)
        # 从文件名中读取真实的人脸数量
        filename = os.path.basename(image_path)
        true_num_faces = int(filename.split('_')[0])
        self.assertEqual(num_faces, true_num_faces)

if __name__ == '__main__':
    unittest.main()
