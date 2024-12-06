import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def find_optimal_k(data: pd.DataFrame, max_k: int = 10) -> int:
    """Finds the optimal number of clusters using the Elbow Method and Silhouette Score."""
    inertia = []
    silhouette_scores = []

    for k in range(2, max_k):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(data, kmeans.labels_))

    # Return k with the highest silhouette score
    optimal_k = range(2, max_k)[silhouette_scores.index(max(silhouette_scores))]
    return optimal_k