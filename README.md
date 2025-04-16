# Library-management


📚 Library Management System - Setup Instructions

✅ Features

Admin:
- Sign up & login
- Add, update, delete books
- View all books

Student:
- Register & login
- View all books only (no admin access)

---

⚙️ Setup Steps

1. Clone the Project

git clone https://github.com/your-username/library-management.git
cd library-management

---

2. Create a Virtual Environment (Recommended)

python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

---

3. 

pip install django mysqlclient

---

4. MySQL Configuration

- Open MySQL Workbench or terminal.
- Create a new database:

CREATE DATABASE lms;

- In settings.py, update the DATABASES config:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lms',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

---

5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

---

6. Run the Server

python manage.py runserver

Go to: http://127.0.0.1:8000/

---

7. URLs for Testing

- Admin Register: /admin_register/
- Admin Login: /admin_login/
- Admin Dashboard: /admin_dashboard/
- Add Book: /admin_add-book/
- Student Register: /student/register/
- Student Login: /student/login/
- View Books (Student): /student/books/

---

📝 Notes

- Admin and Student sessions are separate.
- Student can't access any admin functionality.
- Templates use a base.html layout.
- MySQL is used as backend DB.
