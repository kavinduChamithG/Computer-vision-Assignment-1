import cv2
import tkinter as tk
from tkinter import filedialog

def change_intensity(intensity_levels):
    if original_image is not None:
        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        # Apply intensity levels
        adjusted_image = cv2.convertScaleAbs(grayscale_image, alpha=intensity_levels / 255)
        cv2.imshow("Adjusted Image", adjusted_image)

def open_image():
    global original_image
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = cv2.imread(file_path)
        cv2.imshow("Original Image", original_image)
        cv2.createTrackbar("Intensity Levels", "Original Image", 0, 255, change_intensity)

# Initialize original_image to None
original_image = None

# Create the main window
root = tk.Tk()
root.title("Intensity Adjuster")

# Create a button to open the image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Open the Tkinter window
root.mainloop()

# Close all OpenCV windows
cv2.destroyAllWindows()
