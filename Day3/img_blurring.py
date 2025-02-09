import cv2
import time
import numpy as np

# importing algorithms
from PCA import pca_class

import os

# Ensure the 'output' directory exists, create it if not
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# importing feature extraction classes
from images_to_matrix import images_to_matrix_class

from dataset import dataset_class

# Algo Type
algo_type = "pca"


#No of images For Training(Left will be used as testing Image)
no_of_images_of_one_person = 8
dataset_obj = dataset_class(no_of_images_of_one_person)