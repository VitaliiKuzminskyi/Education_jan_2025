# бот который сохраняет атрибут мема в файл lesson_6.txt
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()              #добавляем переменную в которой команда открывает браузер хром

driver.get('https://9gag.com/trending')

first_mame = driver.find_element(By.CLASS_NAME, 'badge-evt')
first_mame.get_attribute('href')
first_meme_url = (first_mame.get_attribute('href'))

with open ('lesson_6.txt', 'w') as meme_file:
    meme_file.write(first_meme_url)



