"""
Модуль 1: Переменные, типы данных, ввод и вывод
Студент: Жаховский Игорь Игоревич
Группа: БИЗ-Б-0-Д-2024-1
Дата: 15.06.2026
"""

# Упражнение 1. Карточка сотрудника
print("=" * 50)
print("Упражнение 1. Карточка сотрудника")
name = "Алексей Смирнов"
age = 28
salary = 75000.50
is_active = True
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Зарплата: {salary:.2f} руб.")
print(f"Активен: {is_active}")
print()

# Упражнение 2. Приветствие сотрудника
print("=" * 50)
print("Упражнение 2. Приветствие сотрудника")
employee_name = input("Введите имя сотрудника: ")
city = input("Введите город: ")
print(f"Сотрудник {employee_name} работает в офисе {city}")
print()

# Упражнение 3. Расчёт итоговой стоимости
print("=" * 50)
print("Упражнение 3. Расчёт итоговой стоимости")
price = float(input("Введите цену единицы товара (руб.): "))
quantity = int(input("Введите количество единиц: "))
total = price * quantity
print(f"Итоговая стоимость: {total:.2f} руб.")
print()

# Упражнение 4. Доход по банковскому вкладу
print("=" * 50)
print("Упражнение 4. Доход по банковскому вкладу")
deposit = float(input("Введите сумму вклада (руб.): "))
rate = float(input("Введите процентную ставку (% годовых): "))
income = deposit * rate / 100
total_deposit = deposit + income
print(f"Доход за год: {income:.2f} руб.")
print(f"Итоговая сумма вклада: {total_deposit:.2f} руб.")
print()

# Упражнение 5. Конвертация валюты
print("=" * 50)
print("Упражнение 5. Конвертация валюты")
usd_rate = float(input("Введите курс доллара к рублю: "))
rub_amount = float(input("Введите сумму в рублях: "))
usd_amount = rub_amount / usd_rate
print(f"{rub_amount:.2f} руб. = {usd_amount:.2f} USD")
print()

# Упражнение 6. Прибыль и рентабельность продаж
print("=" * 50)
print("Упражнение 6. Прибыль и рентабельность продаж")
revenue = float(input("Введите выручку предприятия (руб.): "))
costs = float(input("Введите общие затраты (руб.): "))
profit = revenue - costs
if revenue > 0:
    profitability = (profit / revenue) * 100
    print(f"Прибыль: {profit:.2f} руб.")
    print(f"Рентабельность продаж: {profitability:.2f}%")
else:
    print("Ошибка: выручка не может быть равна нулю")
print()

# Упражнение 7. Изменение цены финансового актива
print("=" * 50)
print("Упражнение 7. Изменение цены финансового актива")
start_price = float(input("Введите начальную цену актива (руб.): "))
end_price = float(input("Введите конечную цену актива (руб.): "))
abs_change = end_price - start_price
rel_change = (abs_change / start_price) * 100
print(f"Абсолютное изменение: {abs_change:.2f} руб.")
print(f"Относительное изменение: {rel_change:.2f}%")
print()

# Упражнение 8. Мини-прайс-лист
print("=" * 50)
print("Упражнение 8. Мини-прайс-лист")
products = []
for i in range(3):
    name = input(f"Введите название товара {i+1}: ")
    price = float(input(f"Введите цену товара {i+1}: "))
    products.append((name, price))
print("\nПрайс-лист:")
for name, price in products:
    print(f"Позиция: {name} --- {price:.2f} руб.")
print()

# Упражнение 9. Годовой личный бюджет
print("=" * 50)
print("Упражнение 9. Годовой личный бюджет")
month_income = float(input("Введите среднемесячный доход (руб.): "))
month_expense = float(input("Введите среднемесячный расход (руб.): "))
year_income = month_income * 12
year_expense = month_expense * 12
balance = year_income - year_expense
print(f"Годовой доход: {year_income:.2f} руб.")
print(f"Годовой расход: {year_expense:.2f} руб.")
if balance >= 0:
    print(f"Годовой остаток (профицит): {balance:.2f} руб.")
else:
    print(f"Годовой остаток (дефицит): {balance:.2f} руб.")
print()

# Упражнение 10. Расчёт счёта с НДС
print("=" * 50)
print("Упражнение 10. Расчёт счёта с НДС")
quantity = int(input("Введите количество единиц товара: "))
price = float(input("Введите цену за единицу (руб.): "))
vat_rate = float(input("Введите ставку НДС (%): "))
cost_without_vat = quantity * price
vat_amount = cost_without_vat * vat_rate / 100
total_with_vat = cost_without_vat + vat_amount
print(f"Стоимость без НДС: {cost_without_vat:.2f} руб.")
print(f"Сумма НДС ({vat_rate}%): {vat_amount:.2f} руб.")
print(f"Итоговая сумма с НДС: {total_with_vat:.2f} руб.")