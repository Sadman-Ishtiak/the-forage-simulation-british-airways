import pandas as pd

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")

print("TIER1_ELIGIBLE_PAX Value Counts:")
print(df['TIER1_ELIGIBLE_PAX'].value_counts().head(10))

print("\nTIER2_ELIGIBLE_PAX distribution:")
print(df['TIER2_ELIGIBLE_PAX'].describe())
