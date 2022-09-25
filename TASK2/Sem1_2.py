# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

print('Введите а')
a = int(input()) 
print('Введите b')
b = int(input())
print('Введите c') 
c = int(input())
print('Введите d') 
d = int(input())
print('Введите f') 
f = int(input()) 

max = a
if (b > max):
    max = b
if (c > max):
    max = c
if (d > max):
    max = d
if (f > max):
    max = f
print(max)