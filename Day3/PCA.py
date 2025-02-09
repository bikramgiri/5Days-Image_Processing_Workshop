import numpy as np
import cv2
import scipy.linalg as s_linalg


class pca_class:
    def __init__(self, images, y, target_names, no_of_elements, quality_percent):
        self.no_of_elements = no_of_elements
        self.images = np.asarray(images)
        self.y = y
        self.target_names = target_names
        mean = np.mean(self.images, 1)
        self.mean_face = np.asmatrix(mean).T
        self.images = self.images - self.mean_face
        self.quality_percent = quality_percent



   