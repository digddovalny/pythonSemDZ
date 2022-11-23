#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = int(input("Ведите значение х: "))
y = int(input("Ведите значение y: "))
z = int(input("Ведите значение z: "))
left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")


