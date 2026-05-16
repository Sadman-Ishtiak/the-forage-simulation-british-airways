import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_excel("British Airways Summer Schedule Dataset - Forage Data Science Task 1.xlsx")

features = ['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX']
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42)
df['CLUSTER'] = kmeans.fit_predict(X_scaled)

# Cluster distribution by Region
region_cluster = pd.crosstab(df['ARRIVAL_REGION'], df['CLUSTER'], normalize='index') * 100
print("Cluster distribution by Region (%):")
print(region_cluster)

# Cluster distribution by Haul
haul_cluster = pd.crosstab(df['HAUL'], df['CLUSTER'], normalize='index') * 100
print("\nCluster distribution by Haul (%):")
print(haul_cluster)
