# British Airways Data Science Project

This project focuses on providing data-driven insights and predictive modeling to enhance British Airways' customer experience and booking conversion rates. It is divided into two main tasks: **Lounge Eligibility Analysis** and **Customer Booking Prediction**.

## Project Overview

### Task 1: Lounge Eligibility & Summer Schedule Analysis
Optimized the lounge eligibility lookup process by analyzing the summer flight schedule to categorize flights by haul type (Short vs. Long) and calculating tier-based access percentages.

*   **Key Achievement**: Developed an automated method to populate the Lounge Eligibility Lookup Table based on historical capacity and haul-type distributions.
*   **Insights**: Short-haul flights represent a higher density of Tier 3 travelers (16.85%), while Long-haul flights maintain a more exclusive Tier 1 distribution (0.20%).

### Task 2: Customer Booking Prediction
Built a high-performance machine learning model to predict whether a customer will complete a holiday booking based on their behavior and trip preferences.

*   **Model**: Random Forest Classifier with Minority Oversampling.
*   **Performance**: 
    - **Balanced Accuracy**: 96.2%
    - **ROC-AUC**: 0.997
*   **Key Predictors**: Purchase Lead Time, Route, and Flight Hour.

## Project Structure

```text
.
├── task1/                          # Lounge Eligibility Task
│   ├── British Airways Summer Schedule...xlsx  # Raw schedule data
│   ├── Lounge Eligibility Lookup...xlsx        # Finalized template
│   ├── populate_template.py         # Automation script for Excel
│   └── final_analysis_report.md     # Technical documentation
├── task2/                          # Booking Prediction Task
│   ├── customer_booking.csv         # Raw customer data
│   ├── improve_model.py             # ML pipeline (Training & Evaluation)
│   ├── booking_analysis_summary.md  # Executive summary of ML findings
│   ├── powerpoint_outline.md        # Presentation structure
│   └── Booking_Prediction_Summary.pptx # Final executive slide
├── venv/                            # Python virtual environment
└── requirements.txt                 # Project dependencies
```

## Key Findings & Business Insights

### 1. Booking Drivers
Customers who successfully book their holidays typically do so **80 days in advance** on average. In contrast, non-converting customers have a slightly longer lead time (86 days), suggesting a specific "conversion window" where customers are most decisive.

### 2. Ancillary Service Preferences
*   **Extra Baggage**: Highest demand comes from **Circle Trips (78%)**, followed by One-way trips (71%).
*   **Preferred Seats**: Groups of 3-5 passengers show a significant increase in seat selection preference compared to solo travelers.
*   **In-flight Meals**: Round-trip travelers are the most likely to pre-book meals (43%).

### 3. Top Markets
The highest volume of successful bookings originates from **Malaysia**, **Australia**, and **China**.

## Setup and Reproducibility

1.  **Environment Setup**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2.  **Run Prediction Model**:
    ```bash
    python task2/improve_model.py
    ```

3.  **Generate PowerPoint Slide**:
    ```bash
    python task2/generate_slide.py
    ```

## Technologies Used
*   **Data Analysis**: Python, Pandas, Openpyxl
*   **Machine Learning**: Scikit-Learn (Random Forest, SMOTE-style resampling)
*   **Visualization**: Matplotlib, Seaborn
*   **Reporting**: Python-pptx, Markdown

---
*Developed as part of the British Airways Data Science Virtual Internship.*
