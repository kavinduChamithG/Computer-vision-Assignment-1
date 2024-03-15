#Gunawardhana P.K.K.C.
#EG/2019/3596
#Task 04

import cv2
import numpy as np

# Loading the image
image1 = cv2.imread(r'E:\Image Processing Assignment\wwwwboat.jpg', 0)

# Iterating over the image array in steps given by the block size in each case
def iterate_image(image_array, block_size):
    for i in range(0, image_array.shape[0], block_size):
        for j in range(0, image_array.shape[1], block_size):
            current_block = image_array[i:i + block_size, j:j + block_size]
            # Calculate the average of the elements in the block
            avg = np.sum(current_block) / (block_size * block_size)
            # Replacing all elements in the block with the calculated average
            current_block[:] = avg


image_array = np.array(image1)

# Create a copy of the original image for later display
original_image = image1.copy()

# Applying the iteration for 3x3 blocks
iterate_image(image_array, block_size=3)
cv2.imshow('Modified Image (3x3 blocks)', image_array)

# Reset image array
image_array = original_image.copy()

# Applying the iteration for 5x5 blocks
iterate_image(image_array, block_size=5)
cv2.imshow('Modified Image (5x5 blocks)', image_array)

# Reset image array
image_array = original_image.copy()

# Applying the iteration for 7x7 blocks
iterate_image(image_array, block_size=7)
cv2.imshow('Modified Image (7x7 blocks)', image_array)

cv2.imshow('Original Image', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()



