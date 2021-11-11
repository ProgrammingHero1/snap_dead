from cv2 import cv2
import cvzone

overlay = cv2.imread('beard.png', cv2.IMREAD_UNCHANGED)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)

    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        resized_overlay = cv2.resize(overlay, ( int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, resized_overlay, [x-50, y-75])
    cv2.imshow('Snap Dead', frame)

    if cv2.waitKey(10) == ord('q'):
        break