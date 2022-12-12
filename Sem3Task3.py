#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5.1, 10.01] => 0.19

inp = (input("Введите числа через пробел: "))
str = (inp.split(' '))
lst = []
for v in str:
    lst.append(float(v))

lst_last_part = []
for i in range(len(lst)):
    lst_last_part.append(round(lst[i]%1,2))
print(max(lst_last_part)-min(lst_last_part))





