
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import blob_log
from env_variables import env
# from stopwatch import Stopwatch

base_image_path = env["base_image_path"]
output_image_path = env["output_image_path"]
image_names = env["image_names"]

###################################################################
# Motion Blur Analysis
###################################################################
'''
Meant for periodic white and black images. 
Have to measure across the periodic patterns. Use fine bars whose width is smaller than the motion blur length, and take the mean across the perpendicular axis
0 - No luminance difference. Motion blur washed out the patttern
1 - Maximum contrast. Almost no contrast was lost
'''
def staticMichaelsonContrast(img, axis = 0):
    # average along the axis parallel to the bars. 0 for vertical
    img_float = img.astype(np.float64)
    profile = np.mean(img_float, axis=axis)

    l_max = np.max(profile)
    l_min = np.min(profile)

    # Avoid division by zero for completely black images
    if l_max + l_min == 0:
        return 0.0

    return float((l_max - l_min) / (l_max + l_min))

def modulationTransfer(imgBlurred, imgStatic):
    c_static = local_michelson_contrast(roi_static)
    if c_static == 0:
        return 0.0
    return local_michelson_contrast(roi_blurred) / c_static

'''
Breaking the image down into sine waves of different frequencies and orientations. 
0 - High frequency wiped out - Heavy motion blur
1 - High Frequency survived - Almost no motion blur 
'''
def high_freq_energy_ratio(img_blurred, img_static):
    def high_freq_mag(img):
        f = np.fft.fftshift(np.fft.fft2(img.astype(np.float64)))
        mag = np.abs(f)
        # Mask out the low-frequency center (DC component)
        h, w = mag.shape
        cy, cx = h // 2, w // 2
        r = min(h, w) // 8
        y, x = np.ogrid[:h, :w]
        mask = (x - cx)**2 + (y - cy)**2 > r**2
        return np.mean(mag[mask])

    return float(high_freq_mag(img_blurred) / high_freq_mag(img_static))


def main():
    # For each of the images
    for i in image_names:
        print(i)
        img = cv2.imread(f'{base_image_path}\\{i}')
        image_title = i.split(".")[0]
        image_extention = i.split(".")[1]

        

        
        
        # img = cv2.GaussianBlur(img, (0, 0), sigmaX=sigma, sigmaY=sigma)
        # cv2.imwrite( f"{output_image_path}\\{image_title}_blurred.{image_extention}", img)


        
        



main()
