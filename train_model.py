import cv2
import os
import numpy as np

dataset_path = "images"

faces = []
labels = []
names = {}

label_id = 0

for person in sorted(os.listdir(dataset_path)):

    person_path = os.path.join(dataset_path, person)

    if os.path.isdir(person_path):

        names[label_id] = person

        for image in os.listdir(person_path):

            image_path = os.path.join(person_path, image)

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            if img is not None:
                faces.append(img)
                labels.append(label_id)

        label_id += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

if not os.path.exists("trainer"):
    os.makedirs("trainer")

recognizer.save("trainer/trainer.yml")

print("Model Trained Successfully!")
print("Students:", names)