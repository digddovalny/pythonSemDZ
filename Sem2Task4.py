# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

nums = int(input("Введите число N: "))
nums_list = []
mul = 1
for j in range(-abs(nums),abs(nums)+1):
    nums_list.append(j)
print(nums_list)
data = open('file.txt', 'w')
for i in range(0, nums):
    data.write(str(random.randint(0, len(nums_list))-1) + "\n")
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    mul *= nums_list[int(line)]
    print(line)
print(f"Произведение чисел равно: ----> {mul}")
data.close()
