# fetch_node_stats.py

import requests

def get_node_stats():
    url = "http://opendht.moukaeritai.work:4223/node/stats"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーが発生した場合、例外を発生させる
        
        # レスポンスの内容を表示
        print("Raw Response:")
        print(response.text)
        
        # JSONとして解析
        node_stats = response.json()
        
        print("\nNode Stats:")
        print(f"Listen Count: {node_stats.get('listenCount')}")
        print(f"Push Listeners Count: {node_stats.get('pushListenersCount')}")
        print(f"Put Count: {node_stats.get('putCount')}")
        print(f"Request Rate: {node_stats.get('requestRate')}")
        print(f"Total Permanent Puts: {node_stats.get('totalPermanentPuts')}")
        
        node_info = node_stats.get('nodeInfo', {})
        print("\nNode Info:")
        print(f"  Node ID: {node_info.get('node_id')}")
        print(f"  Operations: {node_info.get('ops')}")
        
        print("\n  IPv4 Info:")
        ipv4_info = node_info.get('ipv4', {})
        for key, value in ipv4_info.items():
            print(f"    {key.capitalize()}: {value}")
        
        print("\n  IPv6 Info:")
        ipv6_info = node_info.get('ipv6', {})
        for key, value in ipv6_info.items():
            print(f"    {key.capitalize()}: {value}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching node stats: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    get_node_stats()
