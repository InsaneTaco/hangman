import random as r, sys

#opens word list text file in read mode
with open("words.txt", "r+") as word_list_file:
    #reads file
    word_data = word_list_file.read()
    #splits the data wherever a space occurs
    words_in_list = word_data.upper().split(" ")

turn_count = 0
wrong_guesses = 0
word_board_list = []

# function that prints the board and the hangman dude
def print_board():
    word_board = ""
    for word_list_item in word_board_list:
        word_board += word_list_item + " "
    print(f"\n{word_board}")

# dictionary that tells the amount of wrong guesses to which limb lost; will be used later lol
limb_lost = {
    1: "your head",
    2: "your torso",
    3: "your arm",
    4: "another arm for me stew",
    5: "your leg"
}

print("""\nHi, and welcome to hangman! 
Here are the rules:
    - On your turn, you guess a letter.
    - If you're correct, then cool. It will tell you and then you will know one letter.
    - If you are incorrect, then a limb will be placed on the person hanger.
    - When a full stick figure is assembled, then you lose.
    - Once you are pretty sure what the word is, you can type an entire word as your guess.
    - You can also just play it safe and keep getting letters until you get the entire word.
    - JUST BE WARNED, because if you type an entire word and it is wrong, you instantly lose.
    - Have fun!
    
Hit enter to continue.""")
input()

# randomly selects the word, and then tells the player the character count
word = r.choice(words_in_list)
print(f"\nThe word has {len(word)} characters.")
for i in range(len(word)):
    # prints empty underscores because nothing has been guessed yet
    word_board_list.append("_")
print_board()



# main game loop
while True:
    turn_count += 1
    word_ch_spot = -1
    matches_found = False

    guess = input("\nguess: ").upper()
    # checks if the player won
    if guess == word:
        print("\nLet's go, you didn't die! You win!")
        sys.exit()
    # check if the player failed to guess the word
    elif len(guess) != 1:
        print(f"\nLol, ur done. Imagine being hung. The word was {word}.")
        sys.exit()
    # if the person guesses a correct letter
    else:
        for word_ch in word:
            word_ch_spot += 1
            if guess == word_ch:
                word_board_list[word_ch_spot] = guess
                matches_found = True
        # if the player did not guess a correct letter
        if matches_found == False:
            wrong_guesses += 1
            if wrong_guesses == 6:
                print(f"Ur done. You lost. I have all ur limbs! The word was {word}")
                sys.exit()
            else:
                print("Wrong! There goes " + limb_lost.get(wrong_guesses) + "!")
                    
    print_board()