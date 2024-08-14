import pandas as pd
# Load the data from the provided CSV file into a DataFrame
file_path = "Employees.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)
# 1. Remove any duplicates in the table
df = df.drop_duplicates()
# 2. Remove any decimal places in the Age column
df['Age'] = df['Age'].astype(int)
# 3. Convert the USD salary to EGP (assuming a conversion rate, for example, 1 USD = 49 EGP)
conversion_rate = 49
df['Salary(EGP)'] = df['Salary(USD)'] * conversion_rate
# 4. Print some stats in the console
# Average age
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")
# Median Salaries (in EGP)
median_salary = df['Salary(EGP)'].median()
print(f"Median Salary (EGP): {median_salary}")
# Ratio between males and female employees
gender_counts = df['Gender'].value_counts()
male_female_ratio = gender_counts['Male'] / gender_counts['Female'] if 'Female' in gender_counts else "No female employees"
print(f"Male to Female Ratio: {male_female_ratio}")
# 5. Write the processed data to a new CSV file
output_file_path = "processed_data.csv"
df.to_csv(output_file_path, index=False)
print(f"Processed data saved to {output_file_path}")