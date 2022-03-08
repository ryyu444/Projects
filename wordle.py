# Code for a Wordle Clone

import random

def wordlist(file):
    infile = open(file, "r")
    wordlist = []

    for line in infile:
        line = line.strip()
        wordlist.append(line)

    return wordlist

def Wordle(wordlist):
    incorrect = True
    guesses = 0
    used_letters = []
    answer = random.choice(wordlist)
    print(answer)

    while incorrect:

        output = "" # Empty string
        letters = {} # Map

        if guesses == 5:
            incorrect = False
            
            print()
            print("Sorry, you ran out of tries...")
            print("The answer was " + answer + "." + "\n")
            
            response = input("Would you like to try again?: ")
            print()
            
            if response.lower() == "yes":
                incorrect = True
                guesses = 0
            if response.lower() == "no":
                break

        user_input = input("Enter your guess: ").lower()
        used_letters.sort()
        print("Used Letters: " + str(used_letters))

        if len(user_input) != len(answer):
            print("Invalid guess" + "\n")
            continue

        # Puts all characters in OUTPUT into map
        for i in range(len(answer)):
                letters[i] = answer[i]

        # Goes through INPUT & compares it to OUTPUT
        for i in range(len(user_input)):
            # If it is the same, add a "*" to output & remove the key from the map
            if user_input[i] == answer[i]:
                output += "*"
                letters.pop(i)
            # If not, add a "-" to the output
            else:
                output += "-"
                if user_input[i] not in used_letters:
                    used_letters.append(user_input[i])

        # Goes through INPUT STR
        for h in range(len(answer)):
            # Goes through KEYS in map
            for j in range(len(answer)):
                # IF the key is in the map
                if j in letters:
                    # If the input string character is in the map & the output at that position is not "*"
                    # Replace the - at that position with a +
                    # Remove the key from the map
                    if user_input[h] == letters[j] and output[h] != "*":
                        output = output[:h] + "+" + output[h+1:]
                        letters.pop(j)
                        if user_input[h] in used_letters:
                            used_letters.remove(user_input[h])
                # Key is not in map --> Skip iteration
                else:
                    continue

        if user_input == answer:
            incorrect = False
        
        print(output + "\n")
        guesses += 1

    if guesses == 1:
        print("Great work in getting it in 1 try!")
    elif 1 < guesses <= 5 and incorrect == False:
        print("Congrats! You took " + str(guesses) + " guesses out of 5!")
    else:
        print("Better luck next time!")

def main():
    wlist = wordlist("wordlelist.txt")
    Wordle(wlist)

    return

main()