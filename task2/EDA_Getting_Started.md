# Task 2

---

## Predictive modeling of customer bookings

This Jupyter notebook includes some code to get you started with this predictive modeling task. We will use various packages for data manipulation, feature engineering and machine learning.

### Exploratory data analysis

First, we must explore the data in order to better understand what we have and the statistical properties of the dataset.


```python
import pandas as pd
```


```python
df = pd.read_csv("data/customer_booking.csv", encoding="ISO-8859-1")
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_passengers</th>
      <th>sales_channel</th>
      <th>trip_type</th>
      <th>purchase_lead</th>
      <th>length_of_stay</th>
      <th>flight_hour</th>
      <th>flight_day</th>
      <th>route</th>
      <th>booking_origin</th>
      <th>wants_extra_baggage</th>
      <th>wants_preferred_seat</th>
      <th>wants_in_flight_meals</th>
      <th>flight_duration</th>
      <th>booking_complete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>Internet</td>
      <td>RoundTrip</td>
      <td>262</td>
      <td>19</td>
      <td>7</td>
      <td>Sat</td>
      <td>AKLDEL</td>
      <td>New Zealand</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>5.52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Internet</td>
      <td>RoundTrip</td>
      <td>112</td>
      <td>20</td>
      <td>3</td>
      <td>Sat</td>
      <td>AKLDEL</td>
      <td>New Zealand</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5.52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Internet</td>
      <td>RoundTrip</td>
      <td>243</td>
      <td>22</td>
      <td>17</td>
      <td>Wed</td>
      <td>AKLDEL</td>
      <td>India</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5.52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Internet</td>
      <td>RoundTrip</td>
      <td>96</td>
      <td>31</td>
      <td>4</td>
      <td>Sat</td>
      <td>AKLDEL</td>
      <td>New Zealand</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>5.52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>Internet</td>
      <td>RoundTrip</td>
      <td>68</td>
      <td>22</td>
      <td>15</td>
      <td>Wed</td>
      <td>AKLDEL</td>
      <td>India</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>5.52</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



The `.head()` method allows us to view the first 5 rows in the dataset, this is useful for visual inspection of our columns


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 50000 entries, 0 to 49999
    Data columns (total 14 columns):
     #   Column                 Non-Null Count  Dtype  
    ---  ------                 --------------  -----  
     0   num_passengers         50000 non-null  int64  
     1   sales_channel          50000 non-null  object 
     2   trip_type              50000 non-null  object 
     3   purchase_lead          50000 non-null  int64  
     4   length_of_stay         50000 non-null  int64  
     5   flight_hour            50000 non-null  int64  
     6   flight_day             50000 non-null  object 
     7   route                  50000 non-null  object 
     8   booking_origin         50000 non-null  object 
     9   wants_extra_baggage    50000 non-null  int64  
     10  wants_preferred_seat   50000 non-null  int64  
     11  wants_in_flight_meals  50000 non-null  int64  
     12  flight_duration        50000 non-null  float64
     13  booking_complete       50000 non-null  int64  
    dtypes: float64(1), int64(8), object(5)
    memory usage: 5.3+ MB


The `.info()` method gives us a data description, telling us the names of the columns, their data types and how many null values we have. Fortunately, we have no null values. It looks like some of these columns should be converted into different data types, e.g. flight_day.

To provide more context, below is a more detailed data description, explaining exactly what each column means:

- `num_passengers` = number of passengers travelling
- `sales_channel` = sales channel booking was made on
- `trip_type` = trip Type (Round Trip, One Way, Circle Trip)
- `purchase_lead` = number of days between travel date and booking date
- `length_of_stay` = number of days spent at destination
- `flight_hour` = hour of flight departure
- `flight_day` = day of week of flight departure
- `route` = origin -> destination flight route
- `booking_origin` = country from where booking was made
- `wants_extra_baggage` = if the customer wanted extra baggage in the booking
- `wants_preferred_seat` = if the customer wanted a preferred seat in the booking
- `wants_in_flight_meals` = if the customer wanted in-flight meals in the booking
- `flight_duration` = total duration of flight (in hours)
- `booking_complete` = flag indicating if the customer completed the booking

Before we compute any statistics on the data, lets do any necessary data conversion


```python
df["flight_day"].unique()
```




    array(['Sat', 'Wed', 'Thu', 'Mon', 'Sun', 'Tue', 'Fri'], dtype=object)




```python
mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}

df["flight_day"] = df["flight_day"].map(mapping)
```


```python
df["flight_day"].unique()
```




    array([6, 3, 4, 1, 7, 2, 5])




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_passengers</th>
      <th>purchase_lead</th>
      <th>length_of_stay</th>
      <th>flight_hour</th>
      <th>flight_day</th>
      <th>wants_extra_baggage</th>
      <th>wants_preferred_seat</th>
      <th>wants_in_flight_meals</th>
      <th>flight_duration</th>
      <th>booking_complete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.00000</td>
      <td>50000.00000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.591240</td>
      <td>84.940480</td>
      <td>23.04456</td>
      <td>9.06634</td>
      <td>3.814420</td>
      <td>0.668780</td>
      <td>0.296960</td>
      <td>0.427140</td>
      <td>7.277561</td>
      <td>0.149560</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.020165</td>
      <td>90.451378</td>
      <td>33.88767</td>
      <td>5.41266</td>
      <td>1.992792</td>
      <td>0.470657</td>
      <td>0.456923</td>
      <td>0.494668</td>
      <td>1.496863</td>
      <td>0.356643</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>4.670000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>21.000000</td>
      <td>5.00000</td>
      <td>5.00000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>5.620000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>51.000000</td>
      <td>17.00000</td>
      <td>9.00000</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>7.570000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>115.000000</td>
      <td>28.00000</td>
      <td>13.00000</td>
      <td>5.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>8.830000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.000000</td>
      <td>867.000000</td>
      <td>778.00000</td>
      <td>23.00000</td>
      <td>7.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>9.500000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



The `.describe()` method gives us a summary of descriptive statistics over the entire dataset (only works for numeric columns). This gives us a quick overview of a few things such as the mean, min, max and overall distribution of each column.

From this point, you should continue exploring the dataset with some visualisations and other metrics that you think may be useful. Then, you should prepare your dataset for predictive modelling. Finally, you should train your machine learning model, evaluate it with performance metrics and output visualisations for the contributing variables. All of this analysis should be summarised in your single slide.


