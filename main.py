import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_url(base_url, ip_suffix):
    url = f"{base_url}.{ip_suffix}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(url)
    except requests.exceptions.RequestException:
        pass

def main():
    base_url = input("输入前9位ip号段(如 http://121.196.237): ")  # 获取用户输入的基本URL
    qwe = [str(i) for i in range(1, 257)]
    
    with ThreadPoolExecutor(max_workers=64) as executor:
        futures = {executor.submit(fetch_url, base_url, ip_suffix): ip_suffix for ip_suffix in qwe}

        for future in as_completed(futures):
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
