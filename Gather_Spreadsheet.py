import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from time import sleep

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Skills-Comparison.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Skills-Comparison-Spreadsheet").sheet1

statNames = sheet.col_values(1)[1:]
names = sheet.row_values(1)[1:]
stats = []
# Gets stats from each row
i = 2
while i <= 55:
    stats.append(sheet.row_values(i)[1:])
    # Sleeps to stop google from shitting itself over to many queries per second
    sleep(.1)
    i += 1

# Make sure you use the right name here.
sheet = client.open("Skills-Comparison-Spreadsheet").sheet1

# Convert cell values to a pandas data frame
dataframe = pd.DataFrame(stats, index=statNames, columns=names)
print(dataframe)
