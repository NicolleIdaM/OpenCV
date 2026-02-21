import cv2
import numpy as np

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro: Não foi possível acessar a webcam!")
    exit()

effect = 0

print("EFFECTS")
print("1 - Normal")
print("2 - Gray scale")
print("3 - Border detection")
print("4 - Negative")
print("0 - Exit")

