# Python Flask Checkerboard Project

## Description

A dynamic Flask web application that demonstrates the use of Jinja2 templates and URL routing parameters to render an interactive checkerboard grid on a webpage.

## Features

- **Dynamic Grid Rendering:** Render a checkerboard grid with a customizable number of rows and columns based on URL parameters.
- **Customizable Colors:** Pass color names in the URL to dynamically change the alternating colors of the checkerboard.
- **Multiple Routing Levels:** Supports `/`, `/<x>`, `/<x>/<y>`, and `/<x>/<y>/<color1>/<color2>` patterns to explore different layouts and color schemes.

## Prerequisites

- Python 3.x installed on your system.

## Setup and Running the Project

To download only this project (checkerboard) without cloning the entire repository:

### 1. Clone only this repository

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
git sparse-checkout set python_stack/flask/checkerboard
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

### 7. Install Dependencies

Install the required dependencies such as Flask:

```bash
pip install Flask
```

### 8. Run the Program

Once the virtual environment is activated and dependencies are installed, you can run the main server file:

```bash
python app.py
```

### 9. Deactivate Virtual Environment

When you are done testing the application, you can deactivate the virtual environment by simply running:

```bash
deactivate
```
