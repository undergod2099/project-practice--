"""
Мини-программа: Учёт доходов и расходов бюджета
Вариант 4

Студент: Жаховский Игорь Игоревич
Группа: БИЗ-Б-0-Д-2024-1
Дата: 15.06.2026

Описание программы:
Программа позволяет пользователю вести учёт личного или семейного бюджета.
Пользователь вводит статьи доходов и расходов с суммами.
Программа рассчитывает итоговые суммы и определяет профицит или дефицит бюджета.
"""

def input_items(prompt, count):
    """
    Вводит список статей (название и сумма) и возвращает общую сумму и список.
    
    Параметры:
    prompt (str): приглашение для пользователя
    count (int): количество статей
    
    Возвращает:
    tuple: (общая сумма, список статей в виде кортежей (название, сумма))
    """
    items = []
    total = 0.0
    print(f"\n{prompt}")
    print("-" * 40)
    for i in range(1, count + 1):
        name = input(f"  Статья {i} (название): ")
        amount = float(input(f"    Сумма для '{name}': "))
        items.append((name, amount))
        total += amount
    return total, items

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
    print(f"  ИТОГО: {sum(amount for _, amount in items):>10.2f} руб.")

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
        status = "ПРОФИЦИТ бюджета (есть свободные средства)"
    elif balance < 0:
        status = "ДЕФИЦИТ бюджета (не хватает средств)"
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
    if balance > 0:
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
    print("\nПрограмма поможет вам проанализировать ваш бюджет.")
    print("Вы можете ввести любое количество статей доходов и расходов.")
    
    try:
        # Ввод количества статей
        n_income = int(input("\nВведите количество статей доходов: "))
        if n_income <= 0:
            print("Ошибка: количество статей доходов должно быть положительным.")
            return
        
        n_expense = int(input("Введите количество статей расходов: "))
        if n_expense <= 0:
            print("Ошибка: количество статей расходов должно быть положительным.")
            return
        
        # Ввод доходов и расходов
        income_total, income_items = input_items("ДОХОДЫ:", n_income)
        expense_total, expense_items = input_items("РАСХОДЫ:", n_expense)
        
        # Вывод результатов
        print("\n" + "=" * 50)
        print("РЕЗУЛЬТАТЫ АНАЛИЗА БЮДЖЕТА")
        print("=" * 50)
        
        print_items("ДОХОДЫ", income_items)
        print_items("РАСХОДЫ", expense_items)
        
        # Анализ бюджета
        balance, status = analyze_budget(income_total, expense_total)
        
        print("\n" + "-" * 40)
        print(f"ОСТАТОК БЮДЖЕТА: {balance:>10.2f} руб.")
        print("-" * 40)
        
        print(f"\nЗАКЛЮЧЕНИЕ: {status}")
        print(f"\n{get_saving_advice(balance, expense_total, income_total)}")
        
        # Дополнительный совет
        if balance < 0:
            print("\n  Рекомендация: пересмотрите обязательные расходы")
            print("  и найдите возможности для экономии.")
        elif balance > 0 and balance < income_total * 0.1:
            print("\n  Рекомендация: увеличьте норму сбережений до 10-15% дохода.")
        elif balance > income_total * 0.3:
            print("\n  Рекомендация: рассмотрите варианты инвестирования свободных средств.")
        
    except ValueError:
        print("\nОшибка: введено некорректное значение. Пожалуйста, введите числа.")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
    
    print("\n" + "=" * 50)
    print("Благодарим за использование программы!")
    print("=" * 50)

if __name__ == "__main__":
    main()