# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

print("Введите число а ")
a = float(input())
print(int(a * 10) % 10)