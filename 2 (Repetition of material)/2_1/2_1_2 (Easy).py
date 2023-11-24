# TODO На easy

# На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
#
# сумму чисел
# a и b;
# разность чисел
# a и b;
# произведение чисел
# a и b;
# частное чисел
# a и b;
# целую часть от деления числа
# a и b;
# остаток от деления числа
# a на b;
# корень квадратный из суммы их 10-х степеней:
# sqrt(a^10 + b^10)

import math

a, b = int(input()), int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(math.sqrt(math.pow(a,10) + math.pow(b,10)))