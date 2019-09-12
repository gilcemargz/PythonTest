# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for x in secretWord:
        if x not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    for x in secretWord:
        if x in lettersGuessed:
            word += x
        else:
            word += '_ '

    return word.strip()


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    return ''.join([x for x in map(chr, range(97, 123)) if x not in lettersGuessed])


def hangman(secretWord):
    guesses = 8
    letters = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    print('-------------')

    while True:
        print('You have {} guesses left.'.format(guesses))
        print('Available letters:', getAvailableLetters(letters))
        ll = input('Please guess a letter:')
        ll = ll.lower()

        if ll in letters:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters))
        else:
            if ll not in secretWord:
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, letters))
                guesses -= 1
            letters.append(ll)

            if ll in secretWord:
                print('Good guess:', getGuessedWord(secretWord, letters))

        print('-------------')
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
            break
        elif isWordGuessed(secretWord, letters):
            print('Congratulations, you won!')
            break


if __name__ == '__main__':
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    secretWord = 'exxe'
    hangman(secretWord)

    # print(isWordGuessed('apple', ['e', 'a', 'l', 'p', 'r', 's']))
    # print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))
    # print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
