# Standard American Convention
#
# На вход программе подаётся натуральное число (0 < n < 10^100). Напишите программу,
# которая вставляет в заданное число запятые в соответствии со стандартным
# американским соглашением о запятых в больших числах.

num_str = input()
num_len, num_list = (len(num_str) // 3) - 1 if len(num_str) % 3 == 0 else len(num_str) // 3, []
for i in range(num_len + 1):
    num_list.insert(0, num_str[-3:])
    num_str = num_str[0:-3]
print(*num_list, sep=",")
