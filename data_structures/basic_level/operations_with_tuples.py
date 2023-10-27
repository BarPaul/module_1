if __name__ == '__main__':
    data1, data2 = {i for i in input("Введите первый список: ").split()}, {i for i in input("Введите второй список: ").split()}
    print(f'Количество пересечений: {len(data1.intersection(data2))}')
