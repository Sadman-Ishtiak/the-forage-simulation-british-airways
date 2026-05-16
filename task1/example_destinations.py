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

# For each cluster, find top 3 countries/cities
for i in range(4):
    print(f"\nCluster {i} (Average T1: {df[df['CLUSTER']==i]['TIER1_ELIGIBLE_PAX'].mean():.2f}, T2: {df[df['CLUSTER']==i]['TIER2_ELIGIBLE_PAX'].mean():.2f}, T3: {df[df['CLUSTER']==i]['TIER3_ELIGIBLE_PAX'].mean():.2f})")
    top_countries = df[df['CLUSTER']==i]['ARRIVAL_COUNTRY'].value_counts().head(3).index.tolist()
    print(f"Example Countries: {top_countries}")
