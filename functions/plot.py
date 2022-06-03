from cProfile import label
from matplotlib import pyplot as plt
from numpy import percentile

# def printSetUpLines(arr, inverse = False):
#   setUpLines = [
#     [0.05, 'dotted'],
#     [0.10, 'dashed'],
#     [0.25, 'dashdot'],
#   ]

def printChart (ticker, dates, prices, rates):
  setUpLines = [
    [0.05, 'dotted'],
    [0.10, 'dashed'],
    [0.25, 'dashdot'],
  ]

  fig, yPrices = plt.subplots(figsize=(15, 6))
  yPrices.set_title(ticker)

  yPrices.set_xlabel('Date')
  yPrices.set_ylabel('Prices')
  yPrices.plot(dates, prices)

  for s in setUpLines:
    yPrices.axhline(
      y = percentile(prices, s[0] * 100),
      linestyle = s[1]
    )
    plt.text(s[0] * 100, .5, 'hello')
  yPrices.tick_params(axis='y')

  color = 'tab:orange'
  yRates = yPrices.twinx()
  yRates.set_ylabel('Rates')
  yRates.plot(dates, rates, color=color)
  for s in setUpLines:
    yRates.axhline(
      y = percentile(rates, (1 - s[0]) * 100),
      linestyle = s[1],
      color = color
    )
  yRates.tick_params(axis='y')

  fig.tight_layout()
  plt.show()