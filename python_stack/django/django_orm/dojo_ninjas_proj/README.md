# Dojo Ninjas Project

A simple and elegant Django application showcasing **One-to-Many relationships** using Django's Object-Relational Mapper (ORM).

This project models the relationship between **Dojos** and **Ninjas**. A single Dojo can host multiple Ninjas, while each Ninja belongs to exactly one Dojo.

---

## 🚀 Features

- **Models & Relationships:** Implements a One-to-Many (`ForeignKey`) database relationship.
- **Django ORM queries:** Demonstrate database population, querying, updating, and deletion via python scripts/shell.
- **Representations:** Clean string/representation outputs for both models.

---

## 🛠️ Prerequisites

To run this project, make sure you have the following installed on your machine:
- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

---

## 📥 How to Download and Setup

### 1. Clone the Repository
Clone this workspace from your git provider:
```bash
git clone <repository_url>
cd <repository_folder>/python_stack/django/django_orm/dojo_ninjas_proj
```

### 2. Set Up a Virtual Environment (Recommended)
Creating a virtual environment isolates project dependencies:
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
Install the Django framework:
```bash
pip install django
```

---

## ⚙️ How to Run the Project

### 1. Database Migrations
If you've just cloned the project and need to set up the database tables:
```bash
python manage.py migrate
```

### 2. Start the Development Server
To run the server and view it in your browser:
```bash
python manage.py runserver
```
Visit the local server URL in your browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 3. Run ORM Queries in the Django Shell
This project includes a list of queries in `quries.txt`. To test and execute these commands within the Django Shell environment:
```bash
python manage.py shell
```
Inside the interactive shell, you can import the models and run queries:
```python
from dojo_ninjas_app.models import Dojo, Ninja

# Retrieve all Dojos
Dojo.objects.all()

# Retrieve all Ninjas
Ninja.objects.all()
```

---

## 📁 Project Structure

- `dojo_ninjas_proj/` - Project settings and configuration.
- `dojo_ninjas_app/` - App directory containing database models, migrations, views, and routes.
- `manage.py` - Django command-line utility for administrative tasks.
- `quries.txt` - Complete collection of assignment-required shell queries for quick reference.
