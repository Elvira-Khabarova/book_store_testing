from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(15)
driver.execute_script("window.scrollBy(0, 600);")
ruby_btn=driver.find_element_by_partial_link_text("Selenium Ruby")
ruby_btn.click()
reviews_btn=driver.find_element_by_css_selector(".reviews_tab>a")
reviews_btn.click()
star5_btn=driver.find_element_by_class_name("star-5")
star5_btn.click()
comment_text=driver.find_element_by_id("comment")
comment_text.send_keys("Nice book!")
name_btn=driver.find_element_by_id("author")
name_btn.send_keys("Tester")
email_btn=driver.find_element_by_id("email")
email_btn.send_keys("tester@gmail.com")
submit_btn=driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()