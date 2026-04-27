from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------- CHROME OPTIONS (ANTI-BOT + CRASH FIX) ----------
options = webdriver.ChromeOptions()
'''
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
'''
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.execute_script(
    "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
)

wait = WebDriverWait(driver, 20)

# ---------- TEST CASE 1 ----------
def test_case_1():
    try:
        driver.get("https://www.bing.com")
        wait.until(EC.title_contains("Bing"))
        print("Test Case 1 Passed → Website Opened")
    except:
        print("Test Case 1 Failed")

# ---------- TEST CASE 2 ----------
def test_case_2():
    try:
        global search_box
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        print("Test Case 2 Passed → Search Box Found")
    except:
        print("Test Case 2 Failed")

# ---------- TEST CASE 3 ----------
def test_case_3():
    try:
        search_box.send_keys("Selenium Automation")
        print("Test Case 3 Passed → Text Entered")
    except:
        print("Test Case 3 Failed")

# ---------- TEST CASE 4 ----------
def test_case_4():
    try:
        global current_url
        current_url = driver.current_url

        search_button = wait.until(
            EC.element_to_be_clickable((By.ID, "search_icon"))
        )
        search_button.click()

        wait.until(EC.url_changes(current_url))

        print("Test Case 4 Passed → Search Clicked")
    except:
        print("Test Case 4 Failed")

# ---------- TEST CASE 5 ----------
def test_case_5():
    try:
        wait.until(
            EC.visibility_of_element_located((By.ID, "b_results"))
        )
        print("Test Case 5 Passed → Results Loaded")
    except:
        print("Test Case 5 Failed")

# ---------- RUN ALL ----------
test_case_1()
time.sleep(2)

test_case_2()
time.sleep(2)

test_case_3()
time.sleep(2)

test_case_4()
time.sleep(5)

test_case_5()

time.sleep(10)
driver.quit()
