# mcp_fred.py
from mcp.server.fastmcp import FastMCP
from fred_connector import FREDConnector

# Initialize the MCP server
mcp = FastMCP("FRED Data Connector")
fred = FREDConnector()

# Example tool: query FRED by series ID with optional date filters.
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
        return str(data)  # For MVP, returning a string. You may format as needed.
    except Exception as e:
        return f"Error querying FRED: {e}"

# Optionally, you could add another tool that allows a free-text query to be interpreted.
@mcp.tool()
def search_fred(query: str) -> str:
    """
    Search for FRED series using natural language.
    
    Args:
        query (str): The search query in plain language.
    
    Returns:
        str: The JSON response with search results.
    """
    try:
        results = fred.search_series(query)
        return str(results)
    except Exception as e:
        return f"Error searching FRED: {e}"

if __name__ == "__main__":
    # Run the MCP server in development mode
    mcp.run()
    # mcp.run(transport='stdio')    