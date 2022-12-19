# Вычислить число Пи c заданной точностью d
# Пример: - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

import math

d = (input("Введите число d из указанного диапазона: "))
res_str = d.replace('0.','',1)
PI = math.pi
str_PI = str(PI)
result = ''
count = 0
while len(result) != (len(res_str)+2):
    result = result+str_PI[count]
    count +=1

print(f"число PI с указанной точностью равно: {result}")

