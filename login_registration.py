from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")  # регистрациия аккаунта
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("reg_email")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("reg_password")
password_btn.send_keys("T!w5o3$")
register_btn=driver.find_element_by_xpath("//input[@name='register']")
register_btn.click()
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")  # логин в систему
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("username")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("password")
password_btn.send_keys("T!w5o3$")
login_btn=driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()
logout_btn=driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_text=logout_btn.text
assert logout_text=="Logout"
driver.quit()