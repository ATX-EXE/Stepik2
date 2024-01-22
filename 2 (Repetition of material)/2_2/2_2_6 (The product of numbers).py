# TODO Произведение чисел
#
# Напишите программу для определения, является ли число произведением
# двух чисел из данного набора. Программа должна выводить результат
# в виде ответа «ДА» или «НЕТ».
#
# Формат входных данных
# В первой строке подаётся число n (0<n<1000) – количество чисел в наборе.
# В последующих n строках вводятся целые числа, составляющие набор (могут повторяться).
# Затем следует целое число, которое является или не является произведением
# двух каких-то чисел из набора.
#
# Формат выходных данных
# Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.
#
# Примечание 1. Само на себя число из набора умножиться не может. Другими словами,
# два множителя должны иметь разные индексы в наборе.
#
# Примечание 2. Для решения задачи используйте вложенные циклы.

number_of_digits, nums, result = int(input()), [], False
for i in range(number_of_digits):
    nums.append(int(input()))
answer = int(input())
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums), 1):
        if nums[i] * nums[j] == answer:
            result = True
            break
print("ДА" if result else "НЕТ")

#
# print(number_of_digits, '\n', *nums, '\n', answer)