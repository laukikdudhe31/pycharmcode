import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Person.jpeg')
resized_img = cv2.resize(img, (100, 100))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(10,10))

for (x, y, w, h) in faces:
    cv2.rectangle(gray,(x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Face_detection', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()