# Import Libraries
import pandas as pd

# Import functions from the functions module
import functions

# pip install openpyxl efore running main.py

# Generate email addresses for students
email_addresses = functions.generate_email

# Saving Output Files as tsv and csn files
file_save = functions.process_file

# Gender Seperation
gender_seperation = functions.separate_students_by_gender

# Names with special characters
special_characters = functions.list_students_with_special_characters