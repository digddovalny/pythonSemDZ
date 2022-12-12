#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def transformation(num):
    result = ''
    while num > 0:
        result = str(num%2)+result
        num = num//2
    return result
num = int(input("Введите число для преобразования: "))
print(transformation(num))