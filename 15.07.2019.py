from selenium import webdriver
import time
import math

link = " http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute("valuex")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
input = browser.find_element_by_id('answer')
input.send_keys(y)

d = browser.find_element_by_id("robotCheckbox")
d.click()
c = browser.find_element_by_id("robotsRule")
c.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()
