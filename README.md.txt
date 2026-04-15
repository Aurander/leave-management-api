# Leave Management API

## Overview
This is a RESTful API built using Django REST Framework for managing employee leave requests. It includes authentication and role-based access control.

## Features
- User Registration & Login (JWT Authentication)
- Apply for Leave
- View Personal Leave Requests
- Admin Approval/Rejection System

## Tech Stack
- Python
- Django
- Django REST Framework

## API Endpoints

### Auth
- POST /api/register/
- POST /api/login/

### Leave
- POST /api/leaves/
- GET /api/leaves/
- PATCH /api/leaves/{id}/

## How to Run

```bash
pip install -r requirements.txt
python manage.py runserver