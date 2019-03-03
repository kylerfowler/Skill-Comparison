import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import numpy as np
from time import sleep

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Skills-Comparison.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Skills-Comparison-Spreadsheet").sheet1

names = sheet.row_values(1)[1:]
stats = []
r = input("Choose a row: ")

#iterates though each stat in a row and converts it to and int before adding to a list
i = 1
while i <= 8:
	stats.append(int(sheet.row_values(r)[i]))
	sleep(.15)
	i += 1

#sets up and graphs bar chart
a = plt.bar(names,stats)
plt.xlabel("Name")
plt.ylabel(sheet.row_values(r)[0])
plt.show(a)