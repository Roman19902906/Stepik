from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
x_element = browser.find_element_by_css_selector("#treasure")
x = x_element.get_attribute("valuex")



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(x))

button = browser.find_element_by_css_selector("#robotCheckbox")
button.click()

button1 = browser.find_element_by_css_selector("#robotsRule")
button1.click()

button2 = browser.find_element_by_css_selector("button.btn")
button2.click()
