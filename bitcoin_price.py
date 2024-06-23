import requests
import sys

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'bitcoin' in data and 'usd' in data['bitcoin']:
            return data['bitcoin']['usd']
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    price = get_bitcoin_price()
    if price:
        print(f"Current Bitcoin Price: ${price}")
    else:
        print("Failed to retrieve Bitcoin price.")
        sys.exit(1)
