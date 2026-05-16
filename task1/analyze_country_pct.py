import pandas as pd

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")
df['TOTAL_SEATS'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS'] + df['ECONOMY_SEATS']

country_pct = df.groupby('ARRIVAL_COUNTRY').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'TOTAL_SEATS': 'mean'
})

country_pct['T1_%'] = country_pct['TIER1_ELIGIBLE_PAX'] / country_pct['TOTAL_SEATS'] * 100
country_pct['T2_%'] = country_pct['TIER2_ELIGIBLE_PAX'] / country_pct['TOTAL_SEATS'] * 100
country_pct['T3_%'] = country_pct['TIER3_ELIGIBLE_PAX'] / country_pct['TOTAL_SEATS'] * 100

print(country_pct[['T1_%', 'T2_%', 'T3_%']].sort_values('T3_%', ascending=False))
