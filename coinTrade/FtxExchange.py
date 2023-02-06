import  ccxt

ftx = ccxt.ftx()
# ftx.proxies = {'http': 'http://127.0.0.1:33210', 'https': 'http://127.0.0.1:33210'}
listFtx = dir(ftx)
for symbol in listFtx:
    print(symbol)