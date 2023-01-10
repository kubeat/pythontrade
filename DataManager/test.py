import time
import asyncio
import ccxt.async_support as ccxt
import ccxt


bibox = ccxt.bibox()
# bibox.proxies = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}
bibox.apiKey = 'f93b63f1f03a37f3dc8f5e6849043c46d707c055'
bibox.secret = '02b748e07e4bc6ef83320e7c38d238ce746e1173'
since = None
limit = 100
end_time = bibox.milliseconds()
params = {
'end_time': int(end_time / 1000),
}
withdrawals  = bibox.fetch_withdrawals("TRX", since, limit, params)

