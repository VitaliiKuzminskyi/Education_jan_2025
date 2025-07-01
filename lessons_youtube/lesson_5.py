#програма видаляє файли з певною назвою у певному каталозі, тут це файли з ім'ям в котрий входить текст 'responce.json'

import os

directory_path = 'C:\\Users\\vitaliy.kuzminskiy\\Downloads'

directory_content = os.listdir(directory_path)
print(directory_content)

for filename in directory_content:
    if filename.endswith('responce.json'):
        print(filename)
        # os.remove(directory_path + '/' + filename)            #1 видалить все в папці directory_path та зветься filename
        os.remove((os.path.join(directory_path, filename)))     #2 видалить все в папці directory_path та зветься filename

#для запуску з вікна віндоуз - відкриваєм потрібну папку, Шифт+ПКМ у будь-якій області і чеоез вікно повершел запускаєм python lesson_5.py

#для запуску через .bat файл з любого місця, наприклад, з робочого столу треба в файлі ввести оце 'python D:\AQA\education_jan_2025\lessons_youtube\lesson_5.py'


