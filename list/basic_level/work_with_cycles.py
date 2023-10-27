if __name__ == '__main__':
    try:
        number, is_cond = int(input('Введите число: ')), False
        conditions = [number % 3 == 0, number > 10]
        for i in range(len(conditions)):
            if not conditions[i]: continue
            print(["Число делится на 3", "Число больше 10"][i == 1])
            is_cond = True
        print('Число не соответствует условиям') if not is_cond else ''
    except ValueError:
        print('Значение должно быть целым числом!')
