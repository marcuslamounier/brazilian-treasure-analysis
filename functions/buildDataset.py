import pandas as pd
from datetime import date

defaultPath = 'outputs/'

def exportDataset(df, outputPath, file, dueDate):
  t = date.today().strftime("%Y-%m-%d")
  filename = outputPath + 'dataset_' + file + str(dueDate)[-2:] + '_' + t + '.csv'
  df.to_csv(filename)

def buildDataset(startYear, file, sheet, dueDate):
  outputPath = defaultPath + file + '/'
  currentYear = date.today().year

  df = pd.DataFrame([])
  for year in range(int(startYear), currentYear + 1):
    temp = pd.read_excel(outputPath + file + '_' + str(year) + '.xls', sheet_name = sheet + ' ' + dueDate)
    cols = pd.array(temp.iloc[0])
    temp.columns = cols
    temp = temp[1:]
    if (year == int(startYear)): df = temp
    else: df = pd.concat([df, temp], ignore_index=True)
  exportDataset(df, outputPath, file, dueDate)
  return df
