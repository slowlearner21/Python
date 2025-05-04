import random

word_list = ["elephant","switzerland","antarctica"]
word_chosen = random.choice(word_list)
print(word_chosen)

placeholder = ""
word_length = len(word_chosen)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over =  False
correct_letters = []
while not game_over:
    guess_word = input("Guess the word: ").lower()
    print(guess_word)

    display = ""

    for letter in word_chosen:
        if letter == guess_word:
            display += letter
            correct_letters.append(guess_word)
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_"
    print(display)
    
    if "_" not in display:
        game_over = "True"
        print("You win. ")

