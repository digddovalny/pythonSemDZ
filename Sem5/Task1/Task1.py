# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *

start_txt = f'Начало игры\n-----------------------'
print(start_txt)

def player_vs_player():
    all_candies = 2021
    take_max = 28
    count = 0
    first_player = input('Введи свое имя ---> ')
    second_player = input('Введи имя своего соперника ---> ')

    print('Определим кто первый начнет игру по результатам жеребьевки!')

    x = randint(1,2)
    if x == 1:
        lucky_player = first_player
        loser_player = second_player
    else:
        lucky_player = second_player
        loser_player = first_player
    print(f'Первый ходит {lucky_player} игрок')

    while all_candies > 0:
        if count == 0:
            step = int(input(f'сколько конфет берет игрок {lucky_player} ---> '))
            if step > all_candies or step > take_max:
                step = int(input(f'Можно взять только {take_max} конфет, игрок {lucky_player} '))
            all_candies = all_candies - step
        if all_candies > 0:
            print(f'ещё осталось {all_candies} конфет')
            count = 1
        else:
            print('осталось 0 конфет')

        if count == 1:
            step = int(input(f'сколько конфет берет игрок {loser_player} ---> '))
            if step > all_candies or step > take_max:
                step = int(input(f'Можно взять только {take_max} конфет, игрок {loser_player} '))
            all_candies = all_candies - step
        if all_candies > 0:
            print(f'ещё осталось {all_candies} конфет')
            count = 1
        else:
            print('осталось 0 конфет')
    if count == 1:
        print(f'Победил игрок {loser_player}')
    if count == 0:
        print(f'Победил игрок {lucky_player}')

player_vs_player()

# игра против бота

def player_vs_bot():
    all_candies = 2021
    take_max = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

    while all_candies > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(f'\nХодит {players[lucky%2]} \nНа кону {all_candies} ')

            if all_candies < 29:
                step = all_candies
            else:
                delenie = all_candies//28
                step = all_candies - ((delenie*take_max)+1)
                if step == -1:
                    step = take_max -1
                if step == 0:
                    step = take_max
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {all_candies} '))
            while step > take_max or step > all_candies:
                step = int(input(f'\nЗа один ход можно взять {take_max} конфет, попробуй еще раз: '))
        all_candies = all_candies - step

    print(f'На кону осталось {all_candies} \nПобедил {players[lucky%2]}')

player_vs_bot()