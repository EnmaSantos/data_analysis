import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    file_path = 'data/World-Stock-Prices-Dataset.csv'
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    
    # Capitalize brand names
    df['Brand_Name'] = df['Brand_Name'].str.title()
    
    # Calculate daily growth as percentage change from Open to Close
    df['Daily_Growth (%)'] = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
    
    # Calculate cumulative growth for each stock from the first 'Close' price to current 'Close' price
    df['Cumulative_Growth (%)'] = df.groupby('Brand_Name')['Close'].transform(lambda x: (x / x.iloc[0] - 1) * 100).round(2)
    
    return df

def get_stock_data(df, brands, days_back):
    # Get the latest date in the dataset
    latest_date = df['Date'].max()
    start_date = latest_date - pd.Timedelta(days=days_back)
    
    # Filter data for the selected brands and date range
    stock_data = df[(df['Brand_Name'].isin(brands)) & (df['Date'] >= start_date)]

    # Reset index for clarity
    stock_data = stock_data.reset_index(drop=True)

    # Simplify the 'Date' format to 'YYYY-MM-DD'
    stock_data['Date'] = stock_data['Date'].dt.strftime('%Y-%m-%d')
    
    return stock_data, latest_date

def main():
    # Load dataset
    file_path = 'data/World-Stock-Prices-Dataset.csv'
    df = load_data(file_path)
    
    # Display the latest date in the dataset
    latest_date = df['Date'].max()
    print(f"The latest available date in the dataset is: {latest_date.date()}")
    
    # Ask how many brands to analyze
    num_brands = int(input("How many brands do you want to check? "))
    
    # Get brand names from user
    brands = []
    for i in range(num_brands):
        brand_name = input(f"Enter the brand name for stock {i + 1}: ").strip().title()
        brands.append(brand_name)
    
    # Ask how many days back to analyze
    days_back = int(input(f"How many days back from {latest_date.date()} do you want to check? "))
    
    # Get filtered stock data
    stock_data, latest_date = get_stock_data(df, brands, days_back)
    
    # Check if data is available for the provided brands
    if stock_data.empty:
        print("No data found for the specified brands and date range.")
    else:
        # Display the relevant information
        print("\nFiltered Stock Data:")
        print(stock_data[['Date', 'Brand_Name', 'High', 'Low', 'Daily_Growth (%)', 'Cumulative_Growth (%)']])

if __name__ == "__main__":
    main()
