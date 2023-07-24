# SLcM-Bot
A simple python bot that'll send you an email every time a new document is uploaded on [SLcM.](https://slcm.manipal.edu/)[^1]
- Sends you 3 most recent pdf docs from the SLcM 'Notifications Tab'. 
- Uses Selenium Webdriver.
- Doesn't need your login details. Keep your grades private.
- Took 12+ hours over 3 days to complete. Turns out avoiding logging onto SLcM is the biggest motivator.
- No more 'is this official?', 'wait for confirmation from SC', or any other human delay in communication process.
- Obviously this too has its limitations, which'll be apparent over time.

### Functionality
- Bypasses captcha using [Tesseract OCR](https://pypi.org/project/pytesseract/) (SLcM currently uses a 3 digit captcha code like 007,420)
- Checks the 3 most recent notification titles, if any changes are detected, downloads said pdfs and sends it as an email to receiver list.

### Future improvements (Any help is much appreciated)
- Host script on a cloud service and schedule at different times of day. (personally tried sites like pythonanywhere but free options are severely limited for this imo)
- Personalised emails and beautification using HTML.
- Categorise pdfs according to semester,academic year,etc.
- This is a non-exhaustive list. Any other ideas at all are always welcome by opening an issue in this repo.

Lastly, do give this repo a ⭐ if you found it interesting.



[^1]:A highly uncommon occurence in the life of a MIT student.


