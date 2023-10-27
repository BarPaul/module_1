if __name__ == '__main__':
    data = [
        124,
        1.24,
        "Bye, World!",
        True,
        False,
        [True, False],
        (0, 1),
        {"apple", "banana"},
        {"city": "Moscow", "full_name": "Paul Durov"},
        5.1
    ]
    print(data, data[:5], data[-3:], data[1::2], sep="\n")
    data[2] = "Hello, World!"
    print(data)