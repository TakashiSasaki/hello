# fetch_value.py

import requests
import argparse
import json
import base64

def fetch_value(key):
    url = f"http://opendht.moukaeritai.work:4223/key/{key}"
    headers = {'Accept': 'application/json'}

    print("URL:", url)
    print("Headers:", headers)

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        decoded_data = base64.b64decode(data["data"]).decode()
        print("Value fetched successfully.")
        print("Decoded data:")
        print(decoded_data)
        print("Response:")
        print(json.dumps(data, indent=2))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
        print("Response content:")
        print(response.content.decode())
    except Exception as err:
        print(f"Other error occurred: {err}")  # Python 3.6
        print("Response content:")
        print(response.content.decode() if response else "No response")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch a value from the OpenDHT system.')
    parser.add_argument('key', type=str, help='The key for the value to fetch.')

    args = parser.parse_args()
    fetch_value(args.key)
