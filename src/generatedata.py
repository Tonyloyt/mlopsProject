import pandas as pd
import numpy as np

def generateData():
    # Set the random seed for reproducibility
    np.random.seed(42)

    # Number of instances in the dataset
    num_instances = 500

    # Generate random values for the features
    size = np.random.randint(1000, 3000, num_instances)
    bedrooms = np.random.randint(1, 6, num_instances)
    bathrooms = np.random.randint(1, 4, num_instances)
    garage = np.random.randint(0, 3, num_instances)
    neighborhoods = np.random.choice(['A', 'B', 'C', 'D'], num_instances)

    # Calculate the price based on a formulaic relationship with the features
    price = 100000 + (size * 50) + (bedrooms * 20000) + (bathrooms * 15000) + (garage * 10000) + (neighborhoods == 'B') * 50000

    # Create a DataFrame to store the data
    data = pd.DataFrame({
        'Size (sqft)': size,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'Garage': garage,
        'Neighborhood': neighborhoods,
        'Price': price
    })

    # Save the DataFrame as CSV
    data.to_csv('data/housing_data.csv', index=False)
