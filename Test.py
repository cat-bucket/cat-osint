import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

qwe = [str(i) for i in range(1, 257)]


def fetch_url(ip_suffix):
    url = f"http://121.196.237.{ip_suffix}"
    try:
        response = requests.get(url)
        print(url)
    except requests.exceptions.RequestException:
        
        pass
      
def main():
    with ThreadPoolExecutor(max_workers=64) as executor:  
        
        futures = {executor.submit(fetch_url, ip_suffix): ip_suffix for ip_suffix in qwe}

        for future in as_completed(futures):
  
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("已停止循环。")
