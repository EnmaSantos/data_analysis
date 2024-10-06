import pandas as pd

# File path to the dataset
file_path = './data/World-Stock-Prices-Dataset.csv'

def load_data(file_path):
    """
    Load the stock market dataset and perform initial data exploration.
    """
    try:
        # Load the dataset with appropriate parsing
        df = pd.read_csv(file_path, parse_dates=['date'])

        # Display basic information about the dataset
        print("Dataset loaded successfully.")
        print("Columns and Data Types:")
        print(df.dtypes)
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        print("\nDataset Overview:")
        print(df.info())
        
        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    # Load the data and perform exploration
    stock_data = load_data(file_path)

    # If data is loaded successfully, perform more detailed exploration
    if stock_data is not None:
        # Check for missing values
        missing_values = stock_data.isnull().sum()
        print("\nMissing Values in Each Column:")
        print(missing_values[missing_values > 0])

        # Describe numerical columns to understand data ranges
        print("\nStatistical Summary of Numerical Columns:")
        print(stock_data.describe())
