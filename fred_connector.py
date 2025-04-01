# fred_connector.py
import requests
from config import FRED_API_KEY, FRED_BASE_URL

class FREDConnector:
    def __init__(self, api_key=FRED_API_KEY):
        self.api_key = api_key
        self.base_url = FRED_BASE_URL

    def _get(self, endpoint, params):
        params['api_key'] = self.api_key
        params['file_type'] = 'json'
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_series(self, series_id, observation_start=None, observation_end=None):
        params = {"series_id": series_id}
        if observation_start:
            params["observation_start"] = observation_start
        if observation_end:
            params["observation_end"] = observation_end
        return self._get("series/observations", params)

    def search_series(self, query):
        params = {"search_text": query}
        return self._get("series/search", params)