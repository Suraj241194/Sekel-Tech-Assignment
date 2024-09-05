from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
import time


options = Options()
options.add_experimental_option("detach", True) # This will leave the browser open even after all the tasks on the browser are completed
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install())
                          ,options = options)

driver.maximize_window()


# Test scenario 1 :  User Login

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Username']"))).click()


username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.click()
password.send_keys("admin123")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
login_button.click()

driver.implicitly_wait(5)

if driver.find_element(By.XPATH, "//span[normalize-space()='Admin']"):
    print("Test Case Scenario 1 completed. Login Successful!")

# Test scenario 2 : User management search

click_admin = driver.find_element(By.XPATH, "//span[normalize-space()='Admin']")
click_admin.click()
click_username = driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
click_username.click()
input_name = input("Enter the username.")
driver.implicitly_wait(10)
click_username.send_keys(input_name)
click_search = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
click_search.click()
driver.implicitly_wait(4)

# user_not_present = driver.find_element(By.XPATH, "//span[normalize-space()='No Records Found']")
try:
    if driver.find_element(By.XPATH, "(//div[contains(text(),'Enabled')])[1]"):
        print("Test Case Scenario 2 completed. User found !")
except NoSuchElementException:
    print("Test Case Scenario 2 completed. User not found !")
    pass


# Test Scenario 3 : Add to new user

add_user = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
add_user.click()

wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")))
click_user_role = driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[1]")
click_user_role.click()
# driver.implicitly_wait(1)
click_user_role.send_keys(Keys.ARROW_DOWN)
# driver.implicitly_wait(2)
click_user_role.send_keys(Keys.RETURN)

# click_admin = driver.find_element(By.XPATH, "//div[contains(text(),'Admin')]")
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Admin')]")))
# click_admin.click()



input_employee_name = input("Enter employee name.")
click_employee_name_search = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
click_employee_name_search.send_keys(input_employee_name)

click_employee_name_search.send_keys(Keys.RETURN)
time.sleep(10)
click_employee_name_search.send_keys(Keys.ARROW_DOWN)
click_employee_name_search.send_keys(Keys.RETURN)






click_search_status = driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])")
click_search_status.click()
click_search_status.send_keys(Keys.ARROW_DOWN)
click_search_status.send_keys(Keys.RETURN)

click_add_username = driver.find_element(By.XPATH, "//div[@class='oxd-form-row']//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
add_username = input("Enter Username ")
click_add_username.send_keys(add_username)
time.sleep(3)

click_add_password = driver.find_element(By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
click_add_password.click()
add_password = input("Add Password ")
click_add_password.send_keys(add_password)

click_confirm_password = driver.find_element(By.XPATH, "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@type='password']")
click_confirm_password.send_keys(add_password)
time.sleep(3)
click_save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
click_save.click()

time.sleep(6)

try:
    driver.find_element(By.XPATH, "//span[normalize-space()='Invalid']")
    print("Please enter a valid employee name.")

except NoSuchElementException:
    driver.find_element(By.XPATH, "//div[contains(text()," + "'" + add_username + "')]")
    print("User successfully added.")

print("Test Case Scenario 3 completed. User added !")

