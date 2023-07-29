import yagmail, os, datetime, time
import pandas as pd
from pathlib import Path

SHEET_ID = "your-sheet-id"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"
df = pd.read_csv(url)

recipients_addr = df["Email Address"].tolist()
time.sleep(20)  # to give time for the pdf to be downloaded

def get_modified_files(doc_dir, doc_count=3):
    directory = Path(doc_dir) #creates a path object using the directory
    files = list(directory.glob("*")) #retrieves all the files from the given directory to a list
    files.sort(key=lambda x: x.stat().st_mtime, reverse = True) #sorts the list using modified time, newest first
    return files[:doc_count]; #returns the latest 3 files

titles = []
with open("titles.txt", "r") as f:
    for line in f.readlines()[-3:]:
        titles.append(line.strip())
titles.reverse()
# print(titles)

current_time = datetime.datetime.now()
current_time = (
    str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year)
)
titles[0] = "1. " + titles[0]
titles[1] = "2. " + titles[1]
titles[2] = "3. " + titles[2]

msg = "\n".join([str(elem) for elem in titles])
msg = (
    "Hey there! \n\nA change in the docs was detected just now on SLcM. The 3 most recent titles are:\n"
    + msg
    + "\n\nKindly find the docs attached below.\n\nRegards,\nSLcM Bot\n"
    + current_time
)
yag = yagmail.SMTP("your-email-username", "your-gmail-app-password")  # get yours at https://myaccount.google.com/apppasswords
subject = "New Doc Alert | SLcM Bot"
body = msg
yag.send(
    to=recipients_addr,  # for testing mail just replace the 'to' attribute with a comma separated email list
    subject=subject,
    contents=body,
    attachments=get_modified_files("docs"),
)
