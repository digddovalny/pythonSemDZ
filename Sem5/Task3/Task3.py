# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#Кодировка
def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 0
    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
data = 'AABBCCCCCDD'
print(f'Результат при кодировке : {rle_encode(data)}')

#Декодировка
def rle_decode(data):
    result = ''
    data = list(data)
    amounts = []
    chars = []
    for i in data[::2]:
        if i != None:
            amounts.append(i)
    for i in data[1::2]:
        if i != None:
            chars.append(i)
    for index, amount in enumerate(amounts):
        for i in range(int(amount)):
            result += chars[index]
    return result



data = '4A2B3C'
print(f'результат при декодировке: {rle_decode(data)}')