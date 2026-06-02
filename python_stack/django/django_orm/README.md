# Django ORM Projects Workspace

Welcome to the **Django ORM Assignments** repository folder! This workspace contains two fundamental hands-on Django projects designed to master relational modeling and basic CRUD database operations using Django's powerful Object-Relational Mapper (ORM).

---

## 📁 Projects in this Workspace

Explore the links below to find detailed setup and execution instructions for each project:

### 1. 🥷 [Dojo Ninjas Project](./dojo_ninjas_proj/README.md)
* **Description:** A project demonstrating **One-to-Many relationships** using foreign keys. Models a relationship where `Dojos` contain multiple `Ninjas`.
* **Key Learning:** Database relationships, cascading deletes, querying related models via `related_name`.

### 2. 👤 [Single Model ORM Project](./single_model_orm/README.md)
* **Description:** A foundational project showcasing core database operations (**CRUD**) on a single `User` model.
* **Key Learning:** Record creation, reading with filters/orders, updating fields, deleting entries, and working inside the Django shell environment.

---

## 🛠️ General Setup Instructions

To get started with any of the projects, perform the following global setup:

### 1. Prerequisites
Ensure you have **Python 3.x** installed.

### 2. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>/python_stack/django/django_orm
```

### 3. Create & Activate Virtual Environment
```bash
# Create environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### 4. Install Django
```bash
pip install django
```

---

*For detailed, step-by-step instructions on running the migrations, starting servers, or executing specific database queries, please navigate to the respective project directories.*
