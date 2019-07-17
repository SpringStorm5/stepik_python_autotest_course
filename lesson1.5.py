import math
from selenium import webdriver
link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

a = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(a)
link = browser.find_element_by_link_text(str(a))
link.click()

input2 = browser.find_element_by_name('first_name')
input2.send_keys("Petrov")
input3 = browser.find_element_by_name('last_name')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_name('firstname')
input4.send_keys("Russia")
input1 = browser.find_element_by_id('country')
input1.send_keys("Ivan")
button = browser.find_element_by_xpath("//*[@class='btn btn-default']") 
button.click()
