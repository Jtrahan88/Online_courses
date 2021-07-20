import pandas as pd
import time

fileNameSS = "Northern Branch Phase II Debris Removal Ops.xlsx"
todaysDate = time.strftime("%m-%d-%y")
print("Opening Vehicle check program.....")
df = pd.read_excel(fileNameSS)

# TODO: SScardCheck  --------------> Checks card locations in SMart Sheets
def SScardCheck(df):
    df = df[['APN', "Debris Crew", "Division", "County", "Debris Crew Leader/Crew#"]]
    df = df.set_index("APN")
    todaysDate = time.strftime("%m-%d-%y")
    df.to_excel("Card Check " + todaysDate + ".xlsx")
# SScardCheck(df)