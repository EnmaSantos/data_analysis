import pandas as pd

def load_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True).dt.date
    
    # Capitalize brand names
    df['Brand_Name'] = df['Brand_Name'].str.title()

    # Round 'High' and 'Low' columns to 2 decimal places
    df['High'] = df['High'].round(2)
    df['Low'] = df['Low'].round(2)
    df['Open'] = df['Open'].round(2)
    df['Close'] = df['Close'].round(2)
    
    
    # Calculate daily growth as percentage change from Open to Close
    df['Daily_Growth (%)'] = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
    
    return df

def get_stock_data(df, brands, specific_date):
    # Filter data for the selected brands and specific date
    stock_data = df[(df['Brand_Name'].isin(brands)) & (df['Date'].astype(str) == specific_date)]
    
    return stock_data

def main():
    # Load dataset
    file_path = 'data/World-Stock-Prices-Dataset.csv'
    df = load_data(file_path)
    
    # Display the latest date in the dataset
    latest_date = df['Date'].max()
    print(f"The latest available date in the dataset is: {latest_date}")
    
    # Ask how many brands to analyze
    num_brands = int(input("How many brands do you want to check? "))
    
    # Get brand names from user
    brands = []
    for i in range(num_brands):
        brand_name = input(f"Enter the brand name for stock {i + 1}: ").strip().title()
        brands.append(brand_name)
    
    # Ask the user for a specific date to see daily growth
    specific_date = input(f"\nEnter a specific date (YYYY-MM-DD) within the data range to see the daily growth: ").strip()
    
    # Get filtered stock data for the specific date
    stock_data = get_stock_data(df, brands, specific_date)
    
    # Check if data is available for the provided brands and date
    if stock_data.empty:
        print(f"No data found for the specified brands on {specific_date}.")
    else:
        # Display daily growth information for that date
        print("\nDaily Growth on", specific_date)
        print(stock_data[['Date', 'Brand_Name', 'Open', 'Close', 'Daily_Growth (%)']])
    # Save the daily growth data to a CSV file
    stock_data.to_csv(f'results/daily_growth_{specific_date}.csv', index=False)

if __name__ == "__main__":
    main()
