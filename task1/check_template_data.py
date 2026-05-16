import pandas as pd

file_path = "Lounge Eligibility Lookup Template - Task 1.xlsx"
df = pd.read_excel(file_path, sheet_name="Lounge Eligibility Lookup Table", skiprows=10)
print("Data in Lounge Eligibility Lookup Table (skiprows=10):")
print(df)
