import random

count = 0
number = random.randint(1, 10)
print("Загадано", number)  # Для отладки, потом можно убрать или закомментировать


def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            # Проверка, что число в диапазоне от 1 до 9
            if 1 <= number <= 9:
                return number
            else:
                print("Ошибка: число должно быть от 1 до 9. Попробуйте ещё раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте ещё раз.")

#1
while count < 3:
    tst = get_number('Введите цифру от 1 до 9: ')

    if tst == number:
        print("Вы угадали число!")
        count += 1
        print("Использовано попыток:", count, "из 3")
        break
    elif tst < number:
        print("Ваше число меньше загаданного")
        count += 1
        print("Использовано попыток:", count, "из 3")
    else:  # tst > number
        print("Ваше число больше загаданного")
        count += 1
        print("Использовано попыток:", count, "из 3")

# Если попытки закончились
if count == 3 and tst != number:
    print("\nПопытки закончились! Вы не угадали число.", number)