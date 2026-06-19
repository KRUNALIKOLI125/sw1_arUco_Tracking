ARUCO TRACKING PROJECT

Description
This project is the implementation of real time ArUco marker tracking with the help of open cv and a webcam. This system detects the marker position especially markers center and then guide us to  match the center of the marker  to the webcam center through visual indicators and text instructions

Dependencies
Python 3.x
OpenCV
NumPy

Installation
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
Running the Project
python aruco_test.py

## Tracking Logic

The program uses the webcam to look for an ArUco marker. When the marker is detected, the program finds its position on the screen. It then checks whether the marker is at the correct position or not. If the marker is away from the target position, the program shows an arrow and text instructions to guide it in the correct direction. As the marker moves, the instructions and arrow update continuously in real time.
