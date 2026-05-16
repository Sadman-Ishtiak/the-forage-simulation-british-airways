# Final Analysis Report: British Airways Lounge Eligibility

## 1. Project Overview
This report details the analysis of British Airways' summer schedule to determine lounge eligibility distributions for different customer loyalty tiers (Tier 1, Tier 2, and Tier 3). The objective was to identify logical groupings of flights to create a lookup table for lounge capacity planning.

## 2. Methodology & Code

### 2.1 Environment Setup
We used a Python virtual environment with `pandas` for data manipulation, `openpyxl` for Excel operations, and `scikit-learn` for exploratory clustering.

```python
# Setup commands
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl scikit-learn
```

### 2.2 Data Analysis Script
The following code was used to calculate the primary metrics for the groupings:

```python
import pandas as pd

# Load dataset
df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")
df['TOTAL_SEATS'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS'] + df['ECONOMY_SEATS']

# Calculate averages by Haul Type
haul_stats = df.groupby('HAUL').agg({
    'TIER1_ELIGIBLE_PAX': 'mean',
    'TIER2_ELIGIBLE_PAX': 'mean',
    'TIER3_ELIGIBLE_PAX': 'mean',
    'TOTAL_SEATS': 'mean'
})

# Convert to percentages of total capacity
haul_stats['T1_PCT'] = (haul_stats['TIER1_ELIGIBLE_PAX'] / haul_stats['TOTAL_SEATS']) * 100
haul_stats['T2_PCT'] = (haul_stats['TIER2_ELIGIBLE_PAX'] / haul_stats['TOTAL_SEATS']) * 100
haul_stats['T3_PCT'] = (haul_stats['TIER3_ELIGIBLE_PAX'] / haul_stats['TOTAL_SEATS']) * 100

print(haul_stats[['T1_PCT', 'T2_PCT', 'T3_PCT']])
```

## 3. Findings

### 3.1 Statistical Summary
| Metric | Short Haul (Avg) | Long Haul (Avg) |
| :--- | :--- | :--- |
| **Tier 1 Pax** | 0.62 | 0.59 |
| **Tier 2 Pax** | 7.92 | 8.00 |
| **Tier 3 Pax** | 30.33 | 30.56 |
| **Total Seats** | 180 | 291.8 |
| **Total Tier %** | **21.6%** | **13.5%** |

### 3.2 Analysis of Groupings
*   **Short Haul (Europe/Turkey)**: These flights use smaller aircraft (mostly A320s) but maintain a high absolute number of tier members. This results in a much higher density of lounge-eligible passengers per seat (21.6%).
*   **Long Haul (Global Hubs)**: While these flights use much larger aircraft (A380, B777, B787), the number of high-tier members does not scale proportionally with the increase in seats. The density of lounge eligibility is lower (13.5%), though the premium cabin percentage is higher.

## 4. Population of Lookup Table
The `Lounge Eligibility Lookup Template - Task 1.xlsx` file has been programmatically updated with the following data:

| Grouping | Example Destinations | Tier 1 % | Tier 2 % | Tier 3 % |
| :--- | :--- | :--- | :--- | :--- |
| **Short Haul** | Germany, Spain, Austria | 0.34% | 4.40% | 16.85% |
| **Long Haul** | USA, UAE, Japan | 0.20% | 2.74% | 10.47% |

## 5. Justification
1.  **Grouping Choice**: Flights were grouped by 'HAUL' because it is the strongest predictor of eligibility density.
2.  **Assumptions**: We assume the "eligible pax" counts are representative of historical lounge demand per flight.
3.  **Future Scalability**: By using percentages of total capacity, the model remains valid even if aircraft types are upgraded or downgraded on specific routes.
