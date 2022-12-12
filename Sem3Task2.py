#   Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   Пример:
#   [2, 3, 4, 5, 6] => [12, 15, 16]
#   [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 5, 6]
lst_multy = []
if len(lst)%2 !=0:
    avg_lst = len(lst)//2+1
else:
    avg_lst = len(lst) // 2
for i in range(0,avg_lst):
    multy = lst[i]*lst[len(lst)-i-1]
    lst_multy.append(multy)
print(lst_multy)
