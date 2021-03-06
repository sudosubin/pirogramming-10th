# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_list = list(secret_word)
    for secret_letter in secret_list:
        if secret_letter not in letters_guessed:
            secret_list[secret_list.index(secret_letter)] = '_'

    return ' '.join(secret_list)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    not_guessed = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in not_guessed:
            del not_guessed[not_guessed.index(letter)]

    return ''.join(not_guessed)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    - At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    - The user should start with 6 guesses

    - Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    - Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_warning = 3
    available_guesses = 6
    correct_guesses = 0
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secret_word))
    print("You have %d warnings left." % available_warning)
    print("------------")

    while available_guesses > 0:
        print("You have %d guesses left." % available_guesses)
        print("Available letters:", get_available_letters(letters_guessed))

        user_guess = input("Please guess a letter: ")[0]

        # strange guess
        if user_guess not in string.ascii_letters:
            available_warning -= 1
            print("Oops! That is not a valid letter. You have %d warnings left: %s" % (available_warning, get_guessed_word(secret_word, letters_guessed)))

        # duplicate guess
        if user_guess in letters_guessed:
            available_warning -= 1
            print("Oops! You've already guessed that letter. You have %d warnings left: %s" % (
            available_warning, get_guessed_word(secret_word, letters_guessed)))
            print("------------")
            continue

        # currect
        if user_guess in secret_word:
            letters_guessed.append(user_guess)
            print("Good guess: %s" % get_guessed_word(secret_word, letters_guessed))
            correct_guesses += 1
            if is_word_guessed(secret_word, letters_guessed):
                break
        # wrong
        else:
            letters_guessed.append(user_guess)
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            available_guesses -= 1

        print("------------")

    score = available_guesses * correct_guesses
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is: %d" % available_guesses)
    else:
        print("Sorry, you ran out of guesses. The word was %s." % secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if my_word == other_word:
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    possible_matched = []

    word_index = 0
    for word in wordlist:
        listed_word = list(' '.join(list(word)))
        if len(listed_word) == len(my_word):
            i = 0
            for my_letter in my_word:
                if my_letter != ' ' and my_letter != '_':
                    if my_word[i] != listed_word[i]:
                        break
                i += 1
                if i == len(my_word) - 1:
                    possible_matched.append(word)

    print(' '.join(possible_matched))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    available_warning = 3
    available_guesses = 6
    correct_guesses = 0
    letters_guessed = []

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secret_word))
    print("You have %d warnings left." % available_warning)
    print("------------")

    while available_guesses > 0:
        print("You have %d guesses left." % available_guesses)
        print("Available letters:", get_available_letters(letters_guessed))

        user_guess = input("Please guess a letter: ")[0]

        if (user_guess == "*"):
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("------------")
            continue

        # strange guess
        if user_guess not in string.ascii_letters:
            available_warning -= 1
            print("Oops! That is not a valid letter. You have %d warnings left: %s" % (available_warning, get_guessed_word(secret_word, letters_guessed)))

        # duplicate guess
        if user_guess in letters_guessed:
            available_warning -= 1
            print("Oops! You've already guessed that letter. You have %d warnings left: %s" % (
            available_warning, get_guessed_word(secret_word, letters_guessed)))
            print("------------")
            continue

        # currect
        if user_guess in secret_word:
            letters_guessed.append(user_guess)
            print("Good guess: %s" % get_guessed_word(secret_word, letters_guessed))
            correct_guesses += 1
            if match_with_gaps(get_guessed_word(secret_word, letters_guessed), secret_word):
                break
        # wrong
        else:
            letters_guessed.append(user_guess)
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            available_guesses -= 1

        print("------------")

    score = available_guesses * correct_guesses
    if match_with_gaps(get_guessed_word(secret_word, letters_guessed), secret_word):
        print("Congratulations, you won!")
        print("Your total score for this game is: %d" % available_guesses)
    else:
        print("Sorry, you ran out of guesses. The word was %s." % secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
