
import pytest
from selenium.webdriver.chrome.options import Options #для не візуального запуску хрома з гіта
from selenium import webdriver

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')  #запуск невідімого хрому
    browser = webdriver.Chrome(options=options)    #відкриває хром
    browser.maximize_window()   #розвертає вікно на увесь экран
    browser.implicitly_wait(3)  #якщо браузер відкриє сторінку і там не буде того що він шукє, він ще 3 секунди буде намагатися це зробити, потім пофейлить
    yield browser   #після закінчення тесту браузер закривається ( після yield: Виконуєш дії для очищення або звільнення ресурсу (це важливо для закриття браузера, видалення тимчасових файлів тощо))
    browser.close() #закриває браузер

