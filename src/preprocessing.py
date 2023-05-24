import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    Perform preprocessing on the dataset.

    Args:
        data (pandas.DataFrame): Input dataset.

    Returns:
        tuple: Tuple containing preprocessed features and target variables.
    """
    # convert `Neighborhood` into numeric
    le = LabelEncoder()
    data["Neighborhood"] = le.fit_transform(data["Neighborhood"])
    
    # Split features and target variable
    X = data.drop('Price', axis=1)
    y = data['Price']

    # Perform train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize features using StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
