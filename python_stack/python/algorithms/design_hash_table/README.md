# Python Design HashMap Project

## Description

A low-level implementation of a HashMap data structure in Python, built from scratch to understand the internal mechanics of key-value storage and collision resolution.

## Features

- **Custom Hashing Logic:** Implementation of a hash function to calculate indices for keys.
- **Collision Resolution:** Uses **Linear Probing** (open addressing) to handle cases where multiple keys hash to the same index.
- **Core Operations:** Includes standard HashMap methods like `put` (insert/update), `get` (retrieve), and `remove`.
- **State Visualization:** A `display` method to visualize the internal array structure and bucket contents.

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
git sparse-checkout set python_stack/python/algorithms/design_hash_table
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
