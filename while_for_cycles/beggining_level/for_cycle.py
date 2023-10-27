if __name__ == '__main__':
    try:
        number = int(input("Введите число: "))
        for i in range(number + 1):
            print(i)
    except ValueError:
        print('Значение должно быть целым числом!')