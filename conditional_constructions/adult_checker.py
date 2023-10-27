if __name__ == '__main__':
    try:
        is_adult = lambda age: age >= 18
        age = int(input("Введите свой возраст: "))
        print(['Вы несовершеннолетний(я)', 'Вы совершеннолетний(я)'][is_adult(age)])
    except ValueError:
        print('Возраст это целое число!')