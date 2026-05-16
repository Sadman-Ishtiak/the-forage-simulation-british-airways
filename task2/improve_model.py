import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import resample

# 1. Load the data
df = pd.read_csv("customer_booking.csv", encoding="ISO-8859-1")

# 2. Data Cleaning & Preparation
mapping = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}
df["flight_day"] = df["flight_day"].map(mapping)

# Handle categorical variables
categorical_cols = ['sales_channel', 'trip_type', 'route', 'booking_origin']
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# 3. Address Class Imbalance (Simple Oversampling)
df_majority = df[df.booking_complete==0]
df_minority = df[df.booking_complete==1]
 
df_minority_upsampled = resample(df_minority, 
                                 replace=True,     # sample with replacement
                                 n_samples=len(df_majority),    # to match majority class
                                 random_state=42) # reproducible results
 
df_upsampled = pd.concat([df_majority, df_minority_upsampled])

X = df_upsampled.drop('booking_complete', axis=1)
y = df_upsampled['booking_complete']

# 4. Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 5. Evaluation
y_pred = rf.predict(X_test)
print("Balanced Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1]))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 6. Feature Importance (on balanced model)
importances = rf.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({'feature': feature_names, 'importance': importances}).sort_values(by='importance', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='importance', y='feature', data=feature_importance_df, palette='viridis')
plt.title('Top Factors Predicting Customer Holiday Bookings', fontsize=15)
plt.xlabel('Predictive Power (Importance)', fontsize=12)
plt.ylabel('Customer Feature', fontsize=12)
plt.tight_layout()
plt.savefig('booking_factors.png')
print("Improved feature importance plot saved as booking_factors.png")

# 7. Distribution of Booking Completion
plt.figure(figsize=(6, 4))
sns.countplot(x='booking_complete', data=df)
plt.title('Booking Completion Distribution (Original)')
plt.savefig('imbalance.png')
