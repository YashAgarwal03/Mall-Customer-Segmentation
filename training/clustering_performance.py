import pandas as pd
from sklearn.metrics import silhouette_score

def summarize_clusters(data: pd.DataFrame):
    """Summarizes cluster characteristics."""
    silhouette_avg = silhouette_score(data[['Age','Annual Income', 'Spending Score']], data['Cluster'])
    print(silhouette_avg)