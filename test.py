from fred_connector import FREDConnector
import pandas as pd

def main():
    # Initialize FRED connector
    fred = FREDConnector()
    
    # Fetch DFII10 data
    series_id = "DFII10"  # 10-Year Treasury Inflation-Indexed Security
    start_date = "2020-01-01"
    end_date = "2025-01-01"
    
    try:
        # Get the data
        response = fred.get_series(
            series_id=series_id,
            observation_start=start_date,
            observation_end=end_date
        )
        
        # Convert to pandas DataFrame
        df = pd.DataFrame(response['observations'])
        df['value'] = pd.to_numeric(df['value'].replace('.', pd.NA))
        df['date'] = pd.to_datetime(df['date'])
        
        # Display the first few rows
        print("\nFirst few rows of the data:")
        print(df.head())
        
        # Display basic statistics
        print("\nBasic statistics:")
        print(df['value'].describe())
        
    except Exception as e:
        print(f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    main()
