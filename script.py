import os
import argparse
from sklearn.metrics import mean_absolute_percentage_error
from face_detection.mtcnn import count_faces

def main():
    # parse command line parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', help='输入图片的路径')
    parser.add_argument('--eval', action='store_true', help='是否输出评估指标')
    args = parser.parse_args()
    y_pred=[]
    y_true=[]

    if os.path.isdir(args.input_path):
        # If the input is a folder
        for filename in os.listdir(args.input_path):
            if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
                image_path = os.path.join(args.input_path, filename)
                num_faces = count_faces(image_path)
                y_pred.append(num_faces)
                print(f'{filename}\t{num_faces}')
                if args.eval:
                    # If you need to output evaluation indicators, 
                    # read the real number of faces from the file name
                    true_num_faces = int(filename.split('_')[0])
                    y_true.append(true_num_faces)
        if args.eval:
            mape = mean_absolute_percentage_error(y_true, y_pred)
            print('--------------------')
            print(f'MAPE: {mape}')

    else:
        # If the input is an image file
        num_faces = count_faces(args.input_path)
        y_pred = [num_faces]
        print(f'{os.path.basename(args.input_path)}\t{num_faces}')
        if args.eval:
            # If you need to output evaluation indicators, 
            # read the real number of faces from the file name
            true_num_faces = int(os.path.basename(args.input_path).split('_')[0])
            y_true = [true_num_faces]
            mape = mean_absolute_percentage_error(y_true, y_pred)
            print('----------------')
            print(f'MAPE: {mape}')


if __name__ == '__main__':
    main()
