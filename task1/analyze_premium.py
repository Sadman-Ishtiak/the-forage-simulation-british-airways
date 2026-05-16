import pandas as pd

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")
df['PREMIUM_SEATS'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS']
df['TOTAL_SEATS'] = df['PREMIUM_SEATS'] + df['ECONOMY_SEATS']
df['PREMIUM_%'] = df['PREMIUM_SEATS'] / df['TOTAL_SEATS'] * 100

country_premium = df.groupby('ARRIVAL_COUNTRY').agg({
    'PREMIUM_%': 'mean',
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'TOTAL_SEATS': 'mean'
}).sort_values('PREMIUM_%', ascending=False)

print(country_premium)
