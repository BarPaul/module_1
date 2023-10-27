def ticket_price(age: int, with_companion: bool) -> str:
    if age < 12:
        return 'Билет бесплатный'
    elif (12 <= age <= 18) & with_companion:
        return 'Билет со скидкой'
    return "Полная стоимость билета"


if __name__ == '__main__':
    try:
        age, companion = int(input('Введите возраст: ')), input('Есть с вами сопровождающий? (нет/да): ').lower() == "да"
        print(ticket_price(age, companion))
    except ValueError:
        print('Возраст это целое число!')