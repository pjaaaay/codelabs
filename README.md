# Student Data Processing Project

## Overview

The Student Data Processing Project is a Python-based data processing and analysis project designed to handle student data and perform various operations on it. This README.md file provides an overview of the project, its purpose, and instructions on how to use it.

## Purpose

The purpose of this project is to:

- Parse an Excel file containing student data.
- Generate unique email addresses for students.
- Remove special characters from email addresses.
- Perform data analysis, including categorizing students by gender and identifying similarities in student names.
- Create backup files on Google Drive for data security.

## Prerequisites
- Python version 3.11.5 installed on your system.

# Installation

1. Fork the project to create a copy of the project in your own Github account.
2. Clone the repository to your local machine:
 
 ```sh 
  https://github.com/mikemwai/codelabs.git
 ```

3. Navigate to the project directory and create a virtual environment on your local machine: 

 ```sh 
  python3 -m venv myenv
 ```

4. Activate youur virtual environment:
On Windows:

 ```sh 
  myenv\Scripts\activate
 ```

 On Mac:

 ```sh 
  source myenv/bin/activate
 ```

5. Install project dependencies:

  ```sh
    pip install -r requirements.txt
  ```

# Usage

1. Run the script to process the data on your IDE's command line:

```sh
python main.py
```

2. Check the generated files in the "output" folder.

# Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch for your changes, and submit a pull request. Contributions, bug reports, and feature requests are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
