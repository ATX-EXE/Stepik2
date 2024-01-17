# TODO Больше предыдущего
#
# На вход программе подается строка текста из натуральных чисел.
# Из неё формируется список чисел. Напишите программу подсчета количества чисел,
# которые больше предшествующего им в этом списке числа.
#
# Формат входных данных
# На вход программе подается строка текста из разделенных пробелами натуральных чисел.
#
# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.
#
# Примечание. Разберём первый тест. У нас формируется список [1, 2, 3, 4, 5], в нём
# 2>1, 3>2, 4>3, 5>4. То есть получается 4 таких случая,
# где текущее число больше предыдущего. Поэтому ответ 4.

nums, result = input().split(), 0
for i in range(len(nums) - 1):
    if int(nums[i]) < int(nums[i + 1]):
        result += 1
print(result)
