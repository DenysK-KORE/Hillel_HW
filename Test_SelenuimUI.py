from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

"""
docker run -d -p 4444:4444 -p 5900:5900 --shm-size=2g --name first_web-test_chrome selenium/standalone-chrome-debug
"""


## Test 1 User creation


# additional value
userName = 'admin'
password = 'admin123'
newUser = 'Denys.Kliuchanskyi'
newUserPassword = 'qwer12344!@#$'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)
# main website
login_url = 'https://www.aqa.science/admin/login/?next=/admin/'
driver.get(login_url)

# Xpaths
username_field_xpath = '//*[@id="id_username"]'
password_field_xpath = '//*[@id="id_password"]'
login_button_xpath = '//*[@id="login-form"]/div[3]/input'
user_folder_xpath = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
add_user_button_xpath = '//*[@id="content-main"]/ul/li/a'
set_new_user_name_xpath = '//*[@id="id_username"]'
set_password_for_new_user_xpath = '//*[@id="id_password1"]'
set_password_confirmation_for_new_user_xpath = '//*[@id="id_password2"]'
save_button_xpath = '//*[@id="user_form"]/div/div/input[1]'
success_message = '//*[@id="main"]/div/ul/li/text()[2]'

# Login page
login_field = driver.find_element(By.XPATH, username_field_xpath)
password_field = driver.find_element(By.XPATH, password_field_xpath)
login_button = driver.find_element(By.XPATH, login_button_xpath)

login_field.send_keys(userName)
password_field.send_keys(password)
login_button.click()

# Admin panel
users_folder = driver.find_element(By.XPATH, user_folder_xpath)
users_folder.click()

add_user_button = driver.find_element(By.XPATH, add_user_button_xpath)
add_user_button.click()

# Add new user page
new_user_username = driver.find_element(By.XPATH, set_new_user_name_xpath)
new_user_password = driver.find_element(By.XPATH, set_password_for_new_user_xpath)
new_user_password_confirmation = driver.find_element(By.XPATH, set_password_confirmation_for_new_user_xpath)

new_user_username.send_keys(newUser)
new_user_password.send_keys(newUserPassword)
new_user_password_confirmation.send_keys(newUserPassword)

save_button = driver.find_element(By.XPATH, save_button_xpath)
save_button.click()

try:
    element = WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.XPATH, '//*[@id="content"]/h2')))
    print('User created')
except:
    assert print('Something went wrong # 1')
finally:
    driver.close()



# Test 2 Find user from first case

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)
# main website
login_url = 'https://www.aqa.science/admin/login/?next=/admin/'
driver.get(login_url)

# Xpaths
username_field_xpath = '//*[@id="id_username"]'
password_field_xpath = '//*[@id="id_password"]'
login_button_xpath = '//*[@id="login-form"]/div[3]/input'
user_folder_xpath = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'

# Login page
login_field = driver.find_element(By.XPATH, username_field_xpath)
password_field = driver.find_element(By.XPATH, password_field_xpath)
login_button = driver.find_element(By.XPATH, login_button_xpath)

login_field.send_keys(userName)
password_field.send_keys(password)
login_button.click()

# Admin panel
users_folder = driver.find_element(By.XPATH, user_folder_xpath)
users_folder.click()

try:
    element = WebDriverWait(driver, 10).until(ES.element_to_be_clickable((By.XPATH, '//*[@id="result_list"]/tbody/tr[2]/th/a')))
    print('User found')
except:
    assert print('Something went wrong # 2')
finally:
    driver.close()


# Test 3 Update user info

first_name = 'Denys'
last_name = 'Kliuchanskyi'
email_address = 'denys@typliu.inogda'

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)
# main website
login_url = 'https://www.aqa.science/admin/login/?next=/admin/'
driver.get(login_url)

# Xpaths
username_field_xpath = '//*[@id="id_username"]'
password_field_xpath = '//*[@id="id_password"]'
login_button_xpath = '//*[@id="login-form"]/div[3]/input'
user_folder_xpath = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
select_user_text = 'Denys.Kliuchanskyi'
first_name_field_xpath = '//*[@id="id_first_name"]'
last_name_xpath = '//*[@id="id_last_name"]'
email_address_xpath = '//*[@id="id_email"]'
edit_save_button_xpath = '//*[@id="user_form"]/div/div/input[1]'

# Login page
login_field = driver.find_element(By.XPATH, username_field_xpath)
password_field = driver.find_element(By.XPATH, password_field_xpath)
login_button = driver.find_element(By.XPATH, login_button_xpath)

login_field.send_keys(userName)
password_field.send_keys(password)
login_button.click()

# Admin panel
users_folder = driver.find_element(By.XPATH, user_folder_xpath)
users_folder.click()

# Find User by Name
find_user_by_name = driver.find_element(By.XPATH, "//*[contains(text(), 'Denys.Kliuchanskyi')]")
find_user_by_name.click()

# Fill selected fields

first_name_field = driver.find_element(By.XPATH, first_name_field_xpath)
last_name_filed = driver.find_element(By.XPATH, last_name_xpath)
email_field = driver.find_element(By.XPATH, email_address_xpath)
edit_save_button = driver.find_element(By.XPATH, edit_save_button_xpath)

first_name_field.send_keys(first_name)
last_name_filed.send_keys(last_name)
email_field.send_keys(email_address)

edit_save_button.click()

try:
    element = WebDriverWait(driver, 10).until(ES.text_to_be_present_in_element((By.XPATH, '//*[@id="result_list"]/tbody/tr[2]/td[2]'), 'denys@typliu.inogda'))
    print('User found with added info')
except:
    assert print('Something went wrong # 3')
finally:
    driver.close()

# Test 4 Deleting created user

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              options=options)
# main website
login_url = 'https://www.aqa.science/admin/login/?next=/admin/'
driver.get(login_url)

# Xpaths
username_field_xpath = '//*[@id="id_username"]'
password_field_xpath = '//*[@id="id_password"]'
login_button_xpath = '//*[@id="login-form"]/div[3]/input'
user_folder_xpath = '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
select_user_text = 'Denys.Kliuchanskyi'
delete_button_xpath = '//*[@id="user_form"]/div/div/p/a'
are_you_sure_page_confirm_button_xpath = '//*[@id="content"]/form/div/input[2]'

# Login page
login_field = driver.find_element(By.XPATH, username_field_xpath)
password_field = driver.find_element(By.XPATH, password_field_xpath)
login_button = driver.find_element(By.XPATH, login_button_xpath)

login_field.send_keys(userName)
password_field.send_keys(password)
login_button.click()

# Admin panel
users_folder = driver.find_element(By.XPATH, user_folder_xpath)
users_folder.click()


# Find User by Name
find_user_by_name = driver.find_element(By.XPATH, "//*[contains(text(), 'Denys.Kliuchanskyi')]")
find_user_by_name.click()

# Deleting user
delete_button = driver.find_element(By.XPATH, delete_button_xpath)
delete_button.click()

# Click confirm button

confirm_button = driver.find_element(By.XPATH, are_you_sure_page_confirm_button_xpath)
confirm_button.click()

try:
    element = WebDriverWait(driver, 10).until(ES.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/ul/li')))
    print('User delited')
except:
    assert print('Something went wrong # 4')
finally:
    driver.close()