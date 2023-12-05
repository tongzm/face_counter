

# Face Counter

This is a project using  Multi-task Cascaded Convolutional Networks (MTCNN) for face counting. The test passed in the Anaconda python 3.10 environment of macos and windows.

## MTCNN

PNet, RNet, and ONet are key components of the Multi-task Cascaded Convolutional Networks (MTCNN), playing a crucial role in face detection and alignment.

1. **PNet (Proposal Network)**: PNet is the first stage of MTCNN. It is a fully convolutional network used for obtaining candidate windows and bounding box regression vectors. It generates candidate windows by sliding a small window across the input image.
2. **RNet (Refine Network)**: RNet is the second stage of MTCNN. It takes the output of PNet (candidate windows) as input and further eliminates false windows while performing a more precise bounding box regression on the remaining windows.
3. **ONet (Output Network)**: ONet is the third stage of MTCNN. It not only performs tasks similar to RNet (i.e., further eliminating false windows and performing more precise bounding box regression), but also predicts facial landmarks for the detected faces.

In our project , these networks are used for detecting faces in images. Firstly, PNet generates candidate windows in the image, then RNet further refines these windows, and finally, ONet determines the final face detection results and predicts facial landmarks. This process effectively detects all faces in the image, thereby achieving the goal of face counting.

## Install

First, install the Anaconda python 3.10 environment: slightly


Then, you need to clone this repository:

```bash
git clone https://github.com/tongzm/face_counter_private.git
```

Finally, you need to install the project's dependencies:

```bash
pip install -r requirements.txt
```


## How to use
You can use this program with the following command:
```bash
python script.py /path/to/your/image.jpg
```

You need to replace `/path/to/your/image.jpg` with the actual path to your image file. You can also pass the path to a folder as an argument, and the program will process all .jpg and .png images in the folder:

```bash
python script.py /path/to/your/images/
```

## Evaluation method

If you want to output evaluation metrics, please add the actual number of faces and "_" as the delimiter at the beginning of the image file name, such as: "7_image.jpg", and then add the --eval parameter.
```bash
python script.py /path/to/your/7_image.jpg --eval
```

You need to replace `/path/to/your/7_image.jpg` with the actual path to your image file

## Evaluation metrics
We use [mean absolute percentage error(MAPE)](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error), [Mean absolute error(MAE)](https://en.wikipedia.org/wiki/Mean_absolute_error), [root-mean-square-error-rmse(RMSE)](https://c3.ai/glossary/data-science/root-mean-square-error-rmse/), [R2 Score](https://thecleverprogrammer.com/2021/06/22/r2-score-in-machine-learning/) as evaluation metrics

## Unit test

You can run unit tests with the following command:
```bash
python -m unittest test.py
```

