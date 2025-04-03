from mcp.server.fastmcp import FastMCP
from fred_connector import FREDConnector

mcp = FastMCP("FRED Data Connector")
fred = FREDConnector()

# Tool to query FRED by series ID for given date.
@mcp.tool()
def query_fred(series_id: str, observation_start: str = None, observation_end: str = None) -> str:
    """
    Query the FRED API for a specific series.
    
    Args:
        series_id (str): The FRED series ID.
        observation_start (str, optional): Start date in YYYY-MM-DD format.
        observation_end (str, optional): End date in YYYY-MM-DD format.
    
    Returns:
        str: The JSON response from FRED.
    """
    try:
        data = fred.get_series(series_id, observation_start, observation_end)
        data = [{'date': x['date'], 'value':x['value']} for x in data['observations']]
        return str(data)  # For MVP, returning a string. You may format as needed.
    except Exception as e:
        return f"Error querying FRED: {e}"

# Tool to search in FRED.
@mcp.tool()
def search_fred(query: str, limit: int = 10) -> str:
    """
    Search for FRED series using natural language.
    
    Args:
        query (str): The search query in plain language.
    
    Returns:
        str: The JSON response with search results.
    """
    try:
        results = fred.search_series(query, limit=limit)
        results = results['seriess']
        keys = ['id', 'title', 'observation_start', 'observation_end', 'frequency', 'frequency_short', 'units', 'units_short', 'seasonal_adjustment', 'seasonal_adjustment_short', 'last_updated', 'popularity', 'group_popularity', 'notes']
        results_str = [{x:y[x] for x in y.keys() if x in keys} for y in results]
        results_str = '\n.'.join(str(x) for x in results_str)
        return results_str
    except Exception as e:
        return f"Error searching FRED: {e}"

if __name__ == "__main__":
    mcp.run(transport='stdio')