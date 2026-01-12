from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



for_number_input = ("hottarudraprasad90@gmail.com")
for_password_input = ("1122334455@")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://www.instagram.com/")
webdriver.maximize_window()



for_number = webdriver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
for_number.send_keys(for_number_input, Keys.ENTER)
for_password = webdriver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
for_password.send_keys(for_password_input, Keys.ENTER)

wait = WebDriverWait(webdriver, 20)

# ---- Save login info: Not now ----
try:
    not_now = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@role='button' and contains(text(),'Not now')]"
        ))
    )
    not_now.click()
    print("✅ Save login info dismissed")
except:
    print("⚠ Save login info popup not found")

# ---- Notifications: Not now ----
try:
    notif_not_now = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[@role='button' and contains(text(),'Not now')]"
        ))
    )
    notif_not_now.click()
    print("✅ Notifications dismissed")
except:
    print("⚠ Notification popup not found")

# Open reels
reels = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/reels')]"))
)
reels.click()

def like_reel(driver):
    try:
        like_btn = driver.find_element(
            By.XPATH,
            "//span//*[name()='svg' and @aria-label='Like']"
        )
        like_btn.click()
        print("❤️ Reel liked")
        return True
    except:
        print("⚠️ Already liked or like button not found")
        return False


for i in range(20):  # like 20 reels max
    sleep(10)  # watch reel like a human

    like_reel(webdriver)

    sleep(3)
    webdriver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)