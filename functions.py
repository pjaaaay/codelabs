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

        logging.info(f"Email addresses generated and saved to {result_csv_file_path} and {result_tsv_file_path}")

        print(f"Email addresses generated and saved to {result_csv_file_path} and {result_tsv_file_path}")

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
