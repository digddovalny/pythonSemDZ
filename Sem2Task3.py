#Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

num = int(input("Введите число n: "))
num_list = {}
sum = 0
for i in range(1,num+1):
    num_list[i] = round((1+(1/i))**i,2)
    sum += num_list[i]
print(num_list)
print(f"Сумма чисел в словаре равна: {sum}")