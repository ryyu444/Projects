# Code for a Wordle Clone
import random

def wordlist(file):
    infile = open(file, "r")
    wordlist = []

    for line in infile:
        line = line.strip()
        wordlist.append(line)

    return wordlist

def replay(num_guesses, ans, incorrect):
    printed, replay, end = False, True, False
    one_guess = "Great work in getting it in 1 try!"
    guessed = "Congrats! You took " + str(num_guesses) + " guesses out of 5!"

    if num_guesses == 1 and incorrect == False:
        print(one_guess)
        print("-" * len(one_guess))
        printed = True  
    if (1 < num_guesses <= 5 and incorrect == False):
        print(guessed)
        print("-" * len(guessed))
        printed = True

    if num_guesses > 5:
        print("Sorry, you ran out of tries.")
        print("Better luck next time!")
        print("The word was...")
        print("(>._.)> ~ " + ans + " ~ <(._.<)")
        printed = True
        
    if printed:
        while True:
            response = input("Would you like to play again?: ")

            if response.lower() == "yes":
                replay = True
                break
            if response.lower() == "no":
                end = True
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        print("-" * (31 + len(response)))

    return replay, end, printed

def Wordle(wordlist):
    incorrect, rply = True, False
    guesses = 0
    used_letters = []
    right_letters = []
    answer = random.choice(wordlist)
    # print(answer)
    print("-" * 23)

    while incorrect:

        output = "" # Empty string
        letters = {} # Map


        user_input = input("Enter your guess: ").lower()
        # used_letters.sort()
        # print("Used Letters: " + str(used_letters))

        if len(user_input) != len(answer):
            print("Invalid guess")
            print("-" * len("Invalid guess"))
            continue

        # Puts all characters in OUTPUT into map
        for i in range(len(answer)):
                letters[i] = answer[i]

        # Goes through INPUT & compares it to OUTPUT
        for i in range(len(user_input)):
            if user_input[i] not in used_letters:
                used_letters.append(user_input[i])
            # If it is the same, add a "*" to output & remove the key from the map
            if user_input[i] == answer[i]:
                output += "*"
                letters.pop(i)
                if user_input[i] not in right_letters:
                    right_letters.append(user_input[i])
            # If not, add a "-" to the output
            else:
                output += "-"

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
                        if user_input[h] not in right_letters:
                            right_letters.append(user_input[h])
                # Key is not in map --> Skip iteration
                else:
                    continue

        if user_input == answer:
            incorrect = False
        
        print(output)
        correct_str = "Correct Letters: " + str(right_letters)
        print(correct_str)
        print("-" * len(correct_str))
        guesses += 1

        rply, end, printed = replay(guesses, answer, incorrect)
        
        if (printed):
            return rply, end

def main():
    play = True
    end = False

    while (play and not end):
        wlist = wordlist("wordlelist.txt")
        play, end = Wordle(wlist)

    return 0

main()