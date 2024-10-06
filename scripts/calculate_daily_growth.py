import pandas as pd

def calculate_daily_growth(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)
    
    # Convert 'Date' to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Capitalize brand names
    df['Brand_Name'] = df['Brand_Name'].str.title()
    
    # Calculate daily growth as percentage change from Open to Close
    df['Daily_Growth'] = ((df['Close'] - df['Open']) / df['Open'] * 100).round(2)
    
    # Save the result to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Daily growth calculated and saved to {output_file}")
    return df

if __name__ == "__main__":
    # Specify input and output files in the 'data' folder
    input_file = 'data/World-Stock-Prices-Dataset.csv'
    output_file = 'data/stock_with_daily_growth.csv'
    
    # Perform the calculation
    calculate_daily_growth(input_file, output_file)
