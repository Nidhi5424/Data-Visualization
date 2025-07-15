from sales_analyzer import SalesDataAnalyzer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def display_menu():
    print("\n==========================================")
    print("Data Analysis & Visualization Program")
    print("\n==========================================")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("\n==========================================")

def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        
        if choice == '1':
            file_path = input("\nEnter path to CSV file: ").strip()
            analyzer.load_data(file_path)
            
        elif choice == '2':
            analyzer.explore_data()  
            
        elif choice == '3':
            analyzer.dataframe_operations()
            
        elif choice == '4':
            analyzer.clean_data()
            
        elif choice == '5':
            analyzer.generate_statistics()
            
        elif choice == '6':
            analyzer.visualize_data()
            
        elif choice == '7':
            analyzer.save_visualization()
            
        elif choice == '8':
            print("\nThank you for using the program. Goodbye!")
            break
            
        else:
            print("\nInvalid input. Please enter a number 1-8.")

if __name__ == "__main__":
    main()