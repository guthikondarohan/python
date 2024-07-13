import random

user1_total = 0
user2_total = 0
number_of_turns1 = 0
number_of_turns2 = 0

def user1Turn():
    roll = random.randint(1,6)
    return roll

def user2Turn():
    roll = random.randint(1,6)
    return roll

while user1_total<=30:
    user1Score = user1Turn()
    if user1Score != 1:
        user1_total += user1Score
        number_of_turns1 += 1
    elif user1Score == 1:
        user1_total = 0
        number_of_turns1 += 1
    else:
        break

while user2_total <= 30:
    user2Score = user2Turn()
    if user2Score != 1:
        user2_total += user2Score
        number_of_turns2 += 1
    elif user2Score == 1:
        user2_total = 0
        number_of_turns2 += 1
    else:
        break

if number_of_turns1 > number_of_turns2:
    print("User 1 wins")
    print("user1 took {} turns, user2 took {} turns to reach 30".format(number_of_turns1,number_of_turns2))
elif number_of_turns2 > number_of_turns1:
    print("User 2 wins")
    print("user1 took {} turns, user2 took {} turns to reach 30".format(number_of_turns1,number_of_turns2))
else:
    print("Match has Draw with User1 taking {} turns, and the User2 taking {} turns".format(number_of_turns1,number_of_turns2))
          

    


