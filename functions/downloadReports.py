from datetime import date
from os.path import exists
from os import remove, mkdir
import wget

baseUrl = "https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/sistd/"

def downloadReport(year, url, output):
  fullUrl = baseUrl + str(year) + '/' + url + '_' + str(year) + '.xls'
  wget.download(fullUrl, output)

def downloadReports(startYear, sheet, url):
  currentYear = date.today().year
  pathOutput = 'outputs/' + sheet

  if not exists(pathOutput): mkdir(pathOutput)
  
  for year in range(int(startYear), currentYear):
    fileOutput = pathOutput + '/' + sheet + '_' + str(year) + '.xls'
    if not exists(fileOutput): downloadReport(year, url, fileOutput)

  fileOutput = pathOutput + '/' + sheet + '_' + str(currentYear) + '.xls'
  if exists(fileOutput): remove(fileOutput)
  downloadReport(currentYear, url, fileOutput)

  print('\nData extracted . . .')