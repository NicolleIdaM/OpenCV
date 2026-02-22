import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Unable to access the webcam!")
    exit()

effect = 0

print("EFFECTS")
print("1 - Normal")
print("2 - Grayscale")
print("3 - Border detection")
print("4 - Negative")
print("0 - Exit")

while True:
    returnImg, frame = capture.read()

    if not returnImg:
        print("Error capturing image")
        break

    frames = frame.copy()

    match effect:
        case 1:
            titulo = "Normal effect"
            
        case 2:
            frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames = cv2.cvtColor(frames, cv2.COLOR_GRAY2BGR)
            title = "Grayscale effect"
            
        case 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            borders = cv2.Canny(gray, 50, 150)
            frames = cv2.cvtColor(borders, cv2.COLOR_GRAY2BGR)
            title = "Border detection effect"
            
        case 4:
            frames = 255 - frame
            title = "Negative effect"
            
        case _:
            title = "Normal effect"

    cv2.putText(frames, title, (200, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 0, 128), 2)
    cv2.putText(frames, "Press 1-4 to change, 0 to exit", (150, 60), cv2.FONT_HERSHEY_DUPLEX, 0.6, (128, 0, 128), 1)
    
    cv2.imshow("Webcam with effect", frames)

    key =  cv2.waitKey(1) & 0xFF

    if key == ord("0"):
        print("Leaving...")
        break
        
    elif key == ord("1"):
        effect = 1
        print("Normal effect")
        
    elif key == ord("2"):
        effect = 2
        print("Grayscale effect")
        
    elif key == ord("3"):
        effect = 3
        print("Border detection effect")
        
    elif key == ord("4"):
        effect = 4
        print("Negative effect")

capture.release()
cv2.destroyAllWindows()