number_of_sticks = 10
player_turn = 1

def can_take(sticks):
    return sticks >=1 and sticks <=3

def swich_player_turn(turn):
    return 1 if turn == 2 else 2

def end_of_game(sticks):
    return sticks <=0

print('Введите имя игрока №1')
name_first = str(input())
print('Введите имя игрока №2')
name_second = str(input())


while (not end_of_game(number_of_sticks)):
    if player_turn == 1:
        player_name = name_first
    else:
        player_name = name_second
    print(f'Осталось {number_of_sticks} палочек, сколько палочек игрок {player_name} хочет взять?')
    taken = int(input())
    
    if not can_take(taken):
        print('Вы можете взять только одну, две или три палочки')
        continue
        
    number_of_sticks -= taken
    print(f'Вы взяли {taken} палочек\n')
    
    if end_of_game(number_of_sticks):
        print(f'Палочек больше нет.\nИгрок {player_name} проиграл!')
        break
        
    player_turn = swich_player_turn(player_turn) 
1
