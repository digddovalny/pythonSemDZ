#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def mul(num):
    if num == 1:
        return 1
    else:
        return num * mul(num-1)

num_N = int(input("Введите число N: "))

list = []

for i in range(1,num_N+1):
    list.append(mul(i))
print(list)





