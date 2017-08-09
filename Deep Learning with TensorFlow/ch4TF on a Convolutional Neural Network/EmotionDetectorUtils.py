import pandas as pd
import numpy as np
import os, sys, inspect
from six.moves import cPickle as pickle
import scipy.misc as misc


IMAGE_SIZE = 48
NUM_LABELS = 7
VALIDATION_PERCENT = 0.1  # use 10 percent of training images for validation

IMAGE_LOCATION_NORM = IMAGE_SIZE / 2

np.random.seed(0)

emotion = {0:'anger', 1:'disgust',\
           2:'fear',3:'happy',\
           4:'sad',5:'surprise',6:'neutral'}