## Overview

**Project Title**: Stock Market Analysis with Python and Pandas

**Project Description**: This project aims to analyze trends and patterns in historical stock market data. Using Python and the Pandas library, we will explore the dataset to identify key stock performance indicators, calculate daily returns, analyze volatility, and visualize results over time. The dataset includes daily stock price data (e.g., Open, Close, Volume) for different companies across various industries.

**Project Goals**:
1. Analyze daily and cumulative stock performance using Python.

2. Allow the user to input specific brands and date ranges for targeted analysis.

3. Visualize daily growth and cumulative growth over time through graphs.

4. Save results dynamically in the results folder for easy reference.


## Instructions for Build and Use

Steps to build and/or run the software:

1. Clone the Repository: Clone this repository to your local machine. `git clone https://github.com/EnmaSantos/data_analysis`
2. Install Dependencies: Ensure you have Python and the required libraries installed. You can use pip to install the dependencies: `pip install pandas matplotlib`
3. Navigate to the Script Directory: Go to the scripts directory where the main files are located. `cd data_analysis/scripts`
4. Run the Script: Run the script using Python. 

Instructions for using the software:

1. Select Number of Brands to Analyze: The script will ask you how many brands you want to analyze. Enter the number. 
2. Input Brand Names: For each brand, input the brand name exactly as it appears in the dataset (case insensitive).
3. Choose Date Range or Specific Date:
   - For Daily Growth Analysis: Enter a specific date to analyze the growth for that day.
   - For Cumulative Growth Analysis: Enter how many days back you want to analyze from the latest available date.  
4. View Results: The script will display the daily growth and cumulative growth for the selected brands and date range. 

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python: Version >=3.6 
* Pandas: For data analysis and manipulation.
* Matplotlib: For generating plots and graphs.

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
* [Python Documentation](https://docs.python.org/3/)
* [Kaggle Datasets](https://www.kaggle.com/datasets)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add more data analysis features.
* [ ] Add more specificity for file names.
* [ ] Improve error handling and user input validation.
