

# Face Counter

This is a project using Pytorch InsightFace for face counting. The test passed in the Anaconda python 3.10 environment of macos and windows.

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
We use `mean absolute percentage error(MAPE)` as evaluation metrics

## Unit test

You can run unit tests with the following command:
```bash
python -m unittest test.py
```

