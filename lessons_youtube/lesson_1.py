
my_number = 3333    #intenger
my_number_2 = 123.4     #float


print(3333)
print(my_number)

print('text')
my_text = 'text'

print('123.4')
print(my_number_2)

var1 = True
var2 = False

print('________')

text1 = 'life'
text2 = 'is'
text3 = 'beatiful'
print(text1 + ' ' + text2 + ' ' + text3)

print('________')

a = 5
b = 7
print(a + b)
result_a_b = a + b
print(result_a_b)

print('________')

k = 42
l = 57
m = 83
n = 14
#x * 2 ** 2 / 2 + y
print(k * 2 ** 3 / 2 + l)
print(l * 2 ** 3 / 2 + m)
print(m * 2 ** 3 / 2 + n)
print(n * 2 ** 3 / 2 + k)

print('_')

def calculate(x, y):        #пишем условие и функцию. (х, у) - то что ожидается в функции
    print(x * 2 ** 3 / 2 + y)
calculate(k, l)         #вызываем функцию (запускаем)
calculate(l, m)         #вызываем функцию (запускаем)
calculate(m, n)         #вызываем функцию (запускаем)
calculate(n, k)         #вызываем функцию (запускаем)

print('_')

def calculate_2(x, y):
    result = x * 2 ** 3 / 2 + y
    return result
result_k_l = calculate_2(k, l)      #результат записываем в переменную
print(result_k_l)     #печать результата функции с переменной
print(calculate_2(k, l))        #печать результата функции без переменной, пишем название функции с переменными для вычисления

print('_')

def work():      #функция в которую не нужно ничего передовать, всё что ей нужно уже у неё есть - () в скобочках пусто
    print('I am working')
work()

print('________')

# если о меньше 5 то напечатать 'Привет', иначе напечатать 'Пока'
o = 4.9
if o < 5:
    print('Привет')
else:
    print('Пока')

print('_')

# если о меньше 5 то напечатать 'Привет', если значение от 5 до 10 печатать "Привет-привет" иначе напечатать 'Пока'

o = 5
if o < 5:
    print('Привет')
elif 5 <= o and o < 10:
    print('Привет-привет')
else:
    print('Пока')



