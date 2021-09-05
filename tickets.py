tickets = int(input("Введите количество билетов: "))
result = 0
count = 0

for i in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        print("Вход бесплатный")
        result += 0
        count += 1
    elif 18 <= age < 25:
        print("Стоимость билета: 990 рублей")
        result += 990
        count += 1
    else:
        print("Стоимость билета: 1390 рублей")
        result += 1390
        count += 1

print(f"Общая стоимость билетов {count} билетов: {result} рублей")

if tickets > 3 and count > 3:
    result = result - result * 0.1
    print(f"Стоимость {count} билетов со скидкой 10%: {result} рублей")
