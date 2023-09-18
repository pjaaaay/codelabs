import pandas as pd
import re

# Load the Excel file into a DataFrame
file_path = 'TestFiles.xlsx'
df = pd.read_excel(file_path)

# Create empty lists to store student names and email addresses
students_with_special_chars = []

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

# Create a list of dictionaries containing student names and email addresses
email_data = []
for index, row in df.iterrows():
    student_name = row['Student Name']
    email_address = generate_email(student_name)
    email_data.append({'Student Name': student_name, 'Email Address': email_address})

# Create a new DataFrame from the list of dictionaries
result_df = pd.DataFrame(email_data)

# Remove duplicate email addresses
result_df = result_df.drop_duplicates(subset=['Email Address'])

# Save the result to a new Excel file
result_file_path = 'student_emails.xlsx'
result_df.to_excel(result_file_path, index=False)

print("Email addresses generated and saved to", result_file_path)
