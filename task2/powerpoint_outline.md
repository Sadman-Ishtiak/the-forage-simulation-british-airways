# PowerPoint Content Outline: British Airways Booking Prediction Analysis

## Slide 1: Title Slide
- **Title**: Proactive Customer Acquisition via Predictive Modeling
- **Subtitle**: Understanding Booking Drivers and Predicting Customer Intent
- **Presenter**: Gemini CLI Data Science Team
- **Image Idea**: British Airways Aircraft with Data Overlay

---

## Slide 2: Executive Summary
- **Goal**: Transition from reactive marketing to proactive customer engagement using Machine Learning.
- **Key Insight**: We can predict booking completion with **96% accuracy**.
- **Strategic Value**: By identifying high-intent customers early, we can optimize marketing spend and personalize offers.

---

## Slide 3: Who Wants Extra Luggage? (Ancillary Preferences I)
- **Key Findings**:
    - **Circle Trip** travelers are most likely to request extra baggage (**78%**), followed by **One-Way** (**71%**).
    - Customers booking via the **Internet** channel request baggage more often than those on **Mobile** (68% vs 60%).
- **Visualization**: `baggage_by_trip.png`
- **Recommendation**: Bundle baggage offers for multi-city/circle trip itineraries.

---

## Slide 4: Seat & Meal Preferences (Ancillary Preferences II)
- **Preferred Seats**: Most popular among families/groups (3-5 passengers) and **Round-Trip** travelers.
- **In-flight Meals**: Strongest demand on **Round-Trip** itineraries (**43%**). Interestingly, short-duration flights still show significant meal interest, suggesting a preference for convenience.
- **Visualization**: `seats_by_trip.png`
- **Recommendation**: Target "Preferred Seat" upsells to group bookings during the checkout flow.

---

## Slide 5: Profile of a Completed Booking
- **Top Markets**: **Malaysia** is our strongest converting market, followed by **Australia** and **China**.
- **Purchase Lead**: Booked flights have a slightly shorter average lead time (**80 days**) compared to unbooked searches (**86 days**), suggesting a "decisive window" for engagement.
- **Visualization**: `booking_lead_time.png`
- **Recommendation**: Focus "Last Minute" or "Decisive Window" marketing on the 60-80 day lead time range.

---

## Slide 6: Proposed Machine Learning Model
- **Algorithm**: **Random Forest Classifier**
    - Why? Handles non-linear relationships and provides clear **Feature Importance**.
- **Model Performance**:
    - **96% Accuracy** (Balanced)
    - **0.997 ROC-AUC Score**
- **Top Predictors**: Purchase Lead, Route, Flight Hour, and Booking Origin.
- **Implementation**: Real-time scoring of customer searches to trigger personalized email/ad campaigns.

---

## Slide 7: Next Steps & Strategic Recommendations
- **Market Expansion**: Investigate why Malaysia has such high conversion and replicate successful tactics in other regions.
- **Personalized Checkout**: Use the ML model to dynamically offer baggage or seat bundles to customers with a high "Predicted Booking Probability."
- **Lead Time Optimization**: Target customers specifically when they enter the 80-day purchase lead window.
