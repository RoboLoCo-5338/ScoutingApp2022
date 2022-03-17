import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("RoboLoco-Scouting-Test").sheet1

data = sheet.get_all_records()
print(data)
row = sheet.row_values(2)
col = sheet.col_values(2)
cell = sheet.cell(2, 2).value
sheet.update_cell(2, 2, str(int(cell) - 1))
cell = sheet.cell(2, 2).value

pprint(cell)