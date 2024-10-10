from breeze_connect import BreezeConnect
import yaml

def initialize_breeze():
    # Load API credentials from the configuration file
    with open('../config/settings.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Initialize the BreezeConnect object with the API key
    breeze = BreezeConnect(api_key=config['api_key'])
    
    # Generate session token for authentication
    breeze.generate_session(api_secret=config['secret_key'], session_token=config['session_token'])
    
    # Return the authenticated Breeze object for further use
    return breeze
