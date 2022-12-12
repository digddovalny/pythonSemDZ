#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input("ВВедите число: "))

def fibon(n):
    if n ==0 or n ==1:
        return n
    return fibon(n-1)+fibon(n-2)

def reverse_fibon(n):
    return (-1)**(n+1)*fibon(n)

lst = []

for i in range(num+1):
    lst.append(reverse_fibon(i))

lst.reverse()
lst.pop(-1)

for j in range(num+1):
    lst.append(fibon(j))
print(lst)


