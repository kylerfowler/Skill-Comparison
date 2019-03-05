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

names = []
stats = []

# groups names by sport to be used in color coding
track = ["Joey", "Marc"]
tennis = ["Ryan", "Sam"]
golf = ["Evan"]
baseball = ["Kyle"]
volleyball = ["Justin", "Dan"]

row = input("Choose a row: ")
# iterates though each stat in a row and converts it to and int before adding to a list
i = 1
while i <= 8:
	if sheet.row_values(row)[i] != 'NA':
		stats.append(int(sheet.row_values(row)[i]))
		names.append(sheet.row_values(1)[i])
		sleep(.15)
	i += 1

# sets up bar chart
bar = plt.bar(names, stats, width=.5)

# color codes bar chart
m = 0
while m < len(names):
	if names[m] in track:
		bar[m].set_color('#f4cccc')
		
	elif names[m] in tennis:
		bar[m].set_color('#fff2cc')
		
	elif names[m] in golf:
		bar[m].set_color('#d9ead3')
		
	elif names[m] in baseball:
		bar[m].set_color('#cfe2f3')
		
	elif names[m] in volleyball:
		bar[m].set_color('#d9d2e9')
		
	m += 1

# graphs the bar chart
plt.xlabel("Name")
plt.ylabel(sheet.row_values(row)[0])
plt.show(bar)