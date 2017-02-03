# Neural Algorithm of Artistic Style #

This repository is a course project for EL6123 Image and Video Processing by professor Yao Wang at New York University. It implements and extends "[A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576)".

Its original version can be found at [https://github.com/log0/neural-style-painting](https://github.com/log0/neural-style-painting). You can do it through the IPython Notebook available [here](./TensorFlow%20Implementation%20of%20A%20Neural%20Algorithm%20of%20Artistic%20Style.ipynb)! This code is documented so you can follow along while reading with the paper. You can also just replace with your own images and to generate your new painting.

Current version rewrites VGG-19 model from matlab-data-structure into python-data-structure so that loading the model is more easy and error-free.

Example results from original implementation:

<img src="images/Macau.jpg" width="400px" height="300px" />
<img src="images/output-macau/4900 - final.png" width="400px" height="300px" />

Using the StarryNight:

<img src="images/StarryNight.jpg" width="400px" height="300px" />

# How to run

You will need to install dependencies:

- TensorFlow
- Scipy
- Numpy

//You will need to download the [VGG-19 model](http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat).

Then just run art.py.

References:
- [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576)
- [https://github.com/jcjohnson/neural-style](https://github.com/jcjohnson/neural-style)
- [https://github.com/ckmarkoh/neuralart_tensorflow](https://github.com/ckmarkoh/neuralart_tensorflow)
- [https://github.com/log0/neural-style-painting](https://github.com/log0/neural-style-painting)
