import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("customer_booking.csv", encoding="ISO-8859-1")

# Helper function for percentage breakdown
def get_pct_breakdown(column, target):
    return df.groupby(column)[target].mean().sort_values(ascending=False) * 100

# 1. Extra Baggage Analysis
print("--- Extra Baggage Preferences ---")
print(get_pct_breakdown('trip_type', 'wants_extra_baggage'))
print(get_pct_breakdown('sales_channel', 'wants_extra_baggage'))

# 2. Preferred Seats Analysis
print("\n--- Preferred Seat Preferences ---")
print(get_pct_breakdown('trip_type', 'wants_preferred_seat'))
print(get_pct_breakdown('num_passengers', 'wants_preferred_seat').head(5))

# 3. In-flight Meals Analysis
print("\n--- In-flight Meal Preferences ---")
print(get_pct_breakdown('trip_type', 'wants_in_flight_meals'))
print(get_pct_breakdown('flight_duration', 'wants_in_flight_meals').tail(5)) # Longer flights?

# 4. Successful Booking Characteristics
print("\n--- Successful Booking Characteristics ---")
# Top booking origins for completed bookings
top_origins = df[df['booking_complete'] == 1]['booking_origin'].value_counts().head(5)
print("Top Booking Origins for Completed Bookings:\n", top_origins)

# Average purchase lead for booked vs not booked
avg_lead = df.groupby('booking_complete')['purchase_lead'].mean()
print("\nAvg Purchase Lead (0=Not Booked, 1=Booked):\n", avg_lead)

# 5. Visualizations for Slides
plt.figure(figsize=(10, 6))
sns.barplot(x='trip_type', y='wants_extra_baggage', data=df, errorbar=None)
plt.title('Extra Baggage Requests by Trip Type')
plt.ylabel('Request Probability (%)')
plt.savefig('baggage_by_trip.png')

plt.figure(figsize=(10, 6))
sns.barplot(x='trip_type', y='wants_preferred_seat', data=df, errorbar=None)
plt.title('Preferred Seat Requests by Trip Type')
plt.ylabel('Request Probability (%)')
plt.savefig('seats_by_trip.png')

plt.figure(figsize=(10, 6))
sns.boxplot(x='booking_complete', y='purchase_lead', data=df)
plt.ylim(0, 300) # focus on bulk of data
plt.title('Purchase Lead Time: Booked vs Not Booked')
plt.savefig('booking_lead_time.png')
