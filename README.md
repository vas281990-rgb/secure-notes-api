# 🔐 Secure Notes API

Secure Notes API is a REST API built with FastAPI for safely storing personal notes.
The project includes user authentication, JWT authorization, and encryption of note contents.

This project was created as a **portfolio project for a Middle Python Developer** position.

---

## 🚀 Features

- User registration and login
- JWT-based authentication
- CRUD operations for notes
- Encryption of note content before saving to the database
- Automatic decryption when retrieving notes
- SQLAlchemy ORM
- Environment variables configuration (.env)

---

## 🛠️ Tech Stack

- **Python 3.13**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic v2**
- **JWT (python-jose)**
- **Passlib (bcrypt)**
- **Cryptography**
- **SQLite**
- **Uvicorn**

---

## 📂 Project Structure

secure-notes-api/
│
├── app/
│ ├── main.py # Application entry point
│ ├── auth.py # Authentication & JWT logic
│ ├── notes.py # Notes endpoints (CRUD)
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # Database connection
│ └── security/
│ └── crypto.py # Encryption & decryption logic
│
├── .env # Environment variables
├── requirements.txt # Project dependencies
├── notes.db # SQLite database (local)
└── README.md

---

## ⚙️ Installation & Run

```bash
git clone https://github.com/vas281990-rgb/secure-notes-api.git
cd secure-notes-api

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
🔑 Environment Variables (.env)
DATABASE_URL=sqlite:///./notes.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
📖 API Documentation
After starting the server, open:
http://127.0.0.1:8000/docs
Swagger UI provides full interactive API documentation.
🎯 Project Goal
This project demonstrates:
Backend architecture skills
Secure authentication and authorization
Encryption of sensitive data
Clean code structure
Readiness for real-world backend tasks