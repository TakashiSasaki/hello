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
        for key, value in node_stats.items():
            print(f"{key}: {value}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching node stats: {e}")
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    get_node_stats()
