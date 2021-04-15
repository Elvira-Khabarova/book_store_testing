from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") #отображение, скидка товара
driver.implicitly_wait(15)
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("username")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("password")
password_btn.send_keys("T!w5o3$")
login_btn=driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
html_btn=driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
html_btn.click()
html5forms_btn=driver.find_element_by_xpath("//*[@id='content']/ul/li[1]/a[1]/h3")
html5forms_btn.click()
title_book=driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
title=title_book.text
assert title=="HTML5 Forms"
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") #количество товаров в категории
driver.implicitly_wait(15)
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("username")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("password")
password_btn.send_keys("T!w5o3$")
login_btn=driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
html_btn=driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a")
html_btn.click()
number_product=driver.find_elements_by_css_selector(".product_tag-html")
number=len(number_product)
assert number==3
driver.quit()


from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") #сортировка товаров
driver.implicitly_wait(15)
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("username")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("password")
password_btn.send_keys("T!w5o3$")
login_btn=driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
selector_btn=driver.find_element_by_class_name("orderby")
selector_default=selector_btn.get_attribute("value")
assert selector_default=="menu_order"
select=Select(selector_btn)
select.select_by_value("price-desc")
selector_btn=driver.find_element_by_class_name("orderby")
selector_desc=selector_btn.get_attribute("value")
assert selector_desc=="price-desc"
driver.quit()



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") #отображение, скидка товара
driver.implicitly_wait(15)
account_btn=driver.find_element_by_link_text("My Account")
account_btn.click()
username_btn=driver.find_element_by_id("username")
username_btn.send_keys("one@gmail.com")
password_btn=driver.find_element_by_id("password")
password_btn.send_keys("T!w5o3$")
login_btn=driver.find_element_by_xpath("//input[@name='login']")
login_btn.click()
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
android_quick=driver.find_element_by_css_selector("a.woocommerce-LoopProduct-link > h3")
android_quick.click()
old_price=driver.find_element_by_css_selector(".entry-summary > div:nth-child(2) > p > del > span")
old_price_check=old_price.text
assert old_price_check=="₹600.00"
new_price=driver.find_element_by_css_selector(".entry-summary > div:nth-child(2) > p > ins > span")
new_price_check=new_price.text
assert new_price_check=="₹450.00"
driver.implicitly_wait(0)
preview = WebDriverWait(driver, 15).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div.images > a > img")) )
preview.click()
preview_close = WebDriverWait(driver, 15).until(
EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
preview_close.click()
driver.quit()


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") # проверка цены в корзине
driver.implicitly_wait(15)
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
#html5web_btn=driver.find_element_by_css_selector(" li.post-182 > a.woocommerce-LoopProduct-link > h3")
#html5web_btn.click()
# товара не оказалось на складе, купим другую книгу
javascript_btn=driver.find_element_by_css_selector("#content > ul > li.post-165 > a.woocommerce-LoopProduct-link > h3")
javascript_btn.click()
add_btn=driver.find_element_by_class_name("single_add_to_cart_button")
add_btn.click()
item=driver.find_element_by_class_name("cartcontents")
item_number=item.text
assert item_number=="1 Item"
amount=driver.find_element_by_class_name("amount")
item_amount=amount.text
assert item_amount=="₹350.00"
basket_btn=driver.find_element_by_css_selector("#wpmenucartli > a > i")
basket_btn.click()
driver.implicitly_wait(0)
wait=WebDriverWait(driver, 15)
subtotal_cost=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-subtotal > td > span")))
subtotal=subtotal_cost.text
assert subtotal=="₹350.00"
# На странице есть два Total. Проверим Total в разделе Basket Totals
total_cost=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.order-total > td > strong > span")))
total=total_cost.text
if total=="₹350.00":
    print("в Total отобразилась стоимость")
else:
    print("в Total отобразилась сумма стоимости и роуминга")
driver.quit()


import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/") #работа в корзине
driver.implicitly_wait(15)
shop_btn=driver.find_element_by_css_selector("#menu-item-40 > a")
shop_btn.click()
#jsdata_btn=driver.find_element_by_css_selector(" li.post-180 > a.woocommerce-LoopProduct-link > h3")
#jsdata_btn.click()
# товара не оказалось на складе, купим другую книгу
driver.execute_script("window.scrollBy(0, 300);")
javascript_btn=driver.find_element_by_css_selector("#content > ul > li.post-165 > a.woocommerce-LoopProduct-link > h3")
javascript_btn.click()
driver.implicitly_wait(0)
add_btn=driver.find_element_by_class_name("single_add_to_cart_button")
add_btn.click()
time.sleep(5)
basket_btn=driver.find_element_by_css_selector("#wpmenucartli > a > i")
basket_btn.click()
time.sleep(3)
del_btn=driver.find_element_by_css_selector("tr.cart_item > td.product-remove > a")
del_btn.click()
time.sleep(3)
undo_btn=driver.find_element_by_css_selector(".woocommerce-message > a")
undo_btn.click()
quantity_btn=driver.find_element_by_css_selector("td.product-quantity > div > input").clear()
quantity=driver.find_element_by_css_selector(".cart_item > td.product-quantity > div > input")
quantity.send_keys("3")
time.sleep(3)
update_btn=driver.find_element_by_xpath("//input[@name='update_cart']")
update_btn.click()
quantity=driver.find_element_by_css_selector(".cart_item > td.product-quantity > div > input")
quantity_number=quantity.get_attribute("value")
assert quantity_number=="3"
time.sleep(3)
apply_btn=driver.find_element_by_xpath("//input[@name='apply_coupon']")
apply_btn.click()
message=driver.find_element_by_link_text("Please enter a coupon code.")
message_text=message.text
assert message_text=="Please enter a coupon code."
driver.quit()