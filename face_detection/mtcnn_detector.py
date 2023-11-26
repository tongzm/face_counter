import sys
import os
from PIL import Image

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取InsightFace_Pytorch的目录
insightface_dir = os.path.join(current_dir, '..', 'InsightFace_Pytorch')

# 将InsightFace_Pytorch的目录添加到sys.path
sys.path.insert(0, insightface_dir)

from mtcnn import MTCNN

def count_faces(image_path):
    # 创建检测器
    detector = MTCNN()

    # 读取图片
    img = Image.open(image_path).convert('RGB')

    # 检测人脸
    face_boxes, _ = detector.detect_faces(img,min_face_size=10,
                                          thresholds=[0.1, 0.8, 0.4],
                                          nms_thresholds=[0.5, 0.1, 0.3])

    # 返回人脸数量
    return len(face_boxes)
