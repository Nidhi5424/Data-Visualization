import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate sample data
np.random.seed(123)
dates = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(30)]
products = ['Product X', 'Product Y', 'Product Z']
regions = ['North', 'South', 'East', 'West']

data = {
    'Date': np.random.choice(dates, 50),
    'Product': np.random.choice(products, 50),
    'Region': np.random.choice(regions, 50),
    'Sales': np.random.randint(100, 1000, 50),
    'Profit': np.random.randint(20, 300, 50),
    'Quantity': np.random.randint(1, 10, 50)
}

# Create DataFrame and save
df = pd.DataFrame(data)
df.to_csv('additional_sales.csv', index=False)
print("additional_sales.csv created successfully!")