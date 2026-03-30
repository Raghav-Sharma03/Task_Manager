# Task Manager App

## 📌 Overview

This is a simple Task Manager application built using Flask (backend), React (frontend), and SQLite (database). It allows users to create, view, and delete tasks.

---

## 🛠 Tech Stack

* Backend: Python + Flask
* Frontend: React (Vite)
* Database: SQLite
* API: REST APIs

---

## 🚀 Features

* Add Task
* View Tasks
* Delete Task
* Input validation (task title is required)

---

## ⚙️ Setup Instructions

### Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install flask flask_sqlalchemy flask_cors
python app.py

### Frontend

cd frontend
npm install
npm run dev

---

## 🤖 AI Usage

* Used ChatGPT , GitHub Copilot to generate backend API and frontend UI
* All code was reviewed, tested, and improved manually

---

## ⚖️ Tradeoffs

* Used SQLite for simplicity instead of scalable DB like PostgreSQL
* Minimal UI to focus on functionality and correctness

---

## 🔮 Future Improvements

* Add authentication (login/signup)
* Add task filtering and search
* Add task status update (complete/incomplete)
* Improve UI/UX
