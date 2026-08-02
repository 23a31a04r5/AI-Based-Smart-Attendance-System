import cv2
import csv
import os
from datetime import datetime

# Student Names
names = {
    0: "Devi",
    1: "Madhuri",
    2: "Meghana"
}

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

# Load face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

marked = []
today_attendance = set()

if os.path.exists("attendance/attendance.csv"):
    with open("attendance/attendance.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header

        for row in reader:
            if len(row) >= 2:
                name = row[0]
                date = row[1]

                if date == datetime.now().strftime("%d-%m-%Y"):
                    today_attendance.add(name)
while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        face = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face)

        if confidence < 75:

            name = names.get(label, "Unknown")

            if name not in today_attendance:

                today_attendance.add(name)

                now = datetime.now()

                date = now.strftime("%d-%m-%Y")
                time = now.strftime("%H:%M:%S")

                file_exists = os.path.exists("attendance/attendance.csv")

                with open("attendance/attendance.csv", "a", newline="") as file:

                    writer = csv.writer(file)

                    if not file_exists:
                        writer.writerow(["Name", "Date", "Time", "Status"])

                    writer.writerow([name, date, time, "Present"])

                print(name, "Attendance Marked")

        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.putText(frame, name,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,0,0),
                    2)

    cv2.imshow("Smart Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()