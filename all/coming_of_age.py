from datetime import date

age = int(input("Введите год вашего рождения  "))
today = date.today()
year = int(today.year)


if age == year:
    print("Шутим да")
elif age != year:
    result = year - age
    if 99 > result >= 18:
        print("Вы совершеннолетний", "Всего лет ", result)
    elif result > 99:
        print("Вы Duncan MacLeod", "Всего лет ", result)
    else:
        print("Вы не совершеннолетний", "Всего лет ", result)
else:
    print("Не шутим")
