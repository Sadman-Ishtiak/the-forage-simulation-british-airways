# Data Analysis Report: British Airways Lounge Eligibility

## 1. Overview
The analysis focused on two datasets: the Summer Schedule (10,000 flights) and a Lounge Eligibility Template. The goal was to identify meaningful groupings of flights/passengers to determine lounge eligibility distributions for different customer tiers.

## 2. Key Findings
- **Tier 1 (highest loyalty)**: Very rare, averaging ~0.6 passengers per flight. Most flights have 0 or 1 Tier 1 passenger.
- **Tier 2**: Moderately common, averaging ~8 passengers per flight.
- **Tier 3**: Most common tier, averaging ~30 passengers per flight.
- **Seat Correlation**: Surprisingly, the number of eligible passengers does not correlate strongly with the total number of seats. A320s (Short Haul) and A380s (Long Haul) have almost the same number of tier members on average.

## 3. Proposed Groupings

### Group A: Short Haul (Europe)
- **Characteristics**: Flights within Europe/Turkey, smaller aircraft (A320), fewer premium seats (~5-6%).
- **Eligibility Density**: High percentage of total passengers are tier members (~21% total).
- **Averages**: 0.34% Tier 1, 4.4% Tier 2, 16.9% Tier 3.

### Group B: Long Haul (Global Hubs)
- **Characteristics**: Flights to USA, Japan, UAE. Larger aircraft (A380, B777, B787), high premium seat mix (~17-18%).
- **Eligibility Density**: Lower percentage of total passengers are tier members (~13% total), partly due to larger total capacity.
- **Averages**: 0.20% Tier 1, 2.7% Tier 2, 10.4% Tier 3.

## 4. Clustering Analysis
Using K-Means clustering, we identified 4 distinct profiles across all regions:
1. **Tier 1 Heavy**: Flights with multiple Tier 1 members.
2. **Standard High Density**: Average distribution across all tiers.
3. **Premium Dense**: High counts of Tier 2 and Tier 3 members.
4. **Leisure/Low Density**: Fewer than average tier members.

## 5. Recommendations for the Lookup Table
- Use **Haul Type** as the primary grouping factor.
- Consider adding a **Time of Day** factor if scheduling lounge staffing, although Tier distribution is relatively stable across morning/afternoon/evening.
