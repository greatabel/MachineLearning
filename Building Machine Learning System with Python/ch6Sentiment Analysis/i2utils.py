import os
import collections
import csv
import json

from matplotlib import pylab
import numpy as np


DATA_DIR = "data"
CHART_DIR = "charts"

if not os.path.exists(DATA_DIR):
    raise RuntimeError("Expecting directory 'data' in current path")

if not os.path.exists(CHART_DIR):
    os.mkdir(CHART_DIR)


def load_sanders_data(dirname=".", line_count=-1):
    count = 0