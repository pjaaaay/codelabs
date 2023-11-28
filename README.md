# codelabs (Student Data Processing Project)

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

## Installation

1. Clone the repository on your local machine.

 ```sh 
   git clone https://github.com/mikemwai/codelabs.git
 ```

2. Navigate to the project directory and create a virtual environment on your local machine through the command line: 

 ```sh 
   py -m venv myenv
 ```

3. Activate your virtual environment:

  - On Windows:

 ```sh 
   myenv\Scripts\activate
 ```

  - On Mac:

 ```sh 
   source myenv/bin/activate
 ```

4. Install project dependencies on your virtual environment:

 ```sh
   pip install -r requirements.txt
 ```

## Usage

1. Run main.py to process the data.
2. Check the generated files in the "output" folder in the root directory.

## Contributing

If you'd like to contribute to this project:
- Please fork the repository
- Create a new branch for your changes
- Submit a [pull request](https://github.com/mikemwai/codelabs/pulls) 

Contributions, bug reports, and feature requests are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
