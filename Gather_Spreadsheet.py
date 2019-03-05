import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt

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
    sleep(.15)
    i += 1

# Make sure you use the right name here.
sheet = client.open("Skills-Comparison-Spreadsheet").sheet1

# Convert cell values to a pandas data frame
df = pd.DataFrame(stats, index=statNames, columns=names)

# Create stat categories
universal = df.loc["Height_(ft-in)":"Team_Wins", "Joey":"Dan"]
track = pd.concat([universal.loc["Height_(ft-in)":"Team_Wins", "Joey":"Marc"], df.loc["1st_Place":"Discus_Throw_(ft-in)", "Joey":"Marc"]])
tennis = pd.concat([universal.loc["Height_(ft-in)":"Team_Wins", "Ryan":"Sam"], df.loc["1st_Place":"3rd_Place", "Ryan":"Sam"], df.loc["Tennis_Aces":"Tennis_Serve_Velocity_(mph)", "Ryan":"Sam"]])
golf = pd.concat([universal.loc["Height_(ft-in)":"Team_Wins", "Evan":"Evan"], df.loc["1st_Place":"3rd_Place", "Evan":"Evan"], df.loc["Drive_Distance_(ft)":"Average Score", "Evan":"Evan"]])
baseball = pd.concat([universal.loc["Height_(ft-in)":"Team_Wins", "Kyle":"Kyle"], df.loc["Plate_Appearances":"Changeup_Velocity_(mph)", "Kyle":"Kyle"]])
volleyball = pd.concat([universal.loc["Height_(ft-in)":"Team_Wins", "Justin":"Dan"], df.loc["Volleyball_Aces":"Volleyball_Serve_Velocity_(mph)", "Justin":"Dan"]])
categories = [universal, track, tennis, golf, baseball, volleyball]
# Test Area
print("Universal:",'\n',universal,'\n')
print("Track:",'\n',track,'\n')
print("Tennis:",'\n',tennis,'\n')
print("Golf:",'\n',golf,'\n')
print("Baseball:",'\n',baseball,'\n')
print("Volleyball:",'\n',volleyball)
# Doesn't Work
