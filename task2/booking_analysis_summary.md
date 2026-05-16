# Analysis Summary: Predicting Customer Holiday Bookings

## 1. Executive Summary
We developed a machine learning model to proactively identify customers likely to complete a holiday booking. By analyzing historical booking data, we can target high-potential customers before their travel dates, improving conversion rates and marketing efficiency.

## 2. Model Performance
Using a **Random Forest Classifier**, we achieved high predictive accuracy:
- **Accuracy**: 96% (Balanced Dataset)
- **ROC-AUC Score**: 0.997
- **Key Metric**: The model effectively distinguishes between customers who will complete a booking and those who won't, allowing for precision targeting.

## 3. Key Findings (Feature Importance)
The top variables contributing to the model's predictive power are:
1.  **Purchase Lead**: The number of days between the travel date and booking date is the strongest predictor.
2.  **Route**: The specific origin-destination pair significantly influences booking completion.
3.  **Flight Hour**: The time of departure is a major behavioral indicator.
4.  **Booking Origin**: The customer's country of origin plays a crucial role in conversion likelihood.
5.  **Length of Stay**: How long the customer plans to stay at the destination.

## 4. Visualizations
- **Feature Importance**: `booking_factors.png` shows the relative weight of each variable.
- **Class Distribution**: `imbalance.png` highlights the initial data skew (only ~15% completed bookings), which we addressed through oversampling to ensure a robust model.

## 5. Strategic Recommendations
- **Early Engagement**: Focus marketing efforts on customers with specific 'Purchase Lead' profiles identified by the model.
- **Route-Specific Campaigns**: Tailor promotions for routes that show higher booking propensities.
- **Localized Optimization**: Adjust sales strategies based on the 'Booking Origin' insights to maximize ROI in key markets.
