📝 FastAPI Task Manager (MySQL Backend)
A modular, lightweight RESTful API built with FastAPI and SQLAlchemy, configured to connect to a MySQL relational database. This repository demonstrates clean code practices by separating concerns across dedicated modules for database connections, models, schemas, CRUD functions, and API routing.

📁 Repository Structure
.gitignore: Prevents tracking virtual environments, logs, and sensitive credentials

todo.py: Application entrypoint & FastAPI route handlers

db_td.py: MySQL database engine & session creation logic

mod.py: SQLAlchemy database ORM models

sch.py: Pydantic schemas for data validation and response formatting

crude.py: CRUD helper functions for database operations

🧩 Module Overview
1. todo.py (API Handler)
Houses endpoint routes (GET, POST, PUT, DELETE), initializes the FastAPI instance, and injects DB sessions via Depends(get_db).

2. db_td.py (Database Config)
Configures the SQLAlchemy MySQL engine using pymysql, creates SessionLocal, and defines get_db() session generator.

3. mod.py (ORM Models)
Defines database schema tables (such as Todo/Task) mapped directly to MySQL columns using SQLAlchemy base models.

4. sch.py (Data Schemas)
Pydantic models (TodoCreate, TodoResponse, TodoUpdate) validating incoming request payloads and structuring responses.

5. crude.py (CRUD Logic)
Contains clean, reusable functions (create_todo, get_todos, update_todo, delete_todo) to query MySQL without cluttering routes.

🛠️ Tech Stack
Framework: FastAPI

Database Engine: MySQL

ORM: SQLAlchemy

Database Driver: PyMySQL (pymysql)

Validation: Pydantic

Server: Uvicorn

🚀 Getting Started
Step 1: Clone the Repository
git clone https://github.com/luckypatel6388-source/fastapi-task-manager.git
cd fastapi-task-manager

Step 2: Set Up Virtual Environment & Dependencies
Create virtual environment
python -m venv venv

Activate on Windows
venv\Scripts\activate

Activate on macOS/Linux
source venv/bin/activate

Install required packages
pip install fastapi uvicorn sqlalchemy pymysql pydantic

Step 3: Configure MySQL Connection
In db_td.py, update your MySQL connection URL:

DATABASE_URL = "mysql+pymysql://:@:/<database_name>"

Example Local MySQL URL:
mysql+pymysql://root:password123@localhost:3306/todo_db

Step 4: Run the API
Launch the local development server with auto-reload enabled:

uvicorn todo:app --reload

API Root: http://127.0.0.1:8000

Swagger Interactive Docs: http://127.0.0.1:8000/docs

ReDoc Documentation: http://127.0.0.1:8000/redoc

🔗 Endpoints Summary
POST /todos/ — Create a new task

GET /todos/ — Retrieve all tasks

GET /todos/{todo_id} — Retrieve task details by ID

PUT /todos/{todo_id} — Update task details or completion status

DELETE /todos/{todo_id} — Delete a task
