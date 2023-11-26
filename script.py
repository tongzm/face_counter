import os
import sys
import argparse
from face_detection.mtcnn_detector import count_faces

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='输入图片的路径')
    parser.add_argument('--eval', action='store_true', help='是否输出评估指标')
    args = parser.parse_args()
    total_num_faces=0
    total_true_num_faces=0

    if os.path.isdir(args.input_path):
        # 如果输入是一个文件夹
        for filename in os.listdir(args.input_path):
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                image_path = os.path.join(args.input_path, filename)
                num_faces = count_faces(image_path)
                total_num_faces+=num_faces
                print(f'{filename}\t{num_faces}')
                if args.eval:
                    # 如果需要输出评估指标，从文件名中读取真实的人脸数量
                    true_num_faces = int(filename.split('_')[0])
                    total_true_num_faces+=true_num_faces
        if args.eval:
            accuracy = total_num_faces / total_true_num_faces
            print(f'total detected num faces: {total_num_faces}')
            print(f'total true num faces: {total_true_num_faces}')
            print(f'total Accuracy: #detected_faces/#true_faces = {accuracy}')
    else:
        # 如果输入是一个图片文件
        num_faces = count_faces(args.input_path)
        print(f'{os.path.basename(args.input_path)}\t{num_faces}')
        if args.eval:
            # 如果需要输出评估指标，从文件名中读取真实的人脸数量
            true_num_faces = int(os.path.basename(args.input_path).split('_')[0])
            accuracy = num_faces / true_num_faces
            print(f'detected num faces: {num_faces}')
            print(f'true num faces: {true_num_faces}')
            print(f'Accuracy: #detected_faces/#true_faces = {accuracy}')

if __name__ == '__main__':
    main()
