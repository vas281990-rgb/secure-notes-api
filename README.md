# Secure Notes API 📝🔒

**Secure Notes API** is a simple and secure API for creating, reading, and deleting notes with user registration and JWT authentication.  
Built with **FastAPI**, **SQLAlchemy**, **JWT**, and **Fernet encryption**.

---
 # Secure Notes API 📝🔒

**Secure Notes API** is a simple and secure API for creating, reading, and deleting notes with user registration and JWT authentication.  
Built with **FastAPI**, **SQLAlchemy**, **JWT**, and **Fernet encryption**.

---

## ⚡ Features

- User registration and login
- JWT tokens for authentication
- Encryption of note content (Fernet)
- CRUD operations for notes (Create, Read, Delete)
- SQLite database
- Swagger UI for API testing

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/vas281990-rgb/secure-notes-api.git
cd secure-notes-api
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root with the following variables:

env
Copy code
SECRET_KEY=super-secret-key
ALGORITHM=HS256
FERNET_KEY=Uuq_6ggR59ftgGucmwOlOJ6fDlkuQEnpifW8zu-BsTU=
⚠️ Never upload your real .env file with secrets to GitHub.

🚀 Running the project
bash
Copy code
uvicorn app.main:app --reload
API will be available at: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Health check: http://127.0.0.1:8000/health

🛠 API Endpoints
Auth
Method	Path	Description
POST	/auth/register	Register a new user
POST	/auth/login	Get JWT token for login

Notes
Method	Path	Description
GET	/notes/	Get all notes for the user
POST	/notes/	Create a new note
DELETE	/notes/{id}	Delete a note by its ID

🔑 Example Usage
Register a user
bash
Copy code
POST /auth/register
{
  "username": "alice",
  "password": "securepassword"
}
Login and get JWT token
bash
Copy code
POST /auth/login
username=alice
password=securepassword
Response:

json
Copy code
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
Create a note
bash
Copy code
POST /notes/
Authorization: Bearer JWT_TOKEN_HERE
{
  "title": "My first note",
  "content": "This is a secret note"
}
Get all notes
bash
Copy code
GET /notes/
Authorization: Bearer JWT_TOKEN_HERE
Response:

json
Copy code
[
  {
    "id": 1,
    "title": "My first note",
    "content": "This is a secret note"
  }
]
💾 Database
SQLite file: notes.db

Models:

User: id, username, hashed_password

Note: id, title, content, owner_id

📌 Recommendations
For other developers, you can provide a .env.example with placeholders:

env
Copy code
SECRET_KEY=replace-with-your-secret
ALGORITHM=HS256
FERNET_KEY=replace-with-your-fernet-key
Do not commit .env or notes.db to GitHub (they are already in .gitignore).

🧪 Testing
Use Swagger UI: http://127.0.0.1:8000/docs

You can test all endpoints there.

📜 License
Project is open for personal and educational use.
## ⚡ Features

- User registration and login
- JWT tokens for authentication
- Encryption of note content (Fernet)
- CRUD operations for notes (Create, Read, Delete)
- SQLite database
- Swagger UI for API testing

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/vas281990-rgb/secure-notes-api.git
cd secure-notes-api
Create a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root with the following variables:

env
Copy code
SECRET_KEY=super-secret-key
ALGORITHM=HS256
FERNET_KEY=Uuq_6ggR59ftgGucmwOlOJ6fDlkuQEnpifW8zu-BsTU=
⚠️ Never upload your real .env file with secrets to GitHub.

🚀 Running the project
bash
Copy code
uvicorn app.main:app --reload
API will be available at: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

Health check: http://127.0.0.1:8000/health

🛠 API Endpoints
Auth
Method	Path	Description
POST	/auth/register	Register a new user
POST	/auth/login	Get JWT token for login

Notes
Method	Path	Description
GET	/notes/	Get all notes for the user
POST	/notes/	Create a new note
DELETE	/notes/{id}	Delete a note by its ID

🔑 Example Usage
Register a user
bash
Copy code
POST /auth/register
{
  "username": "alice",
  "password": "securepassword"
}
Login and get JWT token
bash
Copy code
POST /auth/login
username=alice
password=securepassword
Response:

json
Copy code
{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}
Create a note
bash
Copy code
POST /notes/
Authorization: Bearer JWT_TOKEN_HERE
{
  "title": "My first note",
  "content": "This is a secret note"
}
Get all notes
bash
Copy code
GET /notes/
Authorization: Bearer JWT_TOKEN_HERE
Response:

json
Copy code
[
  {
    "id": 1,
    "title": "My first note",
    "content": "This is a secret note"
  }
]
💾 Database
SQLite file: notes.db

Models:

User: id, username, hashed_password

Note: id, title, content, owner_id

📌 Recommendations
For other developers, you can provide a .env.example with placeholders:

env
Copy code
SECRET_KEY=replace-with-your-secret
ALGORITHM=HS256
FERNET_KEY=replace-with-your-fernet-key
Do not commit .env or notes.db to GitHub (they are already in .gitignore).

🧪 Testing
Use Swagger UI: http://127.0.0.1:8000/docs

You can test all endpoints there.

📜 License
Project is open for personal and educational use.