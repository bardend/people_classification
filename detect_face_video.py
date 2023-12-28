import matplotlib
import dlib
import face_recognition
import cv2
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Ruta del archivo de video (puedes usar 0 para la cámara web)
video_path = 'dataset/Ricardo_ulloa.mp4'

# Crear un objeto VideoCapture
cap = cv2.VideoCapture(video_path)

# Verificar si el video se abrió correctamente
if not cap.isOpened():
    print("Error al abrir el video.")
    exit()

# Bucle para leer los fotogramas del video
while True:
    # Leer un fotograma
    ret, frame = cap.read()

    # Verificar si se alcanzó el final del video
    if not ret:
        break

    face_locations = face_recognition.face_locations(frame)

    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location 
        face_img = frame[top:bottom, left:right]
        # Display face using cv2.imshow
        cv2.imshow('Willy', face_img)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()

