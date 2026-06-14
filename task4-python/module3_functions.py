"""
Модуль 3: Функции
Студент: Жаховский Игорь Игоревич
Группа: БИЗ-Б-0-Д-2024-1
Дата: 15.06.2026
"""

def calculate_profit(revenue, costs):
    """
    Рассчитывает прибыль предприятия.
    
    Параметры:
    revenue (float): выручка
    costs (float): затраты
    
    Возвращает:
    float: прибыль (выручка - затраты)
    """
    return revenue - costs

def calculate_vat(price, rate=20):
    """
    Рассчитывает сумму НДС.
    
    Параметры:
    price (float): цена товара
    rate (float): ставка НДС в процентах (по умолчанию 20)
    
    Возвращает:
    float: сумма НДС
    """
    return price * rate / 100

def get_business_category(annual_revenue):
    """
    Определяет категорию бизнеса по годовой выручке.
    
    Параметры:
    annual_revenue (float): годовая выручка
    
    Возвращает:
    str: категория бизнеса
    """
    if annual_revenue < 1_000_000:
        return "Микробизнес"
    elif annual_revenue < 10_000_000:
        return "Малый бизнес"
    elif annual_revenue < 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

def compound_interest(principal, rate, years):
    """
    Рассчитывает итоговую сумму по сложному проценту.
    
    Параметры:
    principal (float): начальный капитал
    rate (float): процентная ставка (% годовых)
    years (int): срок в годах
    
    Возвращает:
    float: итоговая сумма
    """
    return principal * (1 + rate / 100) ** years

def apply_discount(price, discount_percent):
    """
    Применяет скидку к цене товара.
    
    Параметры:
    price (float): исходная цена
    discount_percent (float): размер скидки в процентах
    
    Возвращает:
    float: цена со скидкой
    """
    return price * (1 - discount_percent / 100)

def currency_convert(amount, exchange_rate, direction='to_rub'):
    """
    Конвертирует валюту.
    
    Параметры:
    amount (float): сумма для конвертации
    exchange_rate (float): обменный курс
    direction (str): направление конвертации ('to_rub' или 'to_usd')
    
    Возвращает:
    float: сконвертированная сумма
    """
    if direction == 'to_rub':
        return amount * exchange_rate
    elif direction == 'to_usd':
        return amount / exchange_rate
    else:
        raise ValueError("Некорректное направление конвертации")

def payback_period(investment, annual_profit):
    """
    Рассчитывает срок окупаемости инвестиций.
    
    Параметры:
    investment (float): объём первоначальных инвестиций
    annual_profit (float): ожидаемая годовая прибыль
    
    Возвращает:
    float: срок окупаемости в годах, или -1 если окупаемости нет
    """
    if annual_profit <= 0:
        return -1
    return investment / annual_profit

def format_invoice_line(name, quantity, price):
    """
    Форматирует строку счёта.
    
    Параметры:
    name (str): наименование позиции
    quantity (int): количество
    price (float): цена за единицу
    
    Возвращает:
    str: форматированная строка счёта
    """
    total = quantity * price
    return f"{name} × {quantity} = {total:.2f} руб."

def get_revenues(n):
    """
    Запрашивает у пользователя n значений выручки.
    
    Параметры:
    n (int): количество значений
    
    Возвращает:
    list: список значений выручки
    """
    revenues = []
    for i in range(n):
        rev = float(input(f"Введите выручку за период {i+1}: "))
        revenues.append(rev)
    return revenues

def analyze_revenues(revenues):
    """
    Анализирует список выручки.
    
    Параметры:
    revenues (list): список значений выручки
    
    Возвращает:
    tuple: (минимум, максимум, среднее)
    """
    return min(revenues), max(revenues), sum(revenues) / len(revenues)

def generate_report(company_name, revenue, costs):
    """
    Генерирует финансовый отчёт.
    
    Параметры:
    company_name (str): наименование компании
    revenue (float): выручка
    costs (float): затраты
    
    Возвращает:
    str: многострочный текстовый отчёт
    """
    profit = revenue - costs
    if revenue > 0:
        profitability = (profit / revenue) * 100
    else:
        profitability = 0
    status = "деятельность прибыльна" if profit > 0 else "деятельность убыточна"
    
    report = f"""
    {"=" * 40}
    ФИНАНСОВЫЙ ОТЧЁТ
    {"=" * 40}
    Наименование компании: {company_name}
    Выручка: {revenue:,.2f} руб.
    Затраты: {costs:,.2f} руб.
    Прибыль: {profit:,.2f} руб.
    Рентабельность продаж: {profitability:.2f}%
    Итоговый вывод: {status}
    {"=" * 40}
    """
    return report


# Тестирование функций
if __name__ == "__main__":
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ")
    print("=" * 50)
    
    # Тест calculate_profit
    print(f"\ncalculate_profit(500000, 320000) = {calculate_profit(500000, 320000)} руб.")
    
    # Тест calculate_vat
    print(f"calculate_vat(1000) = {calculate_vat(1000)} руб.")
    print(f"calculate_vat(1000, 10) = {calculate_vat(1000, 10)} руб.")
    
    # Тест get_business_category
    print(f"get_business_category(5_500_000) = {get_business_category(5_500_000)}")
    
    # Тест compound_interest
    print(f"compound_interest(100000, 10, 3) = {compound_interest(100000, 10, 3):.2f} руб.")
    
    # Тест apply_discount
    print(f"apply_discount(1500, 15) = {apply_discount(1500, 15):.2f} руб.")
    
    # Тест currency_convert
    print(f"currency_convert(100, 90, 'to_rub') = {currency_convert(100, 90, 'to_rub')} руб.")
    print(f"currency_convert(9000, 90, 'to_usd') = {currency_convert(9000, 90, 'to_usd'):.2f} USD")
    
    # Тест payback_period
    print(f"payback_period(1000000, 250000) = {payback_period(1000000, 250000)} лет")
    
    # Тест format_invoice_line
    print(format_invoice_line("Ноутбук", 2, 45000))
    
    # Тест generate_report
    print(generate_report("ООО 'Ромашка'", 5000000, 3500000))