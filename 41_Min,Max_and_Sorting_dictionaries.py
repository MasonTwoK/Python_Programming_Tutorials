stock = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 386.21,
    'AAPL': 99.76,
}
stockzip = sorted(zip(stock.values(),stock.keys()))
for a,b in stockzip:
    print(a,b)
