#Gunawardhana P.K.K.C.
#EG/2019/3596
#Task 01

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

levels = 2
image = None

#Change the number of intensity levels
def change_intensity_levels(value):
    global levels
    levels = 2 ** value
    if image is not None:
        reduce_levels()

#Reduce the number of intensity levels
def reduce_levels():
    global image
    global levels
    image_reduced_levels = np.floor_divide(image, 256 // levels) * (256 // levels)
    cv2.imshow('Intensity Level Changed Image', image_reduced_levels)

#Opening an image using a filedialog
def open_image():
    global image
    filename = filedialog.askopenfilename()
    if filename:
        original_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        if original_image is not None:
            image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
            cv2.imshow('Original Image', image)
            reduce_levels()
            cv2.createTrackbar('Intensity Level', 'Intensity Level Changed Image', 1, 8, change_intensity_levels)

#Create a window
cv2.namedWindow('Intensity Level Changed Image')

root = tk.Tk()
root.title("Image Intensity Reduction")

# Create a button to open an image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

root.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()
