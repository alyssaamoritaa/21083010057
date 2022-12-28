import random

print("=" * 37)
print("<<< ⁠⁠✧.* Welcome to the Game! *⁠.⁠✧ >>>")
print("=" * 37)
print('Hello! Please Enter Your Name : ')
myName = input()
print("Hi " + str(myName) + "!" + " Let's play a guessing game.")


def random_game():

    play = True
    while play:

        easy = random.randint(1, 50)
        medium = random.randint(1, 100)
        hard = random.randint(1, 200)
        print("Which difficulty level would you like to play?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")

        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("\nLet's go with easy!")
                level_selection = not True
                break
            if level == "m":
                print("\nLet's go with medium!")
                level_selection = not True
                break
            if level == "h":
                print("\nLet's go with hard!")
                level_selection = not True
                break
            else:
                print("Invalid difficulty level. \nPlease enter either e, m, or h. ")


        if level == 'e':
            print("You'll have 10 guesses to guess a number between 1-50.")
            guesses_left = 10
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == easy:
                    print("You've guessed the right number! " + str(easy))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < easy:
                    print("Nope, your guess is too low. Guess higher!")
                elif try1 > easy:
                    print("Nope, your guess is too  high. Guess lower!")
                guesses_left -= 1
                print('You have ' + str(guesses_left) + ' guesses left!')
                
                if guesses_left == 5:
                    print("You can do this!")
                if guesses_left == 4:
                    print("Keep on trying!")
                if guesses_left == 3:
                    print("You're running out of guesses!")
                if guesses_left == 2:
                    print("Keep trying!")
                if guesses_left == 1:
                    print("One last change!")
                if guesses_left == 0:
                    print('Better luck next time!')

        if level == 'm':
            print("You'll have 10 guesses to guess a number between 1-100.")
            guesses_left = 10
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == medium:
                    print("You've guessed the right number! " + str(medium))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < medium:
                    print("Nope, your guess is too low. Guess higher!")
                elif try1 > medium:
                    print("Nope, your guess is too high. Guess lower!")
                guesses_left -= 1
                print('You have ' + str(guesses_left) + ' guesses left!')

                if guesses_left == 5:
                    print("You can do this!")
                if guesses_left == 4:
                    print("Keep on trying!")
                if guesses_left == 3:
                    print("You're running out of guesses!")
                if guesses_left == 2:
                    print("Keep trying!")
                if guesses_left == 1:
                    print("One last change!")
                if guesses_left == 0:
                    print('Better luck next time!')

        if level == 'h':
            print("You'll have 10 guesses to guess a number between 1-200")
            guesses_left = 10
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == hard:
                    print("You've guessed the right number! " + str(hard))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < hard:
                    print("Your guess is to low. Guess higher!")
                elif try1 > hard:
                    print("Your guess is too high. Guess lower!")
                guesses_left -= 1
                print('You have ' + str(guesses_left) + ' guesses left!')

               	if guesses_left == 5:
                    print("You can do this!")
                if guesses_left == 4:
                    print("Keep on trying!")
                if guesses_left == 3:
                    print("You're running out of guesses!")
                if guesses_left == 2:
                    print("Keep trying!")
                if guesses_left == 1:
                    print("One last change!")
                if guesses_left == 0:
                    print('Better luck next time!')
                
        maybe_play = True
        while maybe_play:
            again = input("\nWould you like to play again?\nYes or No\n ")
            if again == 'No' or again == 'no':
                print('\nThank you for playing. See you next time!')
                maybe_play = not True
                play = not True
            elif again == 'yes' or again == 'Yes':
                print("\nGreat, let's play again!\n")
                maybe_play = not True
                play = True
            else:
                print('Please enter either yes or no.')
                input()
                maybe_play = not True
                play = not True


random_game()
