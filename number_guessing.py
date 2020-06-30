import random

# Generate random number
comp = random.randint(1,10)
# print (comp)

count = 0
while True:

    guess = input('Guess a number between 1 and 10: ')

    try:
        guess_int = int(guess)
        if guess_int > 10 or guess_int < 1:
            print('Number is not between 1 and 10. Please enter a valid number.')
        else:
            # Guess is too big
            if int(guess) > comp:
                count += 1
                print('Too big, guess again')
            # Guess is too small
            elif int(guess) < comp:
                count += 1
                print('Too small, guess again')
            else:
                print('You win!')
                print('Number of guesses: ', count+1)
                break
    except ValueError:
        try:
            float(guess)
            break
        except ValueError:
            print('Invalid input. Please enter a valid number.')    
