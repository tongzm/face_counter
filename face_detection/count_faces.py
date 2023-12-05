from .mtcnn import MTCNN
from PIL import Image


def count_faces(image_path):
    """
    Arguments
    image_path: The path to the image file

    Return:
    The number of faces detected in the image
    """

    # create detector
    detector = MTCNN()

    # read images
    img = Image.open(image_path).convert('RGB')

    # dectec faces
    face_boxes, _ = detector.detect_faces(img,
                                          min_face_size=10.0,
                                          thresholds=[0.1, 0.8, 0.4],
                                          nms_thresholds=[0.5, 0.1, 0.3])

    # return num of face
    return len(face_boxes)
    
