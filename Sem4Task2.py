# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное число N: "))

def factor(n):
    i = 2
    lst = []
    while i * i <= n:
        while n%i ==0:
            lst.append(i)
            n = n/i
        i+=1
    if n > 1:
        lst.append(n)
    return lst

print(factor(num))
