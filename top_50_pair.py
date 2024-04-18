import ccxt

def get_top_50_coins():
    binance = ccxt.binance()
    markets = binance.fetch_markets()
    coins = []

    for market in markets:
        if market['spot'] and market['symbol'].endswith('/USDT'):
            coins.append(market['symbol'])

    return coins[:50]

top_50_coins = get_top_50_coins()
print(top_50_coins)