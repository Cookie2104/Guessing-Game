from random import randrange

Lower_limit = int(input("Select a Lower limit: "))                       # Select a Lower limit
Upper_limit = int(input("Select an Upper limit: "))                      # Select an Upper limit
print("You will have 5 chances to guess the number. Good luck!! ")
Secret_num = randrange(Lower_limit, Upper_limit)                         # Generates a range of numbers according to the limits set above
Guess_count = 0                                                          # Base count
Max_count = 5                                                            # Max count

while Guess_count < Max_count:                                           # Allow the player to guess until count is 5
    Guess_num = int(input("Guess the number: "))
    Guess_count += 1
    if Guess_num < Secret_num:
        print("The number you have guessed is lower. Try again!")
    elif Guess_num > Secret_num:
        print("The number you have guessed is higher. Try again!")
    else:
        print("Congratulations, you have guessed the correct number!")
        break                                                            # End the game once the player guesses the correct number
else:                                                                    # End the game if the user is not able to guess the number within 5 tries
    print("You have failed to guess the number within the given tries")


