import dlib
import face_recognition
import cv2
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

image_input = face_recognition.load_image_file('dataset/will_smith.jpeg')
face_locations = face_recognition.face_locations(image_input)

for i, face_location in enumerate(face_locations):
    top, right, bottom, left = face_location

    print(face_location)

    # Extract face
    face_img = image_input[top:bottom, left:right, ::-1]

    # Display face using cv2.imshow
    cv2.imshow('Willy', face_img)
    cv2.waitKey(0)  # Wait for a key press to close the window

cv2.destroyAllWindows()  # Close all cv2 windows after processing

