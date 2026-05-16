import pandas as pd

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")

aircraft_stats = df.groupby('AIRCRAFT_TYPE').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'FIRST_CLASS_SEATS': 'mean',
    'BUSINESS_CLASS_SEATS': 'mean',
    'ECONOMY_SEATS': 'mean'
})

print("Stats by AIRCRAFT_TYPE:")
print(aircraft_stats)
