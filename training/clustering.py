import pandas as pd
from sklearn.cluster import KMeans

def kmean(data: pd.DataFrame, n_clusters: int) -> pd.DataFrame:
    """Trains the final K-means model."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = kmeans.fit_predict(data[['Age','Annual Income', 'Spending Score']])
    print("Clustering Completed.")
    return data