import os 
from selenium import webdriver
import math

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 


print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_xpath('//input[@placeholder="Введите имя"]')
name.send_keys("tret")
lastname = browser.find_element_by_xpath('//input[@placeholder="Введите фамилию"]')
lastname.send_keys("tret")
email = browser.find_element_by_xpath('//input[@placeholder="Введите Email"]')
email.send_keys("tut@tut.by")

file = browser.find_element_by_id("file")
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()