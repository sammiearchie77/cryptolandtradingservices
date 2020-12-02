import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://blockchain.info/tobtc?currency=USD&value=1388.888888888889')
data = response.data.decode()
print(data)