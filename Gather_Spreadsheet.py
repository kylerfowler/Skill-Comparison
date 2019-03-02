import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Skills-Comparison.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Skills-Comparison-Spreadsheet").sheet1

# Extract and print all of the values in a specific range of cells
cell_list = sheet.range("B2:I55")
for cell in cell_list:
	print(cell.value)