"""
Мини-программа: Учёт доходов и расходов бюджета
Вариант 4

Студент: Жаховский Игорь Игоревич
Группа: БИЗ-Б-0-Д-2024-1
Дата: 15.06.2026

Описание программы:
Программа позволяет пользователю вести учёт личного или семейного бюджета.
Программа работает с предустановленными тестовыми данными (не требует ввода с клавиатуры).
"""

# ========== ТЕСТОВЫЕ ДАННЫЕ (можно менять здесь) ==========
# Доходы: список кортежей (название, сумма)
INCOME_ITEMS = [
    ("Зарплата", 75000.00),
    ("Фриланс", 15000.00),
    ("Проценты по вкладам", 3500.50)
]

# Расходы: список кортежей (название, сумма)
EXPENSE_ITEMS = [
    ("Аренда квартиры", 30000.00),
    ("Продукты питания", 15000.00),
    ("Транспорт", 5000.00),
    ("Интернет и связь", 2000.00),
    ("Развлечения", 5000.00)
]
# ===========================================================

def calculate_total(items):
    """
    Вычисляет общую сумму из списка статей.
    
    Параметры:
    items (list): список кортежей (название, сумма)
    
    Возвращает:
    float: общая сумма
    """
    return sum(amount for _, amount in items)

def print_items(title, items):
    """
    Выводит список статей в отформатированном виде.
    
    Параметры:
    title (str): заголовок таблицы
    items (list): список кортежей (название, сумма)
    """
    print(f"\n{title}")
    print("-" * 40)
    for name, amount in items:
        print(f"  {name}: {amount:>10.2f} руб.")
    print("-" * 40)
    total = calculate_total(items)
    print(f"  ИТОГО: {total:>10.2f} руб.")

def analyze_budget(income_total, expense_total):
    """
    Анализирует бюджет и возвращает остаток и заключение.
    
    Параметры:
    income_total (float): общая сумма доходов
    expense_total (float): общая сумма расходов
    
    Возвращает:
    tuple: (остаток, строка с заключением)
    """
    balance = income_total - expense_total
    if balance > 0:
        status = "ПРОФИЦИТ бюджета (есть свободные средства) ✓"
    elif balance < 0:
        status = "ДЕФИЦИТ бюджета (не хватает средств) ✗"
    else:
        status = "СБАЛАНСИРОВАННЫЙ бюджет (доходы равны расходам)"
    return balance, status

def get_saving_advice(balance, expense_total, income_total):
    """
    Даёт рекомендации по оптимизации бюджета.
    
    Параметры:
    balance (float): остаток бюджета
    expense_total (float): общая сумма расходов
    income_total (float): общая сумма доходов
    
    Возвращает:
    str: рекомендация
    """
    if balance > 0 and income_total > 0:
        saving_percent = (balance / income_total) * 100
        return f"  Отлично! Вы откладываете {saving_percent:.1f}% дохода."
    elif balance < 0:
        required_reduction = -balance
        if expense_total > 0:
            reduction_percent = (required_reduction / expense_total) * 100
            return f"  Рекомендуется сократить расходы на {reduction_percent:.1f}%."
        else:
            return "  Необходимо увеличить доходы."
    else:
        return "  Рассмотрите возможность увеличения доходов или сокращения расходов для создания сбережений."

def main():
    """
    Главная функция программы.
    """
    print("=" * 50)
    print("    УЧЁТ ДОХОДОВ И РАСХОДОВ БЮДЖЕТА")
    print("=" * 50)
    
    # Используем предустановленные тестовые данные
    income_items = INCOME_ITEMS
    expense_items = EXPENSE_ITEMS
    
    # Расчёт общих сумм
    income_total = calculate_total(income_items)
    expense_total = calculate_total(expense_items)
    
    print(f"\n📊 Анализ бюджета (всего статей: {len(income_items)} доходов, {len(expense_items)} расходов)")
    
    # Вывод результатов
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА БЮДЖЕТА")
    print("=" * 50)
    
    print_items("📈 ДОХОДЫ", income_items)
    print_items("📉 РАСХОДЫ", expense_items)
    
    # Анализ бюджета
    balance, status = analyze_budget(income_total, expense_total)
    
    print("\n" + "-" * 40)
    print(f"💰 ОСТАТОК БЮДЖЕТА: {balance:>10.2f} руб.")
    print("-" * 40)
    
    print(f"\n📋 ЗАКЛЮЧЕНИЕ: {status}")
    print(f"\n💡 РЕКОМЕНДАЦИЯ:")
    print(f"{get_saving_advice(balance, expense_total, income_total)}")
    
    # Дополнительный совет
    if balance < 0:
        print("\n  📌 Совет: пересмотрите обязательные расходы")
        print("     и найдите возможности для экономии.")
    elif balance > 0 and income_total > 0 and balance < income_total * 0.1:
        print("\n  📌 Совет: увеличьте норму сбережений до 10-15% дохода.")
    elif balance > 0 and income_total > 0 and balance > income_total * 0.3:
        print("\n  📌 Совет: рассмотрите варианты инвестирования свободных средств.")
    
    # Финансовые показатели
    print("\n" + "-" * 40)
    print("📊 ФИНАНСОВЫЕ ПОКАЗАТЕЛИ:")
    if income_total > 0:
        print(f"  Норма сбережения: {(balance/income_total)*100:.1f}%")
        print(f"  Доля расходов в доходах: {(expense_total/income_total)*100:.1f}%")
    
    print("\n" + "=" * 50)
    print("Благодарим за использование программы!")
    print("=" * 50)

if __name__ == "__main__":
    main()
