# SLcM-Bot
A simple python bot that'll send you an email every time a new document is uploaded on [SLcM.](https://slcm.manipal.edu/)[^1]
- Sends you 3 most recent pdf docs from the SLcM 'Notifications Tab'. 
- Uses Selenium Webdriver.
- Doesn't need your login details. Keep your grades private.
- Took 12+ hours over 3 days to complete. Turns out avoiding logging onto SLcM is the biggest motivator.
- No more 'is this official?', 'wait for confirmation from SC', or any other human delay in communication process.

### Functionality
- Bypasses captcha using [Tesseract OCR](https://pypi.org/project/pytesseract/)
- Checks the 3 most recent notification titles, if any changes are detected, downloads said pdfs and sends it as an email to receiver list.

### Future improvements (Any help is much appreciated)
- Host script on a cloud service and schedule at different times of day. (personally tried sites like pythonanywhere but free options are severely limited for this imo)
- Personalised emails and beautification using HTML.
- Categorise pdfs according to semester,academic year,etc.
- Sending a whatsapp message rather than email.
- This is a non-exhaustive list. Any other ideas at all are always welcome by opening an issue in this repo.

Lastly, do give this repo a ⭐ and help spread the word if you found it interesting.

[Sign up for SLcM Bot here](https://docs.google.com/forms/d/e/1FAIpQLSffSgt0n9C_sEFEo6PRrr_RVsGdW4WPmsjXXMR6OdysC27G3A/viewform)

[^1]:[A rare view of the site.](https://imgur.com/a/du71PuC)


