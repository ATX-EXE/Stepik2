# Стоимость строки
#
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того,
# что один любой символ (в том числе пробел) стоит 60 копеек.
# Ответ дайте в рублях и копейках в соответствии с примерами.

in_str = input()
sym = len(in_str) * 60
print(sym // 100, "р.", sym % 100, "коп.")
