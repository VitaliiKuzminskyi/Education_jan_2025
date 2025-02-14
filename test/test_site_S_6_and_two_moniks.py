#цей тест спілкується з зовнішними файлами homepage та product


from pages.homepage import HomePage
from pages.product import ProductPage

import time #імпорт модуля засинання (не дуже гарна ідея, але у тесті треба)

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.test_title_is('Samsung galaxy s6')

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)   #чекаєм 2 секунди після кліка по розділу вишче (тому що не встигає відобразитися сторінка розділу з моніторами)
    homepage.check_products_count(2)




