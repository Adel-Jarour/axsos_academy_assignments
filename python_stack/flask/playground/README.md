# Python Flask Playground Project

## Description

A dynamic Flask web application that demonstrates the use of Jinja2 templates and URL routing parameters to render interactive elements on a webpage.

## Features

- **Dynamic Box Rendering:** Render a specific number of boxes based on the URL parameter.
- **Customizable Colors:** Pass a color name in the URL to change the background color of the rendered boxes.
- **Interactive UI:** Premium design with Flexbox layout and hover animations for an enhanced user experience.
- **Multiple Routing Levels:** Supports `/play`, `/play/<num>`, and `/play/<num>/<color>` patterns.

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
git sparse-checkout set python_stack/flask/playground
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
