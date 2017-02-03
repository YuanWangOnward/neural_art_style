# This script transfer .mat VGG model to pickle .pkl file
import scipy.io
import scipy.misc
import numpy as np
import pickle


def mat2pkl(vgg_path='imagenet-vgg-verydeep-19.mat'):
    """
    used to transfer .mat vgg modle to .p
    for clear code and avoid potential error
    """
    # read in .mat vgg model
    vgg = scipy.io.loadmat(vgg_path)
    vgg_layers = vgg['layers']
    vgg_meta = vgg['meta']

    # copy meta data
    meta = {}
    meta['inputs'] = {}
    meta['classes'] = {}
    meta['normalization'] = {}
    meta['inputs']['name'] = 'data'
    meta['inputs']['size'] = [224, 224, 3, 10]
    temp = vgg_meta[0][0][1][0][0][0]
    meta['classes']['name'] = [str(temp[0][n][0]) for n in range(1000)]
    temp = vgg_meta[0][0][1][0][0][1]
    meta['classes']['description'] = [str(temp[0][n][0]) for n in range(1000)]
    meta['normalization']['imageSize'] = [224, 224, 3, 10]
    meta['normalization']['keepAspect'] = 1
    meta['normalization']['averageImage'] = [123.6800, 116.7790, 103.9390]
    meta['normalization']['border'] = [32, 32]
    meta['normalization']['cropSize'] = [0.8750, 0.8750]
    meta['normalization']['interpolation'] = 'bilinear'

    # copy layers data
    layers = []
    for layer_index in range(43):
        vgg_layer = vgg_layers[0][layer_index]
        layer_type = vgg_layer[0][0][1][0]
        layer_type
        # for conv layer
        layer = {}
        if layer_type == 'conv':
            layer['name'] = vgg_layer[0][0][0][0]
            layer['type'] = vgg_layer[0][0][1][0]
            layer['weights'] = {}
            layer['weights']['W'] = vgg_layer[0][0][2][0][0]
            layer['weights']['b'] = vgg_layer[0][0][2][0][1]
            layer['size'] = vgg_layer[0][0][3][0]
            layer['pad'] = vgg_layer[0][0][4][0]
            layer['stride'] = vgg_layer[0][0][5][0]
            layer['precious'] = vgg_layer[0][0][6][0]
            layer['dilate'] = vgg_layer[0][0][7][0]
            layer['opts'] = {}
            layers.append(layer)
        elif layer_type == 'relu':
            layer['name'] = vgg_layer[0][0][0][0]
            layer['type'] = vgg_layer[0][0][1][0]
            layer['leak'] = vgg_layer[0][0][2][0]
            layer['weights'] = {}
            layer['precious'] = vgg_layer[0][0][4][0]
            layers.append(layer)
        elif layer_type == 'pool':
            layer['name'] = vgg_layer[0][0][0][0]
            layer['type'] = vgg_layer[0][0][1][0]
            layer['method'] = vgg_layer[0][0][2][0]
            layer['pool'] = vgg_layer[0][0][3][0]
            layer['stride'] = vgg_layer[0][0][4][0]
            layer['pad'] = vgg_layer[0][0][5][0]
            layer['weights'] = {}
            layer['precious'] = vgg_layer[0][0][7][0]
            layer['opts'] = {}
            layers.append(layer)
        elif layer_type == 'softmax':
            layer['name'] = vgg_layer[0][0][0][0]
            layer['type'] = vgg_layer[0][0][1][0]
            layer['weights'] = {}
            layer['precious'] = vgg_layer[0][0][3][0]
            layers.append(layer)
        else:
            raise ValueError('Unknown layer type')

    vgg = {'meta': meta, 'layers': layers}
    pickle.dump(vgg, open("imagenet-vgg-verydeep-19.pkl", "wb"))
