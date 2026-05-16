import pandas as pd
import os

files = [
    "Lounge Eligibility Lookup Template - Task 1.xlsx",
    "British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx"
]

for file in files:
    print(f"\n--- Analyzing file: {file} ---")
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue
    
    xl = pd.ExcelFile(file)
    print(f"Sheets: {xl.sheet_names}")
    
    for sheet in xl.sheet_names:
        print(f"\nSheet: {sheet}")
        # Read first 20 rows to find headers
        df = pd.read_excel(file, sheet_name=sheet, header=None, nrows=20)
        print("First 20 rows (no header):")
        print(df)
        print("-" * 20)
