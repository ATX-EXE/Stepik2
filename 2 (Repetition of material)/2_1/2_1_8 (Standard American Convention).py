# TODO Standard American Convention
#
# На вход программе подаётся натуральное число. Напишите программу,
# которая вставляет в заданное число запятые в соответствии со стандартным
# американским соглашением о запятых в больших числах.

num = input()
# str_num =
# for i in range(len(num) // 3 if len(num) % 3 > 0 else len(num) // 3 - 1):
#     str_num = num[-1:-3] + ","
# num0 = list(num)
# num1=[]
# print(len(num0))
# print((len(num0)-1) // 3)
num0 = int(num)
for i in range((len(num) - 1) // 3):
    print(int(num0) % 1000)
    num0 = num0 // 1000
