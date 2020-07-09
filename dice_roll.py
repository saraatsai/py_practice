# Dice rolling simulation

import random

rollType = [1,2]
roll = []

for n in rollType:
    while True:
        userIn = input("Press %d to roll dice #%d: " % (n,n))
        try:
            check_num = int(userIn)
            if check_num > n or check_num < (n-1): 
                print("Invalid, please press %d to roll the dice" % (n))
            else:
                roll.append(random.randint(1,7))
                # print(roll) # Check 
                break
        except ValueError:
            print("Invalid input, please press %d to roll the dice" % n)

totalRoll = sum(roll)
print("You rolled a " + str(totalRoll))