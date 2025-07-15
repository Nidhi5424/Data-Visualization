import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        if file_path:
            self.load_data(file_path)
    
    def __del__(self):
        print("Cleaning up resources...")

    def load_data(self, file_path):
        """Load data from CSV file"""
        try:
            self.data = pd.read_csv(file_path)
            print(f"\nDataset loaded successfully with {len(self.data)} records")
            
            if 'Date' in self.data.columns:
                self.data['Date'] = pd.to_datetime(self.data['Date'])
            return True
        except Exception as e:
            print(f"\nError loading data: {e}")
            return False

    def explore_data(self):
        """Show all data exploration at once"""
        if self.data is None:
            print("\nNo data loaded. Please load data first.")
            return
        
        print("\n=====================================")
        print("DATA EXPLORATION RESULTS")
        print("\n=====================================")
        
        print("\n1. First 5 rows:")
        print(self.data.head())
        
        print("\n2. Last 5 rows:")
        print(self.data.tail())
        
        print("\n3. Column names and data types:")
        print(self.data.dtypes)
        
        print("\n4. Basic statistics:")
        print(self.data.describe(include='all'))
        
        print("\n5. Missing values count:")
        print(self.data.isnull().sum())
        print("\n=====================================")

    def clean_data(self):
        """Handle missing values"""
        if self.data is None:
            print("\nNo data loaded. Please load data first.")
            return
        
        print("\n=====================================")
        print("DATA CLEANING REPORT")
        print("\n=====================================")
        
        print("\nMissing values BEFORE cleaning:")
        print(self.data.isnull().sum())
        
        numeric_cols = self.data.select_dtypes(include=np.number).columns
        for col in numeric_cols:
            self.data[col] = self.data[col].fillna(self.data[col].median())
        
        categorical_cols = self.data.select_dtypes(include='object').columns
        for col in categorical_cols:
            self.data[col] = self.data[col].fillna(self.data[col].mode()[0])
        
        print("\nMissing values AFTER cleaning:")
        print(self.data.isnull().sum())
        print("\n=====================================")
        print("\nData cleaning completed successfully!")

    def dataframe_operations(self):
        """Perform DataFrame operations with error handling"""
        if self.data is None:
            print("\nNo data loaded. Please load data first.")
            return
        
        print("\n=============================")
        print("DATAFRAME OPERATIONS MENU")
        print("\n=============================")
        print("1. Group by operations")
        print("2. Merge/join operations")
        print("3. Pivot tables")
        print("4. Filter data")
        print("\n=============================")
        
        op_choice = input("\nEnter operation choice: ").strip()
        
        if op_choice == '1':
            print("\nAvailable columns:", list(self.data.columns))
            group_col = input("Enter column to group by: ")
            
            if group_col in self.data.columns:
                
                numeric_cols = self.data.select_dtypes(include=np.number).columns
                if len(numeric_cols) > 0:
                    print(f"\nGrouped by '{group_col}' (showing numeric columns only):")
                    print(self.data.groupby(group_col)[numeric_cols].mean())
                else:
                    print("\nNo numeric columns available for calculations")
            else:
                print(f"\nColumn '{group_col}' not found in data")
        
        elif op_choice == '2':
            print("\nMerge/join functionality would go here")
        
        elif op_choice == '3':
            print("\nPivot table functionality would go here")
        
        elif op_choice == '4':
            print("\nFilter functionality would go here")
        
        else:
            print("\nInvalid choice. Please enter 1-4.")

    def generate_statistics(self):
        """Generate descriptive statistics"""
        if self.data is None:
            print("\nNo data loaded. Please load data first.")
            return
        
        print("\n=========================")
        print("DESCRIPTIVE STATISTICS")
        print("\n=========================")
        print(self.data.describe(include='all'))
        print("\nCorrelation Matrix (numeric columns only):")
        numeric_data = self.data.select_dtypes(include=np.number)
        if not numeric_data.empty:
            print(numeric_data.corr())
        else:
            print("No numeric columns for correlation")
        print("\n================================")

    def visualize_data(self):
        """Data visualization menu"""
        if self.data is None:
            print("\nNo data loaded. Please load data first.")
            return
        
        print("\n" + "="*50)
        print("DATA VISUALIZATION MENU")
        print("\n====================")
        print("1. Bar plot")
        print("2. Line plot")
        print("3. Scatter plot")
        print("4. Histogram")
        print("5. Box plot")
        print("\n====================")
        
        viz_choice = input("\nEnter visualization choice: ").strip()
        
        if viz_choice in ['1', '2', '3', '4', '5']:
            print("\nAvailable columns:", list(self.data.columns))
            x_col = input("Enter x-axis column: ")
            
            if x_col in self.data.columns:
                if viz_choice == '1': 
                    y_col = input("Enter y-axis column: ")
                    if y_col in self.data.columns:
                        sns.barplot(data=self.data, x=x_col, y=y_col)
                        plt.title(f"Bar Plot: {y_col} by {x_col}")
                        plt.xticks(rotation=45)
                        plt.show()
                
            else:
                print(f"\nColumn '{x_col}' not found")
        else:
            print("\nInvalid choice")

    def save_visualization(self):
        """Save visualization placeholder"""
        print("\nThis would save the last generated visualization")