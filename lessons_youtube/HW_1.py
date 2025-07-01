#напешіть функцію яка печатиме текст "Хелло ворлд" якщо передавати у неї пустий рядок
# та "Хелло+те що передаєш" якщо рядок не пустий

def print_hello(x):
    if x != ' ':
        print(f"Hello + {x}")
    else:
        print('Hello world')

print_hello(' ')
print_hello('Vitalii')
