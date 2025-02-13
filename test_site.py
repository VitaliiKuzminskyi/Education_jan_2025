import pytest
from selenium import webdriver  #обращение к вебдрайверу в селениуме
from selenium.webdriver.common.by import  By #импортує усі способи пошуку елементів під капотом


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()    #відкриває хром
    browser.maximize_window()   #розвертає вікно на увесь экран
    browser.implicitly_wait(3)  #якщо браузер відкриє сторінку і там не буде того що він шукє, він ще 3 секунди буде намагатися це зробити, потім пофейлить
    yield browser   #після закінчення тесту браузер закривається ( після yield: Виконуєш дії для очищення або звільнення ресурсу (це важливо для закриття браузера, видалення тимчасових файлів тощо))
    browser.close() #закриває браузер

def test_open_s6(browser):
    browser.get('https://demoblaze.com/')   #у функції відкрившій браузер переходим на вказану сторінку
    galaxy_s6 = browser.find_element(By.XPATH, '//a[text()= "Samsung galaxy s6"]')   #створюєм змінну galaxy_s6 куди зберігаєм те що знайшли під капотом за Xpath, де а це силка пыд капотом браузеоа
    galaxy_s6.click()   #клікаєм по змінній

    title_galaxy_s6 = browser.find_element(By.CSS_SELECTOR, 'h2') #створюєм змінну title_galaxy_s6 куди зберігаєм те що знайшли під капотом з CSS за унікальним тегом h2
    assert title_galaxy_s6.text == 'Samsung galaxy s6'   #тестуєм що ми знайшли текстовий заголовок (змінна.text) заголовк з потрібним нам текстом