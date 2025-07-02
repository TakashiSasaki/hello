# insert_value.py

import requests
import argparse
import json
import base64

def insert_value(key, value):
    url = f"http://opendht.moukaeritai.work:4223/key/{key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "data": base64.b64encode(value.encode()).decode(),
        "type": 0
    }

    print("URL:", url)
    print("Headers:", headers)
    print("Data:", json.dumps(data))

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        print("Value inserted successfully.")
        print("Response:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
        print("Response content:")
        print(response.content.decode())
    except Exception as err:
        print(f"Other error occurred: {err}")  # Python 3.6
        print("Response content:")
        print(response.content.decode() if response else "No response")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Insert a value into the OpenDHT system.')
    parser.add_argument('key', type=str, help='The key for the value to insert.')
    parser.add_argument('value', type=str, help='The value to insert.')

    args = parser.parse_args()
    insert_value(args.key, args.value)
