# 🤖 AI-Based Smart Attendance System

<<<<<<< HEAD
## 📌 Overview

The **AI-Based Smart Attendance System** is developed using **Python** and **OpenCV**. The system detects and recognizes registered student faces through a webcam and automatically records attendance with the current date and time. It also prevents duplicate attendance entries for the same day.

=======
An AI-powered Smart Attendance System developed using **Python** and **OpenCV**. The application detects and recognizes registered student faces through a webcam and automatically records attendance with the current **date**, **time**, and **status**. It also prevents duplicate attendance entries for the same day.

>>>>>>> b696ba9 (Improve README)
---

## ✨ Features

- 👤 Face Detection using Haar Cascade
- 🧠 Face Recognition using LBPH Algorithm
<<<<<<< HEAD
- 📸 Student Image Capture
- 🎓 Student Registration
- ⚙️ Model Training
- ✅ Automatic Attendance Marking
- 📅 Date & Time Logging
=======
- 📸 Student Image Registration
- ⚙️ Model Training
- ✅ Automatic Attendance Marking
- 📅 Date & Time Recording
>>>>>>> b696ba9 (Improve README)
- 📄 Attendance Report in CSV Format
- 🚫 Duplicate Attendance Prevention

---

## 🛠 Technologies Used

- Python
- OpenCV
- NumPy
- CSV
- VS Code

---

## 📂 Project Structure

```text
AI-Based-Smart-Attendance-System
│
├── attendance/
├── screenshots/
├── trainer/
├── app.py
├── train_model.py
├── recognize.py
├── attendance_system.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/23a31a04r5/AI-Based-Smart-Attendance-System.git
```

Move into the project folder:

```bash
cd AI-Based-Smart-Attendance-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Capture Student Images

```bash
py app.py
```

### Step 2: Train the Model

```bash
py train_model.py
```

### Step 3: Start the Attendance System

```bash
py attendance_system.py
```

---

<<<<<<< HEAD
## 📊 Output

- Detects and recognizes registered student faces.
- Automatically marks attendance.
- Stores attendance in **attendance.csv** with:
  - Student Name
  - Date
  - Time
  - Attendance Status
=======
## 📸 Sample Attendance Report

The system automatically records attendance with the student's name, date, time, and attendance status.

![Attendance Report](screenshots/attendance_report.png)

> **Note:** This screenshot uses sample data for demonstration purposes.

---

## 📊 Output

The system automatically:

- Detects registered student faces
- Recognizes students using the trained model
- Marks attendance only once per day
- Stores attendance with date and time in a CSV file
>>>>>>> b696ba9 (Improve README)

---

## 🔮 Future Enhancements

- 🖥 GUI Interface
- 🗄 Database Integration (SQLite/MySQL)
- 📧 Email Notifications
<<<<<<< HEAD
- 🆔 Student ID Integration
- ☁️ Cloud Attendance Storage
- 📱 Mobile Application Support
=======
- 🆔 Student ID Support
- ☁️ Cloud-Based Attendance Storage
- 📱 Mobile Application
>>>>>>> b696ba9 (Improve README)

---

## 👩‍💻 Author

**Madhuri**

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.