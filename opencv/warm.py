from PIL import Image
import os
import numpy as np
import cv2
from matplotlib import pyplot as plt

def start(txtpath, image_path):
    # 0. All images are stored in a folder named 'image'
    # Each image is processed individually

    # Read the list of image filenames from a text file
    with open(txtpath, 'r') as file:
        image_names = file.readlines()

    # Remove any trailing newline characters
    image_names = [name.strip() for name in image_names]
    
    for filename in image_names:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder_path, filename)
            calculate_cool_warm(image_path)

def calculate_cool_warm(image_path):
    # 1. Load the image and extract its RGB values
    img_bgr = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 3. Compute warm-cool value for each pixel using the formula:
    # (R - B)/255 + G/255, then divided by 2
    warm_cool = ((img_rgb[:, :, 0] - img_rgb[:, :, 2]) / 255 + img_rgb[:, :, 1] / 255) / 2

    # 4. Filter out pixels with a warm-cool value of exactly 0
    warm_cool_nonzero = warm_cool[warm_cool != 0]

    # 5. Flatten the array and compute the average warm-cool value of the image
    warm_cool_flattened = warm_cool_nonzero.flatten()
    image_name = image_path.split('.')[0].split('\\')[-1]  # Extract the image filename (without extension)

    # 6. Save the image name and its corresponding average warm-cool value to 'cool_warm1.txt'
    with open("cool_warm1.txt", "a") as file:
        file.write(f"{image_name}:  {np.mean(warm_cool_flattened)}\n")

    # 7. Loop back to process the next image

if __name__ == "__main__":
    image_folder_path = "image_role"  # Folder containing all images
    txtpath = "no_detect.txt"         # Text file listing the image names to be processed
    start(txtpath, image_folder_path)

