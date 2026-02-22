# PROJECT WITH OPENCV

## Folder Structure
```
.
├─ .git (excluded)
├─ Effects.py
└─ README.md
```

## Technologies
- Python
- OpenCV

## Questions that i had and you maybe having
### What's it for?
```
    #It capture the frame and return two values
    cap.read()
```
```
    #1 channel to 3 channels
    frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames = cv2.cvtColor(frames, cv2.COLOR_GRAY2BGR)
```
```
    #This ensures that the keystroke is captured correctly.
    0xFF
```
```
    #Capture frame by frame to be able to create the effect on each part of the face.
    frames = frame.copy()
```

### Structure

```
    #cv2.putText(image, text, position, font, scale, color, thickness)
    cv2.putText(frames, titulo, (220, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 0, 128), 2)
    cv2.putText(frames, "Pressione 1-4 para trocar, 0 para sair", (130, 60), cv2.FONT_HERSHEY_DUPLEX, 0.6, (128, 0, 128), 1)
```
