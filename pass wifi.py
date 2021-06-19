import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Pass wifi").sheet1
data = sheet.get_all_records()

#row = sheet.row_values(3)
col = sheet.col_values(1)
#cell = sheet.cell(1,2)
pprint(col)
insertRow = ["nnn"]
sheet.append_row(insertRow)