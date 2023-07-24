import yagmail, glob, os, datetime, time
import pandas as pd

SHEET_ID = "your-sheet-id"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"
df = pd.read_csv(url)

recipients_addr = df["Email Address"].tolist()

# names=df["Name"].tolist()
files = glob.glob(os.path.expanduser("*.pdf"))

time.sleep(20)  # to give time for the pdf to be downloaded

# Sort by modification time (mtime) ascending and descending
sorted_by_mtime_descending = sorted(files, key=lambda t: -os.stat(t).st_mtime)
# print(sorted_by_mtime_descending)
file_path = sorted_by_mtime_descending[:3]

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
    subject=subject,a
    contents=body,
    attachments=file_path,
)
