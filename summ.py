import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = " http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("num1").text
print(x)
y = browser.find_element_by_id("num2").text
print(y)

def calc(x,y):
  return str(int(x)+int(y))

sum = calc(x,y)
print(sum)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum)


button = browser.find_element_by_css_selector("button.btn")
button.click()

