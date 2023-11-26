

# Face Counter

这是一个使用MTCNN进行人脸检测的项目。在macos,windows的adaconda python 3.10环境下测试通过。

## 安装

首先, 安装adaconda python 3.10环境: 略



然后，你需要克隆这个仓库：

```bash
git clone https://github.com/yourusername/face_counter.git
```

最后，你需要安装项目的依赖：

```bash
pip install -r requirements.txt
```

你可以通过以下命令来使用这个程序：

## 使用
你可以通过以下命令来使用这个程序：
```bash
python script.py /path/to/your/image.jpg
```

你需要将`/path/to/your/image.jpg`替换为你的图片文件的实际路径。你也可以将一个文件夹的路径作为参数，这个程序会处理文件夹中的所有.jpg和.png图片：

```bash
python script.py /path/to/your/images/
```

## 评估方法

如果你想输出评估指标，请在图片文件名的开头加入实际人脸数量和"_"作为分隔符如:"7_image.jpg", 然后添加 --eval参数
```bash
python script.py /path/to/your/7_image.jpg --eval
```

你需要将`/path/to/your/7_image.jpg`替换为你的图片文件的实际路径

## 评估指标
我们设计的评估指标准确率（Accuracy）的定义为：探测到的人脸总数与实际人脸总数的比值。
```bash
Accuracy=探测到的人脸总数/实际人脸总数
```

## 单元测试

你可以通过以下命令来运行单元测试：
```bash
python -m unittest test.py
```

