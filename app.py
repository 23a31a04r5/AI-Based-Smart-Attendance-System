import cv2
import os

student_name = input("Enter Student Name: ")

folder = f"images/{student_name}"

if not os.path.exists(folder):
    os.makedirs(folder)

camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

while True:

    success, frame = camera.read()

    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        count += 1

        face = frame[y:y+h, x:x+w]

        cv2.imwrite(f"{folder}/{count}.jpg", face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0),2)

        cv2.putText(frame, f"Images : {count}", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255,0,0),2)

    cv2.imshow("Capture Images", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if count >= 50:
        break

camera.release()
cv2.destroyAllWindows()

print("Images Saved Successfully!")