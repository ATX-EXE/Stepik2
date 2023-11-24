# Индекс массы тела
#
# Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
# ИМТ показывает весит человек больше или меньше нормы для своего роста. ИМТ человека рассчитывают по формуле:
# ИМТ = масса (кг) / рост (м) * рост (м)
# где масса измеряется в килограммах, а рост — в метрах.
# Масса человека считается оптимальной, если его ИМТ находится между
# 18.5 и 25. Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
# Если значение ИМТ больше 25, то считается, что человек весит больше нормы.
#
# Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно).
# "Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.

weight, height = float(input()), float(input())
imt = weight / (height * height)
if (18.5 <= imt <= 25):
    print("Оптимальная масса")
elif (imt < 18.5):
    print("Недостаточная масса")
else:
    print("Избыточная масса")