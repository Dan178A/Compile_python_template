# Compile_python_template
A template that can help you to compile your whole project at once instead of going one by one ✌️

This script compiles Python files and moves them, along with other specified files, to a `dist` directory while maintaining the directory structure.

## Prerequisites

- Python 3.x
- `shutil` (part of the Python Standard Library)

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. **Prepare the list of files and folders**: 
   - Modify the `files` list in the script to include the files and folders you want to process.
   - Example:
     ```python
     files = [
         'main.py',
         'icon.ico',
         'requirements.txt',
         ('UI', 'UI/'),  # Here you place the path of your folders
     ]
     ```

2. **Run the script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script using Python:
     ```sh
     python compiler.py
     ```

## How It Works

1. **Create the `dist` directory**:
   - The script checks if the `dist` directory exists. If not, it creates it.

2. **Process each file and folder**:
   - For each item in the `files` list:
     - If it's a folder, the script walks through the folder and processes each file.
     - If it's a file, the script processes it directly.

3. **Compile Python files**:
   - The script compiles Python files (`.py`) to bytecode (`.pyc`) and moves the compiled files to the `dist` directory, maintaining the directory structure.

4. **Move other files**:
   - The script moves non-Python files to the `dist` directory, maintaining the directory structure.

## Example

Given the following `files` list:
```python
files = [
    'main.py',
    'icon.ico',
    'requirements.txt',
    ('UI', 'UI/'),  # Here you place the path of your folders
]