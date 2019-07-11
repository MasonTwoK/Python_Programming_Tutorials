'''
Високосный год (2)
Написать функцию is_year_leap,
принимающую 1 аргумент — год,
и возвращающую True, если год високосный, и False иначе.
'''

def is_year_leap(year):
    try:
        y =int(year)

        if y%4 is 0: return True
        else: return False

    except NameError: return "Input not a number. Check it." # Не отрабатывает при вводе переменой x = is_year_leap(as)
    except IndentationError: return "Input is a string. Check it."
    except ValueError: return "Input is letters in string. Check it"
    except TypeError: return "You do not enter anything" # # Не отрабатывает при отсутствии ввода x = is_year_leap()
x = is_year_leap()
print(x)
