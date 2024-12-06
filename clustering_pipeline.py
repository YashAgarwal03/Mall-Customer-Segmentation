from training.data_ingestion import load_data
from training.data_preprocess import preprocess_data
from training.number_of_cluster import find_optimal_k
from training.clustering import kmean
from training.clustering_performance import summarize_clusters

def run_pipeline(file_path: str):
    # Step 1: Data Ingestion
    data = load_data(file_path)
    
    # Step 2: Data Preprocessing
    processed_data = preprocess_data(data)
    
    # Step 3: Finding optimal number of clustering
    optimal_k = find_optimal_k(processed_data)
    
    # Step 6: Clustering
    cluster_data = kmean(processed_data, n_clusters=optimal_k)
    
    # Step 7: performance
    summarize_clusters(cluster_data)

if __name__ == '__main__':
    file_path = 'C:\mall-customer-segmentation\data\Mall_Customers.csv'
    run_pipeline(file_path)
