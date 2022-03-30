import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    browser.implicitly_wait(15)
    text = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket").text
    time.sleep(15)
    assert bool(text) == True, "Кнопка не найдена"
