import cv2
import numpy as np

aruco = cv2.aruco

dictionary = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)

# Generate marker
marker = aruco.generateImageMarker(dictionary, 0, 400)

# Add white border around marker
border_size = 100
marker_with_border = cv2.copyMakeBorder(
    marker,
    border_size,
    border_size,
    border_size,
    border_size,
    cv2.BORDER_CONSTANT,
    value=255
)

cv2.imwrite("marker0.png", marker_with_border)

print("Marker saved as marker0.png")