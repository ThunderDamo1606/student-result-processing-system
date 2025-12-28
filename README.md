# Student Result Processing System (Python + Tkinter + MySQL)

A simple desktop-based application for managing students, inserting marks, and viewing results using Python Tkinter GUI and MySQL database.

This project helps beginners understand:
- GUI programming (Tkinter)
- Python + MySQL connectivity
- Basic CRUD concepts
- Result processing logic

## ✨ Features

### 👨‍💼 Admin Panel
- Add new students
- Add marks for students

### 🎓 Student Panel
- Search result using Roll Number
- Shows PASS / FAIL status

> A student passes only if all subjects have marks greater than 40.

## 📂 Project Structure

📁 Student-Result-System  
│  
├── guitest6.py — Calculator (Tkinter demo)  
├── gutest2.py — Button layout demo  
├── student.py — Student & Marks entry forms  
├── guitest7.py — Main Application (Admin + Student)  
├── tables.txt — Database tables reference  
└── README.md  

Main file to run: **guitest7.py**

## 🛠 Technologies Used
- Python 3
- Tkinter
- MySQL
- mysql-connector-python

## 🗄 Database Setup (MySQL)

Create database and tables:

```sql
CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE student (
  rollno INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(50)
);

CREATE TABLE marks (
  rollno INT,
  sub1 INT,
  sub2 INT,
  sub3 INT
);
