# TrackSphere – Multi-Tenant Project Management API

## Overview

TrackSphere is a backend system built using Django and Django REST Framework.
It implements a **multi-tenant architecture**, allowing multiple organizations to manage their own users, projects, and tasks securely within a single application.

---

## Features

* Multi-tenant architecture (organization-based data isolation)
* User authentication using JWT
* Role-based access (Admin, Manager, etc.)
* Project management
* Task management
* Secure REST APIs

---

## Tech Stack

* Backend: Django, Django REST Framework
* Database: PostgreSQL
* Authentication: JWT

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/swap1799/tracksphere.git

### 2. Navigate to project

cd tracksphere

### 3. Create virtual environment

python -m venv venv

### 4. Activate environment

venv\Scripts\activate  (Windows)

### 5. Install dependencies

pip install -r requirements.txt

### 6. Create .env file

SECRET_KEY=your-secret-key
DEBUG=True

### 7. Run migrations

python manage.py migrate

### 8. Run server

python manage.py runserver

---

## API Endpoints

* /api/auth/register/
* /api/auth/login/
* /api/projects/
* /api/tasks/

---

## Author

Swapna Shelke
