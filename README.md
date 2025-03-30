# Student Attendance System

## 📌 About
The **Student Attendance System** is a CLI-based Python application designed to help teachers efficiently manage and record student attendance using CSV files. It automates attendance tracking by allowing users to create attendance files and record daily attendance with minimal effort.

## 🚀 Features
- 📂 **CSV-based Data Storage** – Stores attendance records efficiently.
- 📝 **Automated Attendance Entry** – Input daily attendance quickly.
- 🎓 **Customizable Student List** – Add student names dynamically.
- 📅 **Topic-Based Tracking** – Records attendance along with the topic covered.

## 🛠 Technologies Used
![Python](https://forthebadge.com/images/badges/made-with-python.svg)

## 📖 How It Works
1. **Create a New Attendance File**
   - Run the script and choose to create a new file.
   - Enter the number of students and their names.
   - A CSV file is generated with appropriate headers.

2. **Record Daily Attendance**
   - Enter the existing CSV file name.
   - Input the topic for the day.
   - Mark each student as **Present (P)** or **Absent (A)**.
   - Attendance is saved automatically.

## ▶️ Usage
```sh
python student_attendance.py
```
Follow the prompts to create a new file or record attendance in an existing file.

## 📌 Example
**Sample CSV Output:**
```
Date,Topic,Student1,Student2,Student3
03/30/25,Math,P,A,P
03/31/25,Science,P,P,A
```

## 📜 Contributing
Feel free to fork the repository and contribute improvements! 🚀

---
**📌 Note:** This is a simple CLI-based attendance tracker and does not include advanced features like a GUI or database integration.

