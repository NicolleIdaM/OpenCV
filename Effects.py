import cv2
import numpy as np

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Erro: Não foi possível acessar a webcam!")
    exit()