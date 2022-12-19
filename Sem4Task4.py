#Задана натуральная степень k.
#Сформировать случайным образом список коэффициентов
#(значения от 0 до 100)* многочлена и записать в файл многочлен степени k.

import random

# запись в файл
def write_in_file(st):
    with open('file1.txt', 'w') as data:
        data.write(st)

# создание коэффициентов
def rnd():
    return random.randint(0, 101)

# генерирование многочлена
def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst

# преобразование многочлена в строку
def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите степень k = "))
koef = create_mn(k)
write_in_file(create_str(koef))