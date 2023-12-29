import numpy as np
import cv2
import os

names = ['Ricardo_Ulloa', 'Aida_Vallejo']
def predict(new_data, frame, position, model):

    height, width = new_data.shape[:2]

    if height > 0 and width > 0 :

        new_data = cv2.resize(new_data, (170, 170))
        predict_image=np.expand_dims(new_data, axis=0)
        predict = model.predict(predict_image)
        print(predict)
        #return the index of the max predict
        class_idx = np.argmax(predict)
        #the classe name 
        class_name = names[class_idx]
        max_prob = np.max(predict)*100
        print(max_prob,"%")

        text = class_name +" "+str(int(np.max(predict)*100) ) +"%"
        #add text to the image
        cv2.rectangle(frame, position,(0, 255, 0),thickness=2)  
        cv2.putText(  frame, text, (position[0], position[1]), cv2.FONT_HERSHEY_SIMPLEX  , 0.5, (255, 0, 0), 2)
        #print(class_name)

    #cv2.imshow('face', img)

   # Ejemplo de uso de la función predict
