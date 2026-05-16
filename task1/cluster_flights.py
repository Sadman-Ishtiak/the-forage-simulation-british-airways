import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")

# Features for clustering
features = ['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX']
X = df[features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['CLUSTER'] = kmeans.fit_predict(X_scaled)

# Analyze clusters
cluster_stats = df.groupby('CLUSTER').agg({
    'TIER1_ELIGIBLE_PAX': ['mean', 'min', 'max'],
    'TIER2_ELIGIBLE_PAX': ['mean', 'min', 'max'],
    'TIER3_ELIGIBLE_PAX': ['mean', 'min', 'max'],
    'HAUL': lambda x: x.mode()[0],
    'ARRIVAL_REGION': lambda x: x.mode()[0],
    'ARRIVAL_COUNTRY': lambda x: x.mode()[0]
})

print("Cluster Statistics:")
print(cluster_stats)

# Check distribution of HAUL in each cluster
print("\nHaul distribution in clusters:")
print(pd.crosstab(df['CLUSTER'], df['HAUL']))
