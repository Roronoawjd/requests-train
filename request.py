import requests
import itertools

string = '0123456789'
num_length = 4
timeout = 5

for num in itertools.product(string, repeat=num_length):
    number = "".join(list(num))
    url = f'http://10.10.193.114/{number}.hv.html'
    res  = requests.get(url, timeout=timeout)
    if res.status_code != 404:
        print(f"{url} (Status: {res.status_code})")
        break
    print(f"{url} (Status: {res.status_code})")