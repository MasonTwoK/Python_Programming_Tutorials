import heapq

list = [23,2,6,0,14,7]

stocks = [
    {'ticker': 'AAPL','price':201},
    {'ticker': 'GOOG','price':800},
    {'ticker': 'FB','price':54},
    {'ticker': 'MSFT','price':333},
    {'ticker': 'TUNA','price':789}
]

print(heapq.nlargest(1,stocks,key= lambda stocks: stocks["price"]))
           