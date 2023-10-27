if __name__ == '__main__':
    my_dict = {"name": "John", "age": 25, "city": "New York"}
    print(my_dict)
    my_dict["age"] = 26
    my_dict["email"] = "john@example.com"
    my_dict.pop('city')
    for key, value in my_dict.items():
        print(f'Ключ: {key}, Значение: {value}')