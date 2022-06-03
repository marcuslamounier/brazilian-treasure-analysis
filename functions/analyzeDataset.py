import pandas as pd
from datetime import datetime
from functions.plot import printChart

def datefyArray(arr):
  return [datetime.strptime(d,'%d/%m/%Y').date() for d in arr]

def analyzeDataset(df, ticker, startYear = None):
  df['Taxa Compra Manhã'] *= 100
  df['Dia'] = datefyArray(df['Dia'].to_numpy())
  if (startYear != None):
    df = df.loc[(df['Dia'] >= datetime(startYear, 1, 1).date())]
  printChart(
    ticker,
    df['Dia'],
    df['PU Compra Manhã'],
    df['Taxa Compra Manhã']
  )