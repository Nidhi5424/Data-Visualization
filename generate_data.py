import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sales_data(num_records=1000):
    np.random.seed(42)
    
    # Generate random dates in 2022-2023
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = (end_date - start_date).days
    dates = [start_date + timedelta(days=np.random.randint(date_range)) for _ in range(num_records)]
    
    # Generate random products
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    
    # Generate random regions
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Generate random sales amounts (with some outliers)
    base_sales = np.random.normal(500, 150, num_records)
    sales = np.abs(base_sales).astype(int)
    
    # Generate random profits (correlated with sales but with some noise)
    profits = (sales * np.random.uniform(0.1, 0.3, num_records)).astype(int)
    
    # Create DataFrame
    data = {
        'Date': dates,
        'Product': np.random.choice(products, num_records),
        'Region': np.random.choice(regions, num_records),
        'Sales': sales,
        'Profit': profits,
        'Quantity': np.random.randint(1, 10, num_records)
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values randomly
    for col in ['Product', 'Region', 'Sales', 'Profit']:
        df.loc[df.sample(frac=0.05).index, col] = np.nan
    
    return df

# Generate and save the dataset
sales_data = generate_sales_data()
sales_data.to_csv('sales_data.csv', index=False)