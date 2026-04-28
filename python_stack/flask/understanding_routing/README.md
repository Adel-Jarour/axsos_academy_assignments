# Python Flask Understanding Route Project

## Description

This project explores the core routing capabilities of the Flask framework, focusing on how to handle different types of URLs, variable parameters, and custom error pages.

## Features

- **Static Routing:** Simple route handling for fixed responses (e.g., `/champion`).
- **Variable Rules:** Dynamic routing using string variables to personalize responses (e.g., `/say/<name>`).
- **Typed Path Parameters:** URL logic with type conversion, such as repeating a word a specific number of times (e.g., `/repeat/<int:num>/<word>`).
- **Custom Error Handling:** Implementation of a custom 404 error page to guide users when they visit an undefined route.

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
git sparse-checkout set python_stack/flask/understanding_routing
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
