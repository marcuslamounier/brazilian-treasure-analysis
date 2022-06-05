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

  fig, yRates = plt.subplots(figsize=(15, 6))
  yRates.set_title(ticker)
  yRates.set_xlabel('Date')

  color = 'tab:orange'
  yRates.set_ylabel(
    'Rates',
    color=color,
    fontsize=14
    )
  yRates.plot(dates, rates, color=color)
  for s in setUpLines:
    yRates.axhline(
      y = percentile(rates, (1 - s[0]) * 100),
      linestyle = s[1],
      color = color
    )
  yRates.tick_params(axis='y', color=color)

  color = 'tab:blue'
  yPrices = yRates.twinx()
  yPrices.set_ylabel(
    'Prices',
    color=color,
    fontsize=14
  )
  yPrices.plot(dates, prices)
  for s in setUpLines:
    yPrices.axhline(
      y = percentile(prices, s[0] * 100),
      linestyle = s[1],
      color = color
    )
  yPrices.tick_params(axis='y', color=color)

  fig.tight_layout()
  plt.show()