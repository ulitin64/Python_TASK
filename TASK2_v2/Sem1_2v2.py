# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

print('Введите числа')
list =[]
for i in 78, 55, 36, 90, 2:
    list.append(int(input()))
    print(list)
    max = list[0]
for i in list:
    if max < i: max = i
print(max)