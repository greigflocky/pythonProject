import random


# This list is taken from the comprehensive list further down in the code, it takes our users letters and the same
# amount of falses to match the letters and if set to true will show the letter, if not will continue to print
# new lines.


def display(char_list, user_list):
    for i in range(0,len(char_list)):
        if user_list[i] == True:
            print(char_list[i], end = " ")
        else:
            print("_", end = " ")

# This function receives the players choice of "Easy, Medium, or Hard" and determines how many lives they receive

def user_lives(a):
    global lives
    lives = (a)

# This code reads the file containing the countries and seperates them into new lines. It then randomly selects a
# country from the list and selects it for the user to guess
# The while loop is in place to stop countries such as "Bosnia and Herzegovina" as they may be to long for player to
# guess (Potentially include this as difficulty feature at a later date?
# The word is uppercased to prevent capitilization during input breaking the code. the length of the word is also
# Determined here

f = open("C:/Users/greig/Documents/Code/Python/Hangman/Countries.txt", "r")
country_list = f.read().splitlines()
country_selected = random.choice(country_list)
while len(country_selected) > 10:
    country_selected = random.choice(country_list)
word_length = len(country_selected)
country_selected = country_selected.upper()

# This splits the list into the country selecteds amount of letters and assigns the same amount of falses to a
# differnet list. This will become clear later in the code

char_list = []
user_list = []
for i in range(0,word_length):
    char_list.append(country_selected[i])
    user_list.append(False)

# Welcome text for the user, asks for input and difficult before passing the users choice into a function parameter
# determining the amount of lives they have


print("Hi and welcome to hangman, before we start please enter your name")
user_name = input("")
print("Hi", user_name, "Thanks for playing my game! I really appreciate it ")
difficulty = input("Please enter your difficulty options, you can choose - EASY, MEDIUM, HARD")
difficulty = difficulty.upper()
if difficulty == "EASY":
    user_lives(10)
elif difficulty == "MEDIUM":
    user_lives(7)
elif difficulty == "HARD":
    user_lives(5)
else:
    difficulty = input("Please re enter either Easy, Medium, Hard")
print("Brilliant you have ", lives, "lives")
print("Here is the amount of words within the country")
# The solution is printed for testing purposes. It would not normally be shown
print(country_selected)

# Create a loop that will loop until the user runs out of lives, start by asking the user to guess a letter then
# Check to make sure the user only has inputted 1 letter only then check to see if that letter is in the
# Assigned country. If the user guesses everything within user list they win
# List comprehensions have been used. The user list value is set to true if the list of characters are equal
# to the users guessed letter and if not it is set to false. Enumerate returns the index and data

while lives >0:
    if all(user_list):
        print("CONGRATS", user_name.upper(), "YOU WON THE WORD WAS", country_selected)
        break
    display(char_list, user_list)
    user_letter = input("Please enter a letter!")
    user_letter = user_letter.upper()
    if len(user_letter) > 1:
        print("YOU CAN ONLY ENTER ONE LETTER AT A TIME")
        continue
    elif user_letter not in country_selected:
        print("Wrong")
        lives -= 1
        print(lives)
    if user_letter in char_list:
        user_list = [True if (c == user_letter or user_list[i] == True) else False for i,c in enumerate(char_list)]
    else:
        False

