# ITI Django Project

## Project Overview
This is a Django web application for managing **trainees** and **courses**. The application allows users to:
- View, add, update, and delete trainees
- View, add, update, and delete courses
- User authentication (login & registration)
- API endpoints for trainee and track management

## Features
✅ List all trainees and courses  
✅ Add new trainees and courses  
✅ Update and delete trainees/courses  
✅ Authentication system (login & registration)  
✅ API for trainee and track management  

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AmeraKhaled/Django_day1.git
cd Django_day1
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Mac/Linux:
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
Then open **http://127.0.0.1:8000/** in your browser.

---

## Project Structure
```
/ITIan/               # Main Django project folder
    ├── accounts/     # Authentication app
    ├── course_app/   # Course management app
    ├── trainee_app/  # Trainee management app
    ├── templates/    # HTML templates
    ├── static/       # CSS, JavaScript, images
    ├── api/          # API for trainee & track
    ├── manage.py     # Django command-line tool
```
### Authentication
The project includes authentication for login and registration.

Login: ``` /accounts/login/```
Register:``` /accounts/register/```
Logout: ```/accounts/logout/```

### API Endpoints
## Trainee API (Class-Based Views)
```GET /api/trainees/``` → List all trainees
```POST /api/trainees/``` → Add a new trainee
## Trainee API (Generic Views)
```PUT /api/trainees/<id>/update/``` → Update a trainee
```DELETE /api/trainees/<id>/delete/``` → Delete a trainee
### API Setup
The API uses Django REST Framework (DRF). To install:
```bash
pip install djangorestframework
```
Then, add 'rest_framework' to INSTALLED_APPS in settings.py.
and then run
```bash 
python manage.py runserver
```

