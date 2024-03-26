# assignment: programming assignment 1
# author: Rutujit(RJ) Mallikarjuna
# date: Januray 23, 2023
# file: hangman.py is a program which performs the game, hangman.
# input: The size of the word you want to play with and the number of lives the user wants. 
# output: Wether or no tthey won the game, the amount of lives they took, the word they guessed and wether or no they want to play again.
from random import choice, random
import random

with open("dictionary.txt", "r") as dictionary_file:
    listofAllWords = []
    for line in dictionary_file:
        line = line.strip()
        listofAllWords.append(line)
# make a dictionary.txt in the same folder where hangman.py is located
# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary(filename) :
    mydict = {}
    max_size = 12

    for i in range(2, max_size+1):
        myList = []
        for word in listofAllWords:
            if len(word) == i:
                myList.append(word)
        #print('i', myList)
        mydict[i] = myList
    return mydict
'''
# print the dictionary (use only for debugging)
def print_dictionary(mydict) :
    max_size = 12
    print(mydict)
'''
# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    print('Please choose a size of a word to be guessed [3 - 12, default any size]:')
    sizeOfWord = input()
    try:
        sizeOfWord = int(sizeOfWord)
        print('The word size is set to',str(sizeOfWord)+'.')
    except:
        sizeOfWord = None
        print('A dictionary word of any size will be chosen.')
    if sizeOfWord == None:
        sizeOfWord = random.randint(3,12)
    elif not ((3 <= sizeOfWord) and (sizeOfWord <= 12)):
        sizeOfWord = None
        print('A dictionary word of any size will be chosen.')
    print('Please choose a number of lives [1 - 10, default 5]:')
    numOfLives = input()
    try:
        numOfLives = int(numOfLives)
    except:
        numOfLives = 5
    if not ((numOfLives>=1) and (numOfLives <= 10)):
        numOfLives = 5
    print('You have',numOfLives,'lives.')
    return (sizeOfWord, numOfLives)


# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    # remove after debugging the dictionary function import_dictionary

    # print a game introduction
    print('Welcome to the Hangman Game!')

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:

    # set up game options (the word size and number of lives)
        wordSize, numLives = get_game_options()
    
    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
        if wordSize:
            word = choice(dictionary[wordSize]).lower()
        else:
            wordSize = choice(range(3, 12+1))
            word = choice(dictionary[wordSize]).lower()
        usedLetters = []
        currentLives = numLives
        correctLetters = []
        spaces = []
        for i in range(len(word)):
            if word[i] != '-':
                spaces.append('__')
            else:
                spaces.append('-')
        # START GAME LOOP   (INNER PROGRAM LOOP)
        while True:
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            print('Letters chosen: ', end='')
            if len(usedLetters) >= 1:
                for i in range(len(usedLetters)-1):
                    print(usedLetters[i].upper(), end=', ')
                print(usedLetters[len(usedLetters)-1].upper(), end='')
            print()
            for i in spaces:urrentLives, end=' '
            for i in range(numLives):
                print(i, end=' ')
                print(' lives:', c- currentLives)
                print('X', end='')
            for i in range(currentLives):
                print('Oend','')
            print()
            if currentLives == 0:
                print('You lost. The word is', word.upper()+'!')
                break
            elif '__' not in spaces:
                print('Congratulations!!! You won! The word is ', word.upper(), '!')
                break
        # ask the user to guess a letter
            print('Please choose a new letter >')
            guessLetter = input()
            while True:
                if guessLetter in usedLetters:
                    print('You have already chosen this letter.')
                    print('Please choose a new letter >')
                    guessLetter = input()
                elif not guessLetter.isalpha() or len(guessLetter) != 1:
                    print('Please choose a new letter >')
                    guessLetter = input()
                else:
                    if guessLetter in word:
                        print('You guessed right!')
                        usedLetters.append(guessLetter)
                    else:
                        print('You guessed wrong, you lost one life.')
                        currentLives -= 1
                    usedLetters.append(guessLetter)
                    break
        # update the list of chosen letters
            for i in word:
                if i in usedLetters:
                    for j in range(len(word)):
                        if word[j] == i:
                            spaces[j] = i.upper()
        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)
        print('Would you like to play again [Y/N]?')
        continueOrNot = input()
        if continueOrNot.lower() == 'n':
            break
        elif continueOrNot.lower() == 'y':
            continue
    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program