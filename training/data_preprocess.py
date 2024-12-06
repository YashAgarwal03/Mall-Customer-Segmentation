import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 40, 80] 
    labels = [0, 1] 
    data['Age_Category'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
    scaler = StandardScaler()
    data = data[data['Annual Income (k$)']<100]
    scaled_features = scaler.fit_transform(data[['Age_Category','Annual Income (k$)', 'Spending Score (1-100)']])
    # Combine scaled features back with Gender
    processed_data = pd.DataFrame(scaled_features, columns=['Age','Annual Income', 'Spending Score'])
    print("Data Preprocessing Completed.")
    return processed_data