#Gunawardhana P.K.K.C.
#EG/2019/3596
#Task 02
import cv2
import numpy as np

def average_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

#Loading the image and convert to grey-scale
image = cv2.imread(r'E:\Image Processing Assignment\eiffel-tower.jpg',0)

#Check whether the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Apply 3x3 average filter
    average_3x3 = average_filter(image, 3)

    # Apply 10x10 average filter
    average_10x10 = average_filter(image, 10)

    # Apply 20x20 average filter
    average_20x20 = average_filter(image, 20)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('3x3 Average Filter', average_3x3)
    cv2.imshow('10x10 Average Filter', average_10x10)
    cv2.imshow('20x20 Average Filter', average_20x20)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

