import random #10.0
import os

# Function to choose a random word from a list
def choose_secret_word():
    words = ["poptropica", "satisfactory"]
    return random.choice(words)

# Function to initialize the hidden word with '*' characters
def initialize_hidden_word(secret_word):
    return ["*"] * len(secret_word)

# Function to print the hidden word with spaces between characters
def print_word_to_guesses(hidden_word):
    print("".join(hidden_word))

# Function to write the game results to a file
def write_game_results(player1, player2, winner, secret_word, player1_letter_guesses, player1_word_guesses, player2_letter_guesses, player2_word_guesses):
    filename = "wordguess_results.txt"
    mode = "a" if os.path.exists(filename) else "w"
    with open(filename, mode) as file:
        if mode == "w":
            file.write("player 1\tPlayer 2\tWinner\tSecret Word\tPlayer 1 Letter Guesses\tPlayer 1 Word Guesses\tPlayer 2 Letter Guesses\tPlayer 2 Word Guesses\n")
        player1_result = "WON" if winner == player1 else "LOST"
        player2_result = "WON" if winner == player2 else "LOST"
        file.write(f"{player1}\t{player2}\t{player1_result}\t{secret_word}\t{player1_letter_guesses}\t{player1_word_guesses}\t{player2_letter_guesses}\t{player2_word_guesses}\n")

# Get player names
player1 = input("What is the name of player 1? ")
player2 = input("What is the name of player 2? ")
print(f"Welcome, {player1} and {player2}! Let's play the Word Guessing Game.")

# Choose secret word and initialize game variables
words = ["poptropica", "satisfactory"]
secret_word = choose_secret_word()
hidden_word = initialize_hidden_word(secret_word)

attempts_left = 3
current_player = player1
player1_letter_guesses = 0
player1_word_guesses = 0
player2_letter_guesses = 0
player2_word_guesses = 0

# Main game loop
while attempts_left > 0 and "*" in hidden_word:
    # print_word_to_guesses(hidden_word)
    letter = input(f"\n{current_player}, guess a letter: ")

    # Check if the guessed letter is in the secret word
    if letter in secret_word:
        count_occurrences = secret_word.count(letter)
        # Change lines 59 and 60 to match if else from lines 76-79
        if current_player == player1:
            player1_letter_guesses += 1
        else:
            player2_letter_guesses += 1

        # Update the hidden word without revealing positions of letters (test case #1)
        # for i in range(len(secret_word)):
        #     if secret_word[i] == letter:
        #         hidden_word[i] = letter
    else:
        attempts_left -= 1
        print(f"Womp Womp, {current_player}! You have {attempts_left} attempts left.")

    # Optionally guess the word
    if attempts_left > 0:
        guess_word = input(f"\n{current_player}, do you want to guess the word? (yes/no)")
        if guess_word == "yes":
                word_guess = input(f"\n{current_player}, guess the word: ")
                if word_guess.lower() == secret_word:
                    print(f"Congratulations, {current_player}! You guessed the word: {secret_word}")
                    if current_player == player1:
                        player1_word_guesses += 1
                    else:
                        player2_word_guesses += 1
                    break  # Exit the loop if word is guessed correctly
                else:
                    print(f"Sorry, {current_player}! That's not the word.")
                    attempts_left -= 1

#Test case number 1, word guessing is mandatory.
#if attempts_left > 0:
   # word_guess = input(f"\n{current_player}, guess the word: ")
    #if word_guess.lower() == secret_word:
        #print(f"Congratulations, {current_player}! You guessed the word: {secret_word}")
        #if current_player == player1:
            #player1_word_guesses += 1
        #else:
            #player2_word_guesses += 1
        #break  # Exit the loop if word is guessed correctly
    #else:
        #print(f"Sorry, {current_player}! That's not the word.")
        #attempts_left -= 1


    # Switch players if current player has used all their attempts of word is guessed
    if attempts_left == 0 or "*" not in hidden_word:
        current_player = player2 if current_player == player1 else player1
        attempts_left = 3

# Whichever player guessed the most letters
player1_final_score = player1_letter_guesses if current_player == player1 else player2_letter_guesses
player1_final_score = player2_letter_guesses if current_player == player2 else player2_letter_guesses

# Display result
if "*" not in hidden_word:
    print(f"Congratualtions, {current_player}! You guessed the word: {secret_word}")

# Write results to a file
write_game_results(player1, player2, "*" not in hidden_word, secret_word, player1_letter_guesses, player1_word_guesses, player2_letter_guesses, player2_word_guesses)
