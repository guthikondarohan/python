print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
        
        
        
        
        '''user1 = str(input("choose rock,paper or scissor user1: "))
user2 = str(input("choose rock,paper or scissor user2: "))
def compare(u1,u2):
    if u1 == u2:
        print("its a draw")
    elif u1 == 'rock':
        if u2 == 'scissor':
            print("user1 wins")
    elif u1 == 'paper':
        if u2 == 'rock':
            print("user1 wins")
    elif u1 == 'scisssor':
        if u2 == 'paper':
            print("user1 wins")
    elif u1 == 'rock':
        if u2 == 'paper':
            print("user2 wins")
    elif u1 == 'paper':
        if u2 == 'scissor':
            print("user2 wins")
    elif u1 == 'scissor':
        if u2 == 'rock':
            print("user2 wins")
    else:
        print("invalid input")

compare(user1,user2) '''

