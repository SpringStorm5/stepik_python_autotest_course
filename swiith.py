from selenium import webdriver
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value").text
print(x)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

