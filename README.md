# 📘 Recipe API – Flask + SQLite

A simple REST API built using Flask and SQLite to manage and retrieve recipe data.  
This project demonstrates backend development concepts including routing, database connectivity, filtering, and record counting.

---

## 📌 Project Overview

This API allows you to:

- View all recipes
- Get total record count
- Filter recipes by query parameters
- Access recipe data via HTTP endpoints

It is designed as a beginner-friendly backend project using Flask and SQL.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- SQLite
- SQL

---

## 📂 Project Structure

```
project-folder/
│
├── app.py
├── recipes.db
├── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install flask
```

### 2️⃣ Run the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

### 🔹 Home
```
GET /
```
Returns a confirmation message that the server is running.

---

### 🔹 Get All Recipes
```
GET /recipes
```
Returns all records from the `recipes` table.

---

### 🔹 Get Total Record Count
```
GET /count
```
Returns total number of records in the database.

Example Response:
```
Total records: 120
```

---

### 🔹 Filter Recipes
```
GET /filter?country=India
```
Returns recipes filtered by country (or other query parameters if implemented).

---

## 🗄️ Database Details

- Database File: `recipes.db`
- Table Name: `recipes`

Example Table Structure:

| id | name | country | ingredients |
|----|------|---------|------------|

---

## ⚠️ Common Issues

### 404 Not Found

If a route returns 404:

- Ensure the route is defined in `app.py`
- Restart the Flask server after making changes
- Check the URL spelling

---

## 🎯 Future Improvements

- Add pagination support
- Add JSON responses
- Implement POST, PUT, DELETE APIs
- Add frontend interface
- Deploy to production using Gunicorn / Render / Railway

