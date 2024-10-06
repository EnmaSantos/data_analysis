import pandas as pd
import matplotlib.pyplot as plt

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
    
    return df

def get_stock_data(df, brands, days_back):
    # Get the latest date in the dataset
    latest_date = df['Date'].max()
    start_date = latest_date - pd.Timedelta(days=days_back)
    
    # Filter data for the selected brands and date range
    stock_data = df[(df['Brand_Name'].isin(brands)) & (df['Date'] >= start_date)]

    # Reset index for clarity
    stock_data = stock_data.reset_index(drop=True)

    return stock_data, latest_date

def calculate_cumulative_growth(stock_data):
    # Calculate cumulative growth for each brand within the filtered data
    stock_data['Cumulative_Growth (%)'] = stock_data.groupby('Brand_Name')['Close'].transform(
        lambda x: (x / x.iloc[0] - 1) * 100).round(2)
    return stock_data

def plot_cumulative_growth(stock_data):
    # Plot the cumulative growth over time for each brand
    plt.figure(figsize=(10, 5))
    for brand in stock_data['Brand_Name'].unique():
        brand_data = stock_data[stock_data['Brand_Name'] == brand]
        plt.plot(brand_data['Date'], brand_data['Cumulative_Growth (%)'], marker='o', label=brand)
    
    plt.title('Cumulative Growth Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Growth (%)')
    plt.xticks(rotation=45)
    plt.legend()
    # Save the plot
    plt.savefig('results/cumulative_growth.png')
    plt.show()

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
    
    # Ask how many days back to analyze for cumulative growth
    days_back = int(input(f"How many days back from {latest_date} do you want to check for cumulative growth? "))
    
    # Get filtered stock data
    stock_data, latest_date = get_stock_data(df, brands, days_back)
    
    # Check if data is available for the provided brands
    if stock_data.empty:
        print("No data found for the specified brands and date range.")
    else:
        # Calculate cumulative growth for the filtered period
        stock_data = calculate_cumulative_growth(stock_data)

        # Display the relevant information
        print("\nCumulative Growth Data:")
        print(stock_data[['Date', 'Brand_Name', 'High', 'Low', 'Cumulative_Growth (%)']])
        
        # Plot the cumulative growth for visualization
        plot_cumulative_growth(stock_data)

if __name__ == "__main__":
    main()
