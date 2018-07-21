import matplotlib.pyplot as plt
import matplotlib.animation as animation
from googlefinance.client import get_price_data

######################
# google finance
######################

def update_stock(i):
    param1 = {
        'q': "QCOM", # Stock symbol (ex: "AAPL")
        'i': "60", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1H" # Period (Ex: "1Y" = 1 year)
    }
    df1 = get_price_data(param1)
    close1 = df1['Close']

    param2 = {
        'q': "CSCO", # Stock symbol (ex: "AAPL")
        'i': "10", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1D" # Period (Ex: "1Y" = 1 year)
    }
    df2 = get_price_data(param2)
    close2 = df2['Close']

    param3 = {
        'q': "INTC", # Stock symbol (ex: "AAPL")
        'i': "10", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1D" # Period (Ex: "1Y" = 1 year)
    }
    df3 = get_price_data(param3)
    close3 = df3['Close']

    param4 = {
        'q': "AAPL", # Stock symbol (ex: "AAPL")
        'i': "10", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1D" # Period (Ex: "1Y" = 1 year)
    }
    df4 = get_price_data(param4)
    close4 = df4['Close']

    param5 = {
        'q': "GOOG", # Stock symbol (ex: "AAPL")
        'i': "10", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1D" # Period (Ex: "1Y" = 1 year)
    }
    df5 = get_price_data(param5)
    close5 = df5['Close']

    # clear old
    ax1[0].clear()
    ax1[1].clear()
    ax1[2].clear()
    ax1[3].clear()
    ax1[4].clear()

    # plot 5*1 graph

    ax1[0].plot(close1.index, close1, label='QCOM')
    ax1[0].set_xlabel('Date')
    ax1[0].set_ylabel('Closing price ($)')
    ax1[0].legend()

    ax1[1].plot(close2.index, close2, label='CSCO')
    ax1[1].set_xlabel('Date')
    ax1[1].set_ylabel('Closing price ($)')
    ax1[1].legend()

    ax1[2].plot(close3.index, close3, label='INTC')
    ax1[2].set_xlabel('Date')
    ax1[2].set_ylabel('Closing price ($)')
    ax1[2].legend()

    ax1[3].plot(close4.index, close4, label='AAPL')
    ax1[3].set_xlabel('Date')
    ax1[3].set_ylabel('Closing price ($)')
    ax1[3].legend()

    ax1[4].plot(close5.index, close5, label='GOOG')
    ax1[4].set_xlabel('Date')
    ax1[4].set_ylabel('Closing price ($)')
    ax1[4].legend()

fig1, ax1 = plt.subplots(nrows=5, ncols=1, figsize=(16,9))
ani1 = animation.FuncAnimation(fig1, update_stock, interval=60000)

plt.show()