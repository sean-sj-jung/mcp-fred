from fred_connector import FREDConnector
import pandas as pd

def main():
    fred = FREDConnector()
    
    series_id = "DFII10"  # 10-Year Treasury Inflation-Indexed Security
    start_date = "2025-01-01"
    end_date = "2025-01-11"
    
    query = "inflation rate"
    limit = 10    
    ## For testing get_series
    try:
        response = fred.get_series(
            series_id=series_id,
            observation_start=start_date,
            observation_end=end_date
        )
        
        response = [{'date': x['date'], 'value':x['value']} for x in response['observations']]
        print(response)
        
    ## For testing search_series
    # try:
    #     results = fred.search_series(query, limit=limit)
    #     results = results['seriess']
    #     keys = ['id', 'title', 'observation_start', 'observation_end', 'frequency', 'frequency_short', 'units', 
    #             'units_short', 'seasonal_adjustment', 'seasonal_adjustment_short', 'last_updated', 'popularity', 
    #             'group_popularity', 'notes']
    #     results_str = [{x:y[x] for x in y.keys() if x in keys} for y in results]
    #     results_str = '\n.'.join(str(x) for x in results_str)
    #     print(results_str)

    except Exception as e:
        print(f"Error fetching data: {str(e)}")

if __name__ == "__main__":
    main()
