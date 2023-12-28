import numpy as np
import cv2
import os

def predict(img, cnt):
    output_folder = 'dataset/Aida_vallejo'  # Carpeta para almacenar los frames
    output_path = os.path.join(output_folder, f"frame_{cnt}.jpg")
    cv2.imwrite(output_path, img)

    #cv2.imshow('face', img)

    # Ejemplo de uso de la función predict
