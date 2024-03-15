#Gunawardhana P.K.K.C.
#EG/2019/3596
#Task 03

import cv2

# Loading the image
image = cv2.imread(r'E:\Image Processing Assignment\autumn1.jpg')

# Check if image is loaded successfully
if image is None:
    print("Error: Could not open the image.")
    exit()

# Define the angle of rotation
angle_45 = 45
angle_90 = 90

# Get the dimensions of the image
height, width = image.shape[:2]

# Calculating the rotation matrix
rotation_matrix_45 = cv2.getRotationMatrix2D((width / 2, height / 2), angle_45, 1)
rotation_matrix_90 = cv2.getRotationMatrix2D((width / 2, height / 2), angle_90, 1)

# Performing the rotation
rotated_image_45 = cv2.warpAffine(image, rotation_matrix_45, (width, height))
rotated_image_90 = cv2.warpAffine(image, rotation_matrix_90, (width, height))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image 45', rotated_image_45)
cv2.imshow('Rotated Image 90', rotated_image_90)

cv2.waitKey(0)
cv2.destroyAllWindows()

