from pandas import read_csv
from functions.analyzeDataset import analyzeDataset
from functions.buildDataset import buildDataset
from functions.downloadReports import downloadReports
from functions.menuFunctions import renderMenu
from datetime import date

print('Welcome to Brazilian Treasure Data Extractor')
print('\n-------------')

titles = read_csv('inputs/titles.csv')
option, index = renderMenu(titles['Title'], 'Choose the Brazilian title')
tdTitle = titles['Title'][index]
tdSheetName = titles['sheetName'][index]
tdUrlName = titles['urlName'][index]
tdCsvName = titles['csvName'][index]

dues = read_csv('inputs/' + tdCsvName + '.csv')
option, index = renderMenu(dues['Year'], 'Choose the expiry year')
tdYear = dues['Year'][index]
tdYearStart = dues['YearStart'][index]
tdDueDate = str(dues['DueDate'][index])
if (len(tdDueDate) == 5): tdDueDate = '0' + tdDueDate

print('Extracting data for Tesouro', tdTitle, tdYear, '. . .')

downloadReports(tdYearStart, tdCsvName, tdUrlName)
print('-------------')

print('Building dataset for Tesouro', tdTitle, tdYear, '. . .')
dataset = buildDataset(tdYearStart, tdCsvName, tdSheetName, tdDueDate)
print('Dataset built . . .')
print('You can access the file for external analysis in outputs path.')
print('-------------')

currentYear = date.today().year
option, index = renderMenu(
  list(range(tdYearStart, currentYear + 1)),
  'From which year should the analysis start?'
)
analyzeDataset(
  dataset,
  ticker = 'Tesouro ' + tdTitle + ' ' + str(tdYear),
  startYear=option
)
