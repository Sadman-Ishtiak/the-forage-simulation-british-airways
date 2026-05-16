import pandas as pd

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")

# Check unique countries per region
country_counts = df.groupby(['ARRIVAL_REGION', 'ARRIVAL_COUNTRY']).size().reset_index(name='COUNT')
print("Countries per region:")
print(country_counts)

# Let's see if there are countries with significantly different distributions
country_stats = df.groupby('ARRIVAL_COUNTRY').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean'
}).sort_values('TIER1_ELIGIBLE_PAX', ascending=False)

print("\nTop 10 Countries by Tier 1 Eligible Pax (Mean):")
print(country_stats.head(10))

# Maybe group by TIME_OF_DAY?
time_stats = df.groupby('TIME_OF_DAY').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean'
})
print("\nStats by TIME_OF_DAY:")
print(time_stats)
