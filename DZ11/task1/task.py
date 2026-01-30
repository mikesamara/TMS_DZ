# Задача 1. Создайте функцию safe_calculator(), которая:
# 1. Принимает два числа и операцию (+, -, *, /)
# 2. Использует try-except для обработки:
#    - Деления на ноль
#    - Неверного типа данных
#    - Неподдерживаемой операции
# 3. Возвращает результат или сообщение об ошибке

def safe_calculator():
    try:
        num_1 = float(input("Введите первое число: "))
        oper = str(input("Введите символ арифметическую операции (+, -, *, /): "))
        num_2 = float(input("Введите второе число: "))
        if oper == "+":
            res = num_1 + num_2
        elif oper == "-":
            res = num_1 - num_2
        elif oper == "*":
            res = num_1 * num_2
        elif oper == "/":
            res = num_1/num_2
        else:
            print('Такой операции нет')
            return
        return print(f'Результат выполнения {num_1} {oper} {num_2} = {res}')
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
    except ValueError:
        print('Неверный тип данных')
    except Exception as e:
        print(f'Произошла ошибка: {e}')




safe_calculator()