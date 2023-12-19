# Координатные четверти
#
# Дан набор точек на координатной плоскости.
# Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
#
# Первая четверть: 1
# Вторая четверть: 0
# Третья четверть: 1
# Четвертая четверть: 0

quantity, array_of_coordinates, response_array = int(input()), [], [0, 0, 0, 0]

for i in range(quantity):
    array_of_coordinates.append(input().split())

for i in array_of_coordinates:
    x, y = int(i[0]), int(i[1])
    if x > 0 and y > 0:
        response_array[0] += 1
    elif x < 0 and y > 0:
        response_array[1] += 1
    elif x < 0 and y < 0:
        response_array[2] += 1
    elif x > 0 and y < 0:
        response_array[3] += 1
print("Первая четверть:", response_array[0], "\n",
      "Вторая четверть:", response_array[1], "\n",
      "Третья четверть:", response_array[2], "\n",
      "Четвертая четверть:", response_array[3])
