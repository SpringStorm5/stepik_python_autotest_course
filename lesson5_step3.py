from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input2 = browser.find_element_by_name('first_name')
input2.send_keys("Petrov")
input3 = browser.find_element_by_name('last_name')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_name('firstname')
input4.send_keys("Russia")
input1 = browser.find_element_by_id('country')
input1.send_keys("Ivan")
button = browser.find_element_by_xpath("*//button[contains(text(),'Отправить')]") 
button.click()

