"""
When the file has headers, you can either skip the header row (with an initial 
call to "reader.next()") or get each row as a "dict" (with the headers as keys) 
by using csv.DictReader
"""

import csv

def process(*args):
    # function that processes CSV rows
    pass

with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)