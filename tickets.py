tickets = int(input("Введите количество билетов: "))
total = 0
count = 0

for i in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        print("Вход бесплатный")
        total += 0
        count += 1
    elif 18 <= age < 25:
        print("Стоимость билета: 990 рублей")
        total += 990
        count += 1
    else:
        print("Стоимость билета: 1390 рублей")
        total += 1390
        count += 1

print(f"Общая стоимость билетов {count} билетов: {total} рублей")

if tickets > 3 and count > 3:
    total = total - total * 0.1
    print(f"Стоимость {count} билетов со скидкой 10%: {total} рублей")
