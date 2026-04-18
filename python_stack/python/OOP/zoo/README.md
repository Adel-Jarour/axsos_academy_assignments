# Python OOP Zoo Project

## Description

This is a simple Python project demonstrating Object-Oriented Programming (OOP) concepts such as classes, inheritance, and polymorphism. The project models a Zoo with different kinds of animals (Lion, Bear, Snake) that can be added to the zoo, displayed, and fed.

## Features

- **Animal Base Class and Subclasses:** Demonstrates creating specific animal classes extending a general behavior.
- **Zoo Management:** A main `Zoo` class that manages a collection of animals (adding, feeding, and displaying their status).
- **Object Interaction:** Feeding an animal affects its health/happiness attributes through method calls.

## Prerequisites

- Python 3.x installed on your system.

## Setup and Running the Project

To download only this project (zoo) without cloning the entire repository:

### 1. Clone only this file

Open your terminal and run these two command:

```bash
git clone --no-checkout https://github.com/Adel-Jarour/axsos_academy_assignments.git
cd axsos_academy_assignments
```

### 2. Enable sparse checkout

```bash
git sparse-checkout init --cone
```

### 3. Specify the folder path

```bash
git sparse-checkout set python_stack/python/OOP/zoo
```

### 4. Checkout files

```bash
git checkout
```

### 5. Create a Virtual Environment

Run the following command to create a virtual environment:

```bash
python -m venv venv
```

### 6. Activate the Virtual Environment

- **On Windows:**
  ```cmd
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 7. Run the Program

Once the virtual environment is activated, you can run the main simulation file:

```bash
python zoo.py
```

### 8. Deactivate Virtual Environment

When you are done testing the application, you can deactivate the virtual environment by simply running:

```bash
deactivate
```
