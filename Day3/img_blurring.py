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
# from images_matrix_for_2d_square_pca import  images_to_matrix_class_for_two_d
from dataset import dataset_class

# Algo Type (pca, 2d-pca, 2d2-pca)
algo_type = "pca"


#for single image = 0
#for video = 1
#for group image = 2
# reco_type = 0

#No of images For Training(Left will be used as testing Image)
no_of_images_of_one_person = 8 
dataset_obj = dataset_class(no_of_images_of_one_person)


#Data For Training
images_names = dataset_obj.images_name_for_train
y = dataset_obj.y_for_train
no_of_elements = dataset_obj.no_of_elements_for_train
target_names = dataset_obj.target_name_as_array

#Data For Testing
images_names_for_test = dataset_obj.images_name_for_test
y_for_test = dataset_obj.y_for_test
no_of_elements_for_test = dataset_obj.no_of_elements_for_test


training_start_time = time.process_time()
img_width, img_height = 50, 50

if algo_type == "pca":
    i_t_m_c = images_to_matrix_class(images_names, img_width, img_height)