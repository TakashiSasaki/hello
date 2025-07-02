# fetch_node_info.py

import requests

def get_node_info():
    url = "http://opendht.moukaeritai.work:4223/node/info"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる
        
        # レスポンスの内容を表示
        print("Raw Response:")
        print(response.text)
        
        # JSONとして解析
        node_info = response.json()
        
        print("\nNode Info:")
        print(f"Node ID: {node_info.get('node_id')}")
        print(f"Public IP: {node_info.get('public_ip')}")
        print(f"Operations: {node_info.get('ops')}")
        
        print("\nIPv4 Info:")
        for key, value in node_info.get('ipv4', {}).items():
            print(f"  {key.capitalize()}: {value}")
        
        print("\nIPv6 Info:")
        for key, value in node_info.get('ipv6', {}).items():
            print(f"  {key.capitalize()}: {value}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching node info: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    get_node_info()
