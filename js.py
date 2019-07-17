from selenium import webdriver
import math
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_id("input_value").text

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)


input = browser.find_element_by_tag_name("input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)


answer = browser.find_element_by_id("answer")
answer.send_keys(y)

d = browser.find_element_by_css_selector("[for='robotCheckbox']")
d.click()
c = browser.find_element_by_css_selector("[for='robotsRule']")
c.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView();


