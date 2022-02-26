import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from common import get_training_data

save_path = "data"

demo_path = "data/train/s/1_右食指_u_b_20210416081256.bmp"


labels = ["n", "s"]




train = get_training_data(save_path + "/train")
test = get_training_data(save_path + "/test")
print(f"Train: {len(train)}, Test: {len(test)}")


