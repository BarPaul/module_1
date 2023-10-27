if __name__ == '__main__':
    my_dict = {}
    my_dict['name'] = 'John'
    my_dict['age'] = 25
    my_dict['city'] = 'New York'
    print(my_dict)
    my_dict['age'] = 26
    my_dict['email'] = 'john@example.com'
    print('Ключ "country" отсутсвует' if my_dict.get('country', True) else 'Ключ "country" присутсвует')
    for key, value in my_dict.items():
        print(f'Ключ: {key}, Значение: {value}')