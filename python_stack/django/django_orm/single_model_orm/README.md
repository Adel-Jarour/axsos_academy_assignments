# Single Model ORM Project

A practical Django application focusing on core **CRUD (Create, Read, Update, Delete) operations** using Django's Object-Relational Mapper (ORM).

This project sets up a single-model database structure called **User** to demonstrate how Python objects are automatically translated into SQL queries by the Django ORM under the hood.

---

## 🚀 Features

- **Model Design:** A structured `User` model with attributes: `first_name`, `last_name`, `email_address`, `age`, and `created_at`.
- **Query Techniques:** Showcases practical query styles including:
  - Adding records (`create`)
  - Finding elements (`first()`, `last()`, `get()`)
  - Updating records (`save()`)
  - Deleting records (`delete()`)
  - Sorting data (`order_by()` in ascending/descending directions)

---

## 🛠️ Prerequisites

Ensure you have the following installed on your local computer:
- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

---

## 📥 How to Download and Setup

### 1. Clone the Repository
Clone the workspace:
```bash
git clone <repository_url>
cd <repository_folder>/python_stack/django/django_orm/single_model_orm
```

### 2. Set Up a Virtual Environment (Recommended)
Isolate this project's dependencies:
```bash
# Create virtual environment
python -m venv venv

# Activate it:
# On Windows (Command Prompt/PowerShell)
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Django
Install Django using pip:
```bash
pip install django
```

---

## ⚙️ How to Run the Project

### 1. Run Database Migrations
Set up your SQLite database structure by running migrations:
```bash
python manage.py migrate
```

### 2. Run the Development Server
Launch the server to check the app locally:
```bash
python manage.py runserver
```
Visit the server locally: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 3. Test ORM Queries in the Interactive Django Shell
To run the query commands located inside `quries.txt`:
```bash
python manage.py shell
```
Inside the shell, import your model and start querying:
```python
from users_app.models import User

# List all users
User.objects.all()

# Sort users by first name ascending
User.objects.all().order_by('first_name')
```

---

## 📁 Project Structure

- `single_model_orm/` - Main project directory containing configuration settings.
- `users_app/` - App directory containing the `User` model, migrations, and core application code.
- `manage.py` - Standard Django CLI tool for administrative tasks.
- `quries.txt` - Complete list of step-by-step query assignments executed for this project.
