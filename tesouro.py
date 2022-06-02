import pandas as pd
from datetime import date
import wget
from os.path import exists
from os import remove, mkdir

baseUrl = "https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/sistd/"

print('Brazilian Treasure Data Extractor')
print('-------------')
print('Titles')

titles = pd.read_csv('inputs/titles.csv')
nTitles = len(titles['Title'])
for i in range(nTitles):
	print('[ ', i + 1, ' ] -', titles['Title'][i])
print('-------------')

print('Type the NUMBER according with the title you want to extract AND press ENTER')
option = -1
while (option < 1 or option > nTitles):
	option = int(input('Type here: '))
	if (option < 1 or option > nTitles):
		print('Please insert a valid option')

option -= 1
tdTitle = titles['Title'][option]
tdSheetName = titles['sheetName'][option]
tdUrlName = titles['urlName'][option]
tdCsvName = titles['csvName'][option]

print('-------------')
dues = pd.read_csv('inputs/'+tdCsvName+'.csv')
print('Expiry year for', tdTitle, 'titles:')
for i in range(len(dues['Year'])):
	print('[ ', i + 1, ' ] -', dues['Year'][i])

print('Type the NUMBER according with the expiry date you want to extract AND press ENTER')
option = -1
while (option < 1 or option > nTitles):
	option = int(input('Type here: '))
	if (option < 1 or option > nTitles):
		print('Please insert a valid option')

option -= 1
tdYear = dues['Year'][option]
tdStart = dues['Start'][option]
tdDuedate = dues['Duedate'][option]

currentYear = date.today().year
pathOutput = 'outputs/' + tdCsvName

if not exists(pathOutput):
	mkdir(pathOutput)

for year in range(int(tdStart), currentYear):
	fileOutput = pathOutput + '/' + tdCsvName + '_' + str(year) + '.xls'
	if not exists(fileOutput):
		response = wget.download(
			baseUrl + str(year) + '/' + tdUrlName + '_' + str(year) + '.xls',
			fileOutput
		)

fileOutput = pathOutput + '/' + tdCsvName + '_' + str(currentYear) + '.xls'
if exists(fileOutput):
	remove(fileOutput)
response = wget.download(
	baseUrl + str(currentYear) + '/' + tdUrlName + '_' + str(currentYear) + '.xls',
	fileOutput
)
