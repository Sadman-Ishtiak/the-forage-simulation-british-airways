import pandas as pd

# Load the dataset
file_path = "British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx"
df = pd.read_excel(file_path)

# Calculate percentage of eligible passengers for each tier relative to total seats or something?
# Actually, the template has "Tier 1 %", "Tier 2 %", "Tier 3 %". 
# This might mean what percentage of passengers in that group are eligible for each tier.
# Or it could be the percentage of eligible passengers who actually use the lounge?
# Given it's a "Lounge Eligibility Lookup Table", it's probably about eligibility.

# Let's see the total seats vs eligible passengers
df['TOTAL_SEATS'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS'] + df['ECONOMY_SEATS']

# Basic stats by HAUL
haul_stats = df.groupby('HAUL').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'TOTAL_SEATS': 'mean'
})

print("Stats by HAUL:")
print(haul_stats)

# Basic stats by ARRIVAL_REGION
region_stats = df.groupby('ARRIVAL_REGION').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'TOTAL_SEATS': 'mean'
})

print("\nStats by ARRIVAL_REGION:")
print(region_stats)

# Let's calculate the percentage of eligible passengers per flight
df['TIER1_PCT'] = df['TIER1_ELIGIBLE_PAX'] / df['TOTAL_SEATS']
df['TIER2_PCT'] = df['TIER2_ELIGIBLE_PAX'] / df['TOTAL_SEATS']
df['TIER3_PCT'] = df['TIER3_ELIGIBLE_PAX'] / df['TOTAL_SEATS']

haul_pct_stats = df.groupby('HAUL').agg({
    'TIER1_PCT': 'mean',
    'TIER2_PCT': 'mean',
    'TIER3_PCT': 'mean'
})

print("\nAverage Tier % by HAUL:")
print(haul_pct_stats)

region_pct_stats = df.groupby('ARRIVAL_REGION').agg({
    'TIER1_PCT': 'mean',
    'TIER2_PCT': 'mean',
    'TIER3_PCT': 'mean'
})

print("\nAverage Tier % by ARRIVAL_REGION:")
print(region_pct_stats)
