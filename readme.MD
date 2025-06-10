# Django GPA Calculator

This is a Django-based GPA calculator that allows users to register, log in, and manage their classes to calculate their GPA. The app leverages Django's built-in authentication system to securely manage user accounts and associate each user's classes and grades with their profile.

---

## Features
- User registration and login using Django's default `auth` system
- Add, edit, and delete classes with course names, credit hours, and grades
- GPA calculation based on user-entered data
- User-specific data isolation (each user sees only their own classes and GPA)

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (optional but recommended)

### Installation
```bash
# Clone the repository
$ git clone https://github.com/yourusername/gpa-calculator-django.git
$ cd gpa-calculator-django

# Create a virtual environment
$ python -m venv env
$ source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
$ pip install -r requirements.txt

# Apply migrations
$ python manage.py migrate

# Create a superuser (optional)
$ python manage.py createsuperuser

# Run the development server
$ python manage.py runserver
```

Then open your browser and go to `http://127.0.0.1:8000`.

---

## How It Works

### Authentication
This project uses Django's built-in `User` model from `django.contrib.auth` for authentication. Users can register for an account, log in, and log out. Authentication views are handled using Django's `LoginView`, `LogoutView`, and `UserCreationForm`.

### GPA Logic
Each user has access to their own dashboard, where they can:
- Add new courses (course name, credit hours, and letter grade)
- Edit or delete existing courses
- View their GPA, which is calculated using a weighted average based on the credit hours and grade points (A = 4.0, B = 3.0, etc.)

Classes are stored in a model that includes a foreign key to the user, ensuring that each user's data is private and secure.

---

## Project Structure
```
gpa_calculator/
├── gpa_calculator/       # Main project settings
├── core/                 # Core app with models, views, forms, etc.
├── templates/            # HTML templates for pages
├── static/               # Static files (CSS, JS)
├── db.sqlite3            # Default SQLite DB (changeable)
├── manage.py             # Django entry point
└── requirements.txt      # Python dependencies
```

---

## License
MIT License. See `LICENSE` file for more info.
