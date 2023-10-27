if __name__ == '__main__':
    try:
        number, i = float(input("Введите число: ")), 0
        while i <= number:
            print(i)
            i += 1
    except ValueError:
        print('Значение должно быть числом!')