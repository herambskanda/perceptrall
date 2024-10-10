# api/icicidirect/breeze_api.py

import urllib.parse
from breeze_connect import BreezeConnect
from configs.api_config import BREEZE_API_KEY, BREEZE_SECRET_KEY, BREEZE_SESSION_TOKEN
import datetime

class BreezeAPI:
    def __init__(self):
        # Initialize BreezeConnect with the encoded API key
        self.api = BreezeConnect(BREEZE_API_KEY)

        # Generate session using the encoded secret key and session token
        self.api.generate_session(
            api_secret=BREEZE_SECRET_KEY,
            session_token=BREEZE_SESSION_TOKEN
        )

    def get_historical_data(self, stock_code="ITC", interval="5minute", from_date=None, to_date=None):
        """Fetch historical stock data using Breeze API's Historical Data v2."""
        
        # Ensure the date format is in ISO 8601 format: YYYY-MM-DDTHH:MM:SS.000Z
        def format_date(date_str, time_str="00:00:00"):
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            iso_format = date_obj.isoformat()[:10] + 'T' + time_str + '.000Z'
            return iso_format
        
        # Convert from_date and to_date to ISO format
        formatted_from_date = format_date(from_date, "05:30:00") if from_date else None
        formatted_to_date = format_date(to_date, "23:59:59") if to_date else None

        return self.api.get_historical_data_v2(
            interval=interval,
            from_date=formatted_from_date,
            to_date=formatted_to_date,
            stock_code=stock_code,
            exchange_code="NSE",
            product_type="cash"
        )

    def stream_live_data(self, stock_code, callback):
        """Stream live stock data using the SDK."""
        self.api.start_websocket(
            subscribe_message={
                "stocks": [stock_code],
                "exchange_code": "NSE"
            },
            on_ticks=callback
        )

    def place_order(self, stock_code, quantity, price, action="BUY"):
        """Place a buy/sell order using the Breeze API."""
        return self.api.place_order(
            stock_code=stock_code,
            exchange_code="NSE",
            product="CNC",
            action=action,
            order_type="LIMIT",
            price=price,
            quantity=quantity
        )
