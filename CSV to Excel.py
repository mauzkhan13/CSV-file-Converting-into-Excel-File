import os
import pandas as pd

# Set the path to the directory containing the CSV files
csv_dir = r'C:\Users\Mauz Khan\Desktop'


# Set the path to the directory where the XML files will be saved
excel_dir = r'C:\Users\Mauz Khan\Desktop'

# Get a list of all the CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]


# Get a list of all the CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

# Loop through each CSV file and perform the conversion
for csv_file in csv_files:
    # Construct the full path to the CSV file
    csv_path = os.path.join(csv_dir, csv_file)
    
    # Read the CSV file using pandas
    df = pd.read_csv(csv_path)
    
    # Construct the full path to the output Excel file
    excel_file = os.path.splitext(csv_file)[0] + '.xlsx'
    excel_path = os.path.join(excel_dir, excel_file)
    
    # Write the DataFrame to the Excel file
    df.to_excel(excel_path, index=False)
