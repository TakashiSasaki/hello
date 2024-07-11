# fetch_value.py

import requests
import argparse

def fetch_value(key):
    url = f"http://opendht.moukaeritai.work:4223/key/{key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる
        
        # レスポンスの内容を表示
        print("Raw Response:")
        print(response.text)
        
        # JSONとして解析
        values = response.json()
        
        print("\nValues for Key:", key)
        for value in values:
            print(f"Value: {value}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching value: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch a value from the OpenDHT system.')
    parser.add_argument('key', type=str, help='The key for the value to fetch.')

    args = parser.parse_args()
    fetch_value(args.key)
