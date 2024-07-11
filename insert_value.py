# insert_value.py

import requests
import json
import argparse

def insert_value(key, value):
    url = f"http://opendht.moukaeritai.work:4223/key/{key}"
    payload = {
        "value": value
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる
        
        print("Value inserted successfully.")
        print("Response:")
        print(response.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error inserting value: {e}")
    except ValueError as e:
        print(f"Error parsing response: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Insert a value into the OpenDHT system.')
    parser.add_argument('key', type=str, help='The key for the value to insert.')
    parser.add_argument('value', type=str, help='The value to insert.')

    args = parser.parse_args()
    insert_value(args.key, args.value)
