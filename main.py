
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import blob_log
from env_variables import env
# from stopwatch import Stopwatch

base_image_path = env["base_image_path"]
output_image_path = env["output_image_path"]

image_names = env["image_names"][0]




def main():
    # For each of the images
    for i in image_names:
        img = cv2.imread(f'{base_image_path}\\{i}')

        b, g, r = cv2.split(img)
        baseImg = b

        image_title = i.split(".")[0]
        image_extention = i.split(".")[1]
        # Pre Processing
        sigma = 1
        
        # img = cv2.GaussianBlur(img, (0, 0), sigmaX=sigma, sigmaY=sigma)
        # cv2.imwrite( f"{output_image_path}\\{image_title}_blurred.{image_extention}", img)


        
        



main()
