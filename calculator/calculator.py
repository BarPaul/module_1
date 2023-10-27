def solve(ar: str, a: float, b: float) -> float:
    if ar not in ['+', '-']:
        return Exception('Операция должна быть + или -')
    return [a - b, a + b][ar == '+']


if __name__ == '__main__':
    print('Привет! Это калькулятор light edition.\nДоступные операции: +, -')
    try: 
        arifmetic, a, b = input("Введите операцию: "), float(input("Введите первое число: ")), float(input("Введите второе число: "))
        print(f'Результат: {solve(arifmetic, a, b)}')
    except ValueError:
        print('Значение должно быть числом!')
    except Exception as e:
        print(e.args)