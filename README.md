# 💖 Task Manager CLI App

A beautiful and professional Command Line Task Manager built using Python.  
This application helps users manage daily tasks with priorities, deadlines, categories, and status tracking using a colorful terminal interface.

---

## ✨ Features

✔ User Registration & Login  
✔ Add Tasks  
✔ View Tasks  
✔ Complete Tasks  
✔ Delete Tasks  
✔ Priority-based Sorting  
✔ Deadline Validation   
✔ Task Categories  
✔ JSON File Storage  
✔ Beautiful CLI Interface using Rich  
✔ User-specific Tasks  

---

## 🛠 Technologies Used

- Python
- JSON
- Rich Library

---

## 📂 Project Structure

```text
SmartTaskManager/
│
├── main.py
├── auth.py
├── task_manager.py
├── tasks.json
├── users.json
├── requirements.txt
└── README.md
```

---

## 📦 Installation

Install required library:

```bash
pip install rich
```

OR

```bash
pip install -r requirements.txt
```

---

## ▶ Run Project

```bash
python main.py
```

---

## 💾 Storage

Tasks are stored in:

```text
tasks.json
```

Users are stored in:

```text
users.json
```

---

## 🌸 Features Explanation

### 🔐 Authentication
Users can create accounts and login securely.

### 📝 Task Management
Users can:
- Add tasks
- Delete tasks
- Mark tasks as completed
- View all tasks

### 🎯 Priority Sorting
Tasks are automatically sorted based on:
- High
- Medium
- Low

### 📅 Deadline Validation
Past dates are not accepted.

### ⚠ Overdue Detection
Tasks whose deadline has passed are automatically marked as OVERDUE.

### 🎨 Beautiful CLI
The project uses the Rich library for:
- colorful text
- styled tables
- aesthetic terminal UI

---

## 🚀 Future Improvements

- Search Tasks
- Edit Tasks
- Password Encryption
- Notifications
- Export Tasks
- Dark Theme
- Task Analytics

---

## 👩‍💻 Author

Karthiga V

---

## ⭐ Project Type

Professional Python CLI Project
