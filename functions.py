import pandas as pd
import re
import os
import logging

# Specify the output folder
output_folder = 'output'

# Ensure the output folder exists, create it if it doesn't
os.makedirs(output_folder, exist_ok=True)

# Configure logging and specify the log file path under the output folder
log_file_path = os.path.join(output_folder, 'computation_log.txt')
logging.basicConfig(filename=log_file_path, level=logging.INFO)

# Lists to store male and female students
male_students = []
female_students = []

# List to store students with special characters
students_with_special_characters = []

# Function to generate email addresses
def generate_email(name):
    cleaned_name = re.sub(r'[^a-zA-Z\s]', '', name)
    name_parts = cleaned_name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        email = f"{first_name[0].lower()}{last_name.lower()}@gmail.com"
    else:
        email = f"{name_parts[0].lower()}@gmail.com"
    return email

# Function to separate students based on gender
def separate_students_by_gender(df):
    male_students.clear()
    female_students.clear()

    for index, row in df.iterrows():
        gender = row['Gender']
        student_name = row['Student Name']

        # Separate students based on gender and add their names to the respective lists
        if gender == 'M':
            male_students.append(student_name)
        elif gender == 'F':
            female_students.append(student_name)

# Function to list students with special characters using regex
def list_students_with_special_characters(df):
    students_with_special_characters.clear()

    for index, row in df.iterrows():
        student_name = row['Student Name']

        # Check if the student name contains special characters using regex
        if re.search(r'[^a-zA-Z\s]', student_name):
            students_with_special_characters.append(student_name)

# Function to process a file and save the result
def process_file(file_path, output_folder):
    try:
        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Create a list of dictionaries containing student names and email addresses
        email_data = []
        for index, row in df.iterrows():
            no = row['No.']
            student_number = row['Student Number']
            student_name = row['Student Name']

            # Parse the "DoB" column as a date
            dob = pd.to_datetime(row['DoB'], format='%Y-%m-%d', errors='coerce')
            if pd.notna(dob):
                dob = dob.strftime('%Y-%m-%d')

            email_address = generate_email(student_name)
            gender = row['Gender']

            email_data.append({'No.': no, 'Student Number': student_number, 'Student Name': student_name, 'DoB': dob, 'Email Address': email_address, 'Gender': gender})

        # Create a new DataFrame from the list of dictionaries
        result_df = pd.DataFrame(email_data)

        # Remove duplicate email addresses
        result_df = result_df.drop_duplicates(subset=['Email Address'])

        # Get the filename without the extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Specify the result file names and paths
        result_csv_file_name = f'output-{file_name}.csv'
        result_csv_file_path = os.path.join(output_folder, result_csv_file_name)

        result_tsv_file_name = f'output-{file_name}.tsv'
        result_tsv_file_path = os.path.join(output_folder, result_tsv_file_name)

        # Save the result to CSV and TSV files under the 'output' folder
        result_df.to_csv(result_csv_file_path, index=False)
        result_df.to_csv(result_tsv_file_path, index=False, sep='\t')

        # Log the counts of male and female students
        separate_students_by_gender(df)
        logging.info(f"Email addresses generated and saved to {result_csv_file_path} and {result_tsv_file_path}")
        logging.info(f"Number of Male Students: {len(male_students)}")
        logging.info(f"Number of Female Students: {len(female_students)}")

        # List students with special characters
        list_students_with_special_characters(df)
        logging.info(f"Students with special characters: {', '.join(students_with_special_characters)}")

    except Exception as e:
        # Log errors
        logging.error(f"Error processing file {file_path}: {str(e)}")
        print(f"Error processing file {file_path}: {str(e)}")

# Process the first file
file_path_3B = 'test-files-3B.xlsx'
process_file(file_path_3B, output_folder)

# Process the second file
file_path_3C = 'test-files-3C.xlsx'
process_file(file_path_3C, output_folder)
