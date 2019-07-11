
'''
Простейшие арифметические операции (1)
Написать функцию arithmetic, принимающую 3 аргумента:
первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''
def arifmetic (num1,num2,operation):
    try:
        a = int(num1)
        b = int(num2)
        if operation is "+":
            c = a+b
            return c
        elif operation is "-":
            c = a-b
            return c
        elif operation is "*":
             c = a*b
             return c
        elif operation is "/":
            c = a/b
            return c
        else:
            return "unknown operation"
    except ValueError:
        print("Wrong input, check numbers")


x = arifmetic("6","5","+")
print(x)

#Test 