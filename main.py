import numpy as np
import cv2
from deepface import DeepFace

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier()
#
#
# while(True):
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('From Camera', frame)
#     # cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# #
# cap.release()
# cv2.destroyAllWindows()
# result = DeepFace.verify(img1_path="C:/User/demon/Desktop/database/DSC_0307.jpg", img2_path="C:/User/demon/Desktop/database/DSC_0308.jpg")
# print(result)
#DeepFace.stream(db_path="C:/User/demon/Desktop/database ")