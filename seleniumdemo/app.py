from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- SETUP ----------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 15)

driver.get("https://demoqa.com/buttons")

# ---------- TEST CASE 1 : OPEN ELEMENTS ----------
try:
    driver.get("https://demoqa.com/checkbox")

    home_checkbox = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='rct-checkbox']"))
    )
    home_checkbox.click()

    print("Test Case 1 Passed → Checkbox Selected")
except:
    print("Test Case 1 Failed")

time.sleep(2)


# ---------- TEST CASE 2 : CHECKBOX ----------
try:
    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    )
    print("Test Case 2 Passed → Checkbox Verified")
except:
    print("Test Case 2 Failed")

time.sleep(2)

# ---------- TEST CASE 3 : RADIO BUTTON ----------
try:
    radio_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Radio Button']"))
    )
    radio_btn.click()

    yes_radio = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='yesRadio']"))
    )
    yes_radio.click()

    print("Test Case 3 Passed → Radio Button Selected")
except:
    print("Test Case 3 Failed")

time.sleep(2)

# ---------- TEST CASE 4 : WEB TABLE OPEN ----------
try:
    web_table = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Web Tables']"))
    )
    web_table.click()

    print("Test Case 4 Passed → Web Table Opened")
except:
    print("Test Case 4 Failed")

time.sleep(2)

# ---------- TEST CASE 5 : ADD NEW RECORD ----------
try:
    add_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
    )
    add_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys("Surekha")
    driver.find_element(By.ID, "lastName").send_keys("AI")
    driver.find_element(By.ID, "userEmail").send_keys("surekha@test.com")
    driver.find_element(By.ID, "age").send_keys("25")
    driver.find_element(By.ID, "salary").send_keys("50000")
    driver.find_element(By.ID, "department").send_keys("Testing")

    submit = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].scrollIntoView();", submit)
    time.sleep(1)
    submit.click()

    print("Test Case 5 Passed → Record Added in Web Table")
except:
    print("Test Case 5 Failed")

time.sleep(8)
driver.quit()
