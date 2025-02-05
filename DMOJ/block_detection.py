import cv2
import numpy as np

# Step 1: Load the image
image_path = r'C:\Users\decub\Downloads\WIN_20241117_13_27_21_Pro.jpg'
image = cv2.imread(image_path)  # Replace with your image path

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Detect edges using Canny
edges = cv2.Canny(gray, 50, 150)

# Step 4: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Loop through contours to find prism-like shapes
for contour in contours:
    # Approximate contour to a polygon
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Look for shapes with 6+ vertices (indicative of 3D perspective)
    if len(approx) >= 6:
        # Optionally, filter based on area to remove noise
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust this threshold as needed
            # Draw the contour on the original image
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 100)

# Step 6: Show the results
cv2.imshow('Detected Rectangular Prisms', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
