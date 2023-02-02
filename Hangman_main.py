from Art import logo, stages
from Words import word_list
from Clear_function import clear
import random


# Function to ask the player if he wants to play again
def play_again():
    if_play_again = input("Would you like to play again? Y/N: ")
    if if_play_again.upper() == "Y":
        clear()
        return True


print(logo)

while True:
    chosen_word = random.choice(word_list)

    # Printing a chosen word for debugging purposes
    # print(f'The solution is {chosen_word}.')

    # To display the encrypted secret word
    display_list = []

    # Chosen (random) word in the form of the list
    chosen_word_list = []

    # List of the letters already used by a player
    list_of_guesses = []

    # Adding value to display_list and chosen_word_list based on the chosen word
    for letter in chosen_word:
        display_list.append("_")
        chosen_word_list.append(letter)

    # boolean to track when the game is over
    end_of_game = False
    lives = 6

    while not end_of_game:
        print(display_list)
        print(f"List is letters you've already tried is: {list_of_guesses}")
        print(stages[lives])

        guess = input("Guess a letter: ").lower()

        clear()

        # adding a guessed letter to the list of list_of_guesses
        if guess not in list_of_guesses:
            list_of_guesses.append(guess)
        if guess in display_list:
            print(f"Hey! {guess} is already there!")

        # updating display_list if the player guessed the letter
        for i in range(len(chosen_word_list)):
            if chosen_word[i] == guess:
                display_list[i] = guess

        # reducing lives
        if guess not in chosen_word:
            lives -= 1
            print(f"Sorry, letter {guess} is not in this word, you lose the life!")

            # output when the player run out of the guesses
            if lives == 0:
                print(stages[0])
                print(f"Sorry, you lose! The missing word was '{chosen_word}'")
                end_of_game = True

        # output when the player guessed all the letters - display list doesn't contain '_' anymore
        if "_" not in display_list:
            print(f"Good job! The missing word was '{chosen_word}'")
            end_of_game = True

    # breaking the loop when the player doesn't want to start another game
    if not play_again():
        break
