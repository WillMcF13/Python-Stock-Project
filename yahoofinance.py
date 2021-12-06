import yfinance as yf
import datetime 
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import requests
import csv

yf.pdr_override()

# api_key = open('api_key', 'r').read()

tickers = []
loop = True
second = True

ticker = input("Please input the stock ticker that you would like to gain some more information about: ").upper()
stock = yf.Ticker(ticker)

while second == True:
    user = input("Please input the type of information that you would like to learn about the stock: (B): Balance Sheet, (C): Cashflow, (D): Dividends, (E): Earnings, (G): Graph, (H): History, (N): Next Event, (R): Recommendations, (S): Splits, (Q): Quit ").upper()

    if user == 'B':
        print(stock.balance_sheet)

    elif user == 'C':
        print(stock.cashflow)

    elif user == 'D':
        print(stock.dividends)
    
    elif user == 'E':
        print(stock.earnings)

    elif user == 'G':

        while loop == True:
            ticker = input("Please input the stock tickers that you would like to gain some more information about (Press enter when you are done adding tickers): ").upper()
            
            if ticker == '':
                break

            else:
                tickers.append(ticker)
                print(tickers)

        graphs = yf.download(tickers)

        plt.figure
        plt.xlabel('Years')
        plt.ylabel('Price')
        plt.plot(graphs['Close'])
        plt.legend(loc="upper left")
        plt.show()

    elif user == 'H':
        # https://stackoverflow.com/questions/15226898/python-3-2-input-date-function
        start_date = input("Please enter the date you would like to start with when looking at the stock history in YYYY-MM-DD (Press enter if you would like the start date to be the earliest date): ")

        if start_date == '':
            start = datetime.datetime(1980, 1, 1)

        else:
            year, month, day = map(int, start_date.split('-'))
            start = datetime.datetime(year, month, day)

        end_date = input("Please enter the date you would like to end with when looking at the stock history in YYYY-MM-DD (Press enter if you would like to use today as the end date): ")
        
        if end_date == '':
            end = datetime.datetime.today() 

        else:
            end_year, end_month, end_day = map(int, end_date.split('-'))
            end = datetime.datetime(end_year, end_month, end_day)
        
        data = pdr.get_data_yahoo(ticker, start, end)
        print(data)

    elif user == 'N':
        print(stock.calendar)

    elif user == 'R':
        print(stock.recommendations)
    
    elif user == 'S':
        print(stock.splits)

    elif user == 'Q':
        second = False

    else:
        continue
