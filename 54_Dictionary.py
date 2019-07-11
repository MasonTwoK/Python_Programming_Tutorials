stocks ={
'AAPL':201,
'GOOG':800,
'FB':54,
'MSFT':333,
'TUNA':789,
}

min_price = min(zip(stocks.values(),stocks.keys()))

print(min_price)