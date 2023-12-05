import os
import argparse
from face_detection import count_faces
from sklearn.metrics import mean_absolute_percentage_error,mean_absolute_error,mean_squared_error,r2_score 
import math


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
            mae = mean_absolute_error(y_true, y_pred)
            rmse = math.sqrt(mean_squared_error(y_true, y_pred))
            r2 = r2_score(y_true, y_pred)
            print('--------------------')
            print(f'MAPE: {mape}')
            print(f'MAE: {mae}')
            print(f'RMSE: {rmse}')
            print(f'R^2: {r2}')


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
            mae = mean_absolute_error(y_true, y_pred)
            rmse = math.sqrt(mean_squared_error(y_true, y_pred))
            r2 = r2_score(y_true, y_pred)
            print('--------------------')
            print(f'MAPE: {mape}')
            print(f'MAE: {mae}')
            print(f'RMSE: {rmse}')
            print(f'R^2: {r2}')


if __name__ == '__main__':
    main()
