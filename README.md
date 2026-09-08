# Job Application Tracker

A Django-based web application for managing job applications, tracking application progress, and maintaining multiple resume versions in one place.

## Features

* User authentication with login and logout
* Add, edit, and delete job applications
* Track application status:

  * Applied
  * Interview
  * Selected
  * Rejected
  * Withdrawn
* Record interview dates and application notes
* Search applications by company
* Filter applications by status
* Dashboard with application statistics
* Recent application overview
* Upload and manage multiple resume versions
* Set an active resume
* View and download uploaded resumes
* REST API for job application management
* API support for GET, POST, PUT, PATCH, and DELETE operations
* User-specific data access and isolation

## Tech Stack

* **Backend:** Python, Django
* **API:** Django REST Framework
* **Database:** SQLite
* **Frontend:** HTML, CSS, Django Templates
* **File Handling:** Django FileField
* **API Testing:** Postman
* **Version Control:** Git, GitHub

## Project Structure

```text
Job_Application_Tracker/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tracker/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── api.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint          | Purpose                         |
| ------ | ----------------- | ------------------------------- |
| GET    | `/api/jobs/`      | List user's applications        |
| POST   | `/api/jobs/`      | Create an application           |
| GET    | `/api/jobs/<id>/` | Retrieve an application         |
| PUT    | `/api/jobs/<id>/` | Update an application           |
| PATCH  | `/api/jobs/<id>/` | Partially update an application |
| DELETE | `/api/jobs/<id>/` | Delete an application           |

All API endpoints require authentication.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Nazeer636/Job-Application-Tracker.git
cd Job-Application-Tracker
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Testing

The application was manually tested for:

* Authentication and logout
* Job application CRUD operations
* Dashboard statistics
* Search and status filtering
* Resume upload, download, deletion, and active-resume selection
* REST API CRUD operations
* User data isolation
* Form validation and edge cases

## Future Improvements

* Application reminders and interview notifications
* Resume-to-job matching
* Application analytics and charts
* Deployment to a cloud platform
* Automated unit and API tests
* Additional API filtering and pagination
