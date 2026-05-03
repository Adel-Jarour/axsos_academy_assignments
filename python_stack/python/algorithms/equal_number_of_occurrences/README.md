# Python Are Occurrences Equal Project

## Description

This solution checks whether all characters in a given string appear the same number of times. It uses a frequency-counting approach with a dictionary, then verifies that all counts are equal.

## Features

- Counts character occurrences efficiently using a dictionary
- Simple and readable implementation
- Works for any string input
- Time complexity: O(n)
- Includes multiple approaches (set-based and loop-based) for comparison

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
git sparse-checkout set python_stack/python/algorithms/equal_number_of_occurrences
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
