import matplotlib.pyplot as plt
import matplotlib.animation as animation
from yahoofinancials import YahooFinancials
from collections import defaultdict
import datetime
import pandas as pd

######################
# yahoo finance
######################
stock_dict = defaultdict(list)
stocks = ['QCOM', 'CSCO', 'INTC', 'AAPL', 'GOOG']
time_list = []

def update_stock(i):
    now = datetime.datetime.now()
    time_list.append(now)
    j = 0
    for stock in stocks:
        ticker = stock
        print("processing stock "+stock)
        yahoo_financials = YahooFinancials(ticker)
        stock_dict[stock].append(yahoo_financials.get_current_price())

        ax2[j].clear()
        ax2[j].plot(time_list, stock_dict[stock], label=stock)
        ax2[j].set_xlabel('Date Time')
        ax2[j].set_ylabel('Closing price ($)')

        j += 1

fig2, ax2 = plt.subplots(nrows=5, ncols=1, figsize=(16,9))

ani2 = animation.FuncAnimation(fig2, update_stock, interval=10000)

plt.show()