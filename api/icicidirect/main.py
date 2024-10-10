# main.py

from api.icicidirect.breeze_api import BreezeAPI

# Initialize BreezeAPI with credentials from config
api = BreezeAPI()

# Test: Fetch historical data for a specific stock
try:
    historical_data = api.get_historical_data(
        stock_code="RELIANCE",
        interval="5minute",
        from_date="28/02/2021",  # Pass dates in DD/MM/YYYY format
        to_date="28/02/2021"     # Pass dates in DD/MM/YYYY format
    )
    
    # Print the retrieved historical data
    if historical_data:
        print("Historical Data:", historical_data)
    else:
        print("No data retrieved.")

except Exception as e:
    print(f"Error while fetching historical data: {e}")
