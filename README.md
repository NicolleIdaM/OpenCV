#PROJECT WITH OPENCV

##Requisitos
- Python
- OpenCV

##Questions that i had and you maybe having
###What's it for?
```
    #It capture the frame and return two values
    cap.read()
```

###Structur
```
    #cv2.putText(image, text, position, font, scale, color, thickness)
    cv2.putText(frames, titulo, (220, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 0, 128), 2)
    cv2.putText(frames, "Pressione 1-4 para trocar, 0 para sair", (130, 60), cv2.FONT_HERSHEY_DUPLEX, 0.6, (128, 0, 128), 1)
```