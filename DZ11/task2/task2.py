# Задача 2. Создайте декоратор log_calls, который:
# 1. Записывает в файл 'function_log.txt':
#    - Время вызова
#    - Имя функции
#    - Аргументы
#    - Возвращаемое значение
# 2. Подумайте как можно использовать @wraps из
# библиотеки functools для сохранения метаданных
import time
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(a, b, c):
        start_time = time.strftime('%d.%m.%Y %H:%M:%S')
        result = func(a, b, c)

        with open('function_log.txt', 'a') as f:
            f.write(f'[{start_time}] Вызвана функция: {func.__name__}\n')
            f.write(f'Аргументы: первый аргумент ={a}, оператор = {b}, второй аргумент = {c}\n')
            f.write(f'Результат: {result}\n')
        return result
    return wrapper

@log_calls
def safe_calculator(a, b, c):
    try:
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
            return None
        print(f'Результат выполнения {num_1} {oper} {num_2} = {res}')
        return res
    except ZeroDivisionError:
        print('Деление на ноль невозможно')
        return None
    except ValueError:
        print('Неверный тип данных')
        return  None
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


if __name__ =='__main__':
    num_1 = float(input("Введите первое число: "))
    oper = str(input("Введите символ арифметическую операции (+, -, *, /): "))
    num_2 = float(input("Введите второе число: "))
    safe_calculator(num_1, oper, num_2)