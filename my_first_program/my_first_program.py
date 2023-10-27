# Вариант №1. Настраиваемый
'''
определяем функцию about_me, которая принимает два аргумента.
:name - строка, в которой содержиться имя
:age - целое число, возраст
возращает f-строку.
'''
def about_me(name: str, age: int) -> str:
    # возвращение строки
    return f'Меня зовут {name}. Мне {age}.'

# обработчик ошибок
try:
    # определяем переменную name, в которой будет строка с именем
    # определяем переменную age, в которой будет целое число с возрастом
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    # вывод результатов функции
    print(about_me(name, age))
# обработка ошибки ввода переменной age (когда age не целое число)
except ValueError:
    # вывод в случае ошибки
    print('Возраст только в целых числах!')

# Вариант №2. Постоянный
# определяем переменную name, в которой будет строка с именем
# name = "Павел"
# определяем переменную age, в которой будет целое число с возрастом
# age = 14
# выводим переменные через f-строку
# print(f'Меня зовут {name}. Мне {age} лет.')


# Вариант №3. Сокращенный
'''
получаем аргументы и выводим результат анонимной функции (лямбды)
сама функция принимает 2 аргумента
:name - строка, в которой содержиться имя
:age - целое число, возраст
возращает строку.
'''
# print((lambda name, age: f'Меня зовут {name}. Мне {age}.')(input("Введите имя: "), int(input("Введите возраст"))))