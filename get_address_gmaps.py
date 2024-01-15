import requests
import os
import sys

# Import from Secret API key from another folder
path_to_folder = 'C:/Users/kevin/Google Drive/My Drive/Github/All API Keys'
sys.path.insert(0, path_to_folder)
from all_api_keys import google_maps_api_key

def get_place_address(place_name, city_name, api_key):
    # Define the endpoint URL
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"

    # Define the parameters for the API request
    params = {
        "input": f"{place_name} {city_name}",
        "inputtype": "textquery",
        "fields": "formatted_address",
        "key": api_key
    }

    # Send the API request
    response = requests.get(url, params=params)

    # Parse the response JSON
    data = response.json()

    # Extract the address from the response
    # Check if the 'candidates' field is present in the response
    if 'candidates' in data and len(data['candidates']) > 0:
        address = data['candidates'][0]['formatted_address']
    else:
        address = "No results found"

    return address

place_name = "in n out burger"
city_name = "morgan hill"
address = get_place_address(place_name, city_name, google_maps_api_key)
print(address)