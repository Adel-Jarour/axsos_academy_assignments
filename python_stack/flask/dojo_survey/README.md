# Python Flask Dojo Survey Project

## Description

A dynamic Flask web application that demonstrates how to handle HTML forms and HTTP POST requests. It captures user input from a stylized survey form, processes the data on the server side, and dynamically renders the submitted results on a separate page.

## Features

- **Form Handling:** Uses HTML forms with the `POST` method to securely transmit user input.
- **Data Retrieval:** Retrieves submitted data in the Flask backend using `request.form`.
- **Dynamic Rendering:** Passes captured data to Jinja2 templates (`render_template`) to display results.
- **Enhanced UI (Bonus):** Implements Bootstrap 5 and custom CSS for a responsive, modern, and polished card-based interface.
- **Extended Inputs (Bonus):** Includes multiple input types such as text fields, dropdowns, radio buttons, checkboxes, and textareas.

## Prerequisites

- Python 3.x installed on your system.

## Setup and Running the Project

To download only this project (dojo_survey) without cloning the entire repository:

### 1. Clone only this file

Open your terminal and run these two commands:

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
git sparse-checkout set python_stack/flask/dojo_survey
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

### 7. Install Requirements

Ensure Flask is installed:

```bash
pip install Flask
```

### 8. Run the Program

Once the virtual environment is activated, you can run the main server file:

```bash
python server.py
```

Navigate to `http://localhost:5000` in your browser.

### 9. Deactivate Virtual Environment

When you are done testing the application, you can deactivate the virtual environment by simply running:

```bash
deactivate
```
