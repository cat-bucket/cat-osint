import requests
qwe = [str(i) for i in range(1, 101)]
x=0
try:
  while True:
    url="http://121.196.237."+qwe[x]
    print(url)
    x += 1
    try:
      response = requests.get(url)
      print("成功")
      
    except requests.exceptions.HTTPError as http_err:
      print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
      print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
      print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
      print(f"An error occurred: {req_err}")
except KeyboardInterrupt:
    print("已停止循環。")

