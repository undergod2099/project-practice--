"""
Модуль 2: Условные конструкции и циклы
Студент: Жаховский Игорь Игоервич
Группа: БИЗ-Б-0-Д-2024-1
Дата: 15.06.2026
"""

# Упражнение 1. Финансовый результат периода
print("=" * 50)
print("Упражнение 1. Финансовый результат периода")
profit = float(input("Введите итоговую прибыль за месяц (руб.): "))
if profit > 0:
    print("Прибыль")
elif profit < 0:
    print("Убыток")
else:
    print("Безубыточность")
print()

# Упражнение 2. Классификация субъекта по выручке
print("=" * 50)
print("Упражнение 2. Классификация субъекта по выручке")
annual_revenue = float(input("Введите годовую выручку предприятия (руб.): "))
if annual_revenue < 1_000_000:
    print("Категория: Микробизнес")
elif annual_revenue < 10_000_000:
    print("Категория: Малый бизнес")
elif annual_revenue < 100_000_000:
    print("Категория: Средний бизнес")
else:
    print("Категория: Крупный бизнес")
print()

# Упражнение 3. Расчёт налога на доходы физических лиц
print("=" * 50)
print("Упражнение 3. Расчёт налога на доходы физических лиц")
salary = float(input("Введите ежемесячную заработную плату (руб.): "))
if salary <= 50000:
    tax_rate = 13
else:
    tax_rate = 15
tax = salary * tax_rate / 100
net_salary = salary - tax
print(f"Ставка НДФЛ: {tax_rate}%")
print(f"Сумма налога: {tax:.2f} руб.")
print(f"Зарплата 'на руки': {net_salary:.2f} руб.")
print()

# Упражнение 4. Таблица доходности по ставке
print("=" * 50)
print("Упражнение 4. Таблица доходности по ставке")
rate = float(input("Введите процентную ставку (%): "))
capital = 100000
print(f"\n{'Месяц':<8} {'Сумма процентов, руб.':<25} {'Итоговая сумма, руб.':<25}")
print("-" * 58)
for month in range(1, 13):
    interest = capital * (rate / 100) / 12
    capital += interest
    print(f"{month:<8} {interest:<25.2f} {capital:<25.2f}")
print()

# Упражнение 5. Анализ ценового диапазона
print("=" * 50)
print("Упражнение 5. Анализ ценового диапазона")
prices = [150, 320, 210, 450, 180]
average_price = sum(prices) / len(prices)
print(f"Список цен: {prices}")
print(f"Средняя цена: {average_price:.2f}")
for price in prices:
    if price > average_price:
        print(f"Цена {price} руб. -> ВЫШЕ СРЕДНЕГО")
    else:
        print(f"Цена {price} руб. -> НИЖЕ ИЛИ РАВНА СРЕДНЕЙ")
print()

# Упражнение 6. Накопление капитала по модели сложного процента
print("=" * 50)
print("Упражнение 6. Накопление капитала по модели сложного процента")
start_capital = float(input("Введите начальный капитал (руб.): "))
interest_rate = float(input("Введите процентную ставку (%): "))
print(f"\n{'Год':<8} {'Накопленная сумма, руб.':<30}")
print("-" * 38)
for year in range(1, 6):
    amount = start_capital * (1 + interest_rate / 100) ** year
    print(f"{year:<8} {amount:<30.2f}")
print()

# Упражнение 7. Накопительный счёт с ежемесячными взносами
print("=" * 50)
print("Упражнение 7. Накопительный счёт с ежемесячными взносами")
monthly_contribution = float(input("Введите размер ежемесячного взноса (руб.): "))
months = int(input("Введите количество месяцев: "))
total = 0
print(f"\n{'Месяц':<8} {'Накопленная сумма, руб.':<30}")
print("-" * 38)
for month in range(1, months + 1):
    total += monthly_contribution
    print(f"{month:<8} {total:<30.2f}")
print()

# Упражнение 8. Доступность товаров в рамках бюджета
print("=" * 50)
print("Упражнение 8. Доступность товаров в рамках бюджета")
budget = float(input("Введите бюджет покупателя (руб.): "))
print()
for i in range(5):
    product_name = input(f"Введите название товара {i+1}: ")
    product_price = float(input(f"Введите цену товара {i+1}: "))
    if product_price <= budget:
        print(f"Товар '{product_name}' доступен")
    else:
        print(f"Товар '{product_name}' не хватает {product_price - budget:.2f} руб.")
    print()
print()

# Упражнение 9. Анализ выручки за полугодие
print("=" * 50)
print("Упражнение 9. Анализ выручки за полугодие")
revenues = []
for i in range(1, 7):
    rev = float(input(f"Введите выручку за месяц {i} (руб.): "))
    revenues.append(rev)
print(f"\nМинимальная выручка: {min(revenues):.2f} руб.")
print(f"Максимальная выручка: {max(revenues):.2f} руб.")
print(f"Среднемесячная выручка: {sum(revenues)/6:.2f} руб.")
print()

# Упражнение 10. Мониторинг рентабельности
print("=" * 50)
print("Упражнение 10. Мониторинг рентабельности")
threshold = float(input("Введите пороговое значение рентабельности (%): "))
above = 0
below = 0
for i in range(1, 7):
    r = float(input(f"Введите рентабельность за месяц {i} (%): "))
    if r >= threshold:
        above += 1
    else:
        below += 1
print(f"\nКоличество месяцев с рентабельностью ВЫШЕ порога: {above}")
print(f"Количество месяцев с рентабельностью НИЖЕ порога: {below}")