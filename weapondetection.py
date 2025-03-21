import numpy as np
import cv2
import imutils
import datetime

# Load the cascade classifier for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False  # Initialize gun_exist to False

while True:
    ret, frame = camera.read()

    if not ret:
        break  # Break the loop if the frame is not captured successfully

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

if gun_exist:
    print("Guns detected")
else:
    print("Guns not detected")

camera.release()
cv2.destroyAllWindows()