import subprocess
import yaml
from selenium import webdriver
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytesseract

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "download.default_directory": "C:\\x\\", # put the directory you want files to be downloaded in
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1280x720")
driver = webdriver.Chrome(options=chrome_options)


def get_credentials():   # create a login.yml file with your own slcm user and password 
    conf = yaml.safe_load(open("login.yml"))
    myslcmUsername = conf["slcm_user"]["username"]
    myslcmPassword = conf["slcm_user"]["password"]
    return myslcmUsername, myslcmPassword


def login(
    url,
    usernameId,
    username,
    passwordId,
    password,
    submit_buttonId,
    captchaId,
    imgCaptcha,
):
    # driver.maximize_window()
    driver.delete_all_cookies()
    driver.get(url)
    driver.find_element("id", usernameId).send_keys(username)
    driver.find_element("id", passwordId).send_keys(password)

    img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, imgCaptcha))
    )

    driver.save_screenshot("screenshot.png")

    image = Image.open("screenshot.png")
    left = 828
    top = 363
    right = left + 250
    bottom = top + 52
    image = image.crop((left, top, right, bottom))
    image.save("captcha.png")

    image = Image.open("captcha.png")
    image2 = image.resize((200, 120))
    image2.save("captchafinal.png")

    captcha_text = pytesseract.image_to_string(Image.open("captchafinal.png"))  # Bypassing captcha
    driver.find_element("id", captchaId).send_keys(captcha_text)
    driver.find_element("id", submit_buttonId).click()
    # driver.implicitly_wait(3)  # seconds
    # error_text = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, errorId))
    # )
    # error_text = driver.find_element("id", errorId).text
    # print("Error: ", error_text)
    if captcha_text == "":
        print("Error in generating captcha, trying again")
        login(
            "https://slcm.manipal.edu/",
            "txtUserid",
            username,
            "txtpassword",
            password,
            "btnLogin",
            "txtCaptcha",
            "imgCaptcha",
        )
    else:
        imp_docs()


def imp_docs():
    test = WebDriverWait(driver, 20).until(    # explicit wait due to varying internet connection speeds
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/form/div[5]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/center/a",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[3]/form/div[5]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/center/a",
    ).click()
    # driver.get("https://slcm.manipal.edu/ImportantDocuments.aspx")
    test = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]",
            )
        )
    )

    latest_title = driver.find_element(
        By.XPATH,
        "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]",
    ).text

    with open("titles.txt", "r") as f:
        last_line = f.readlines()[-1]
        # print("Last Title: ", last_line)
        if latest_title == last_line:
            print("Latest Title: ", latest_title, "\nNo new updates")
            driver.quit()
        else:
            with open("titles.txt", "a") as f:
                f.write("\n")
                latest_title = driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]",
                ).text
                f.write(latest_title)
                latest_title = driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]",
                ).text
                f.write("\n")
                f.write(latest_title)
                latest_title = driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]",
                ).text
                f.write("\n")
                f.write(latest_title)
                driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[4]/td[3]/a",
                ).click()
                driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[3]/td[3]/a",
                ).click()
                driver.find_element(
                    By.XPATH,
                    "/html/body/div[3]/form/div[5]/div/div/div/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[3]/a",
                ).click()
                # print("Latest Title: ", latest_title, "\nNew update found")
            subprocess.run(["python", "mails.py"])
            driver.quit()
        # main.py


myslcmUsername, myslcmPassword = get_credentials()

login(
    "https://slcm.manipal.edu/",
    "txtUserid",
    myslcmUsername,
    "txtpassword",
    myslcmPassword,
    "btnLogin",
    "txtCaptcha",
    "imgCaptcha",
)
