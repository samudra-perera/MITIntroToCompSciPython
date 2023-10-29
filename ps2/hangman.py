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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
    # return 'tact'

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #Check if the letters in the word are in letters guessed, if not return false
    #After checking all letters return True is False was not returned
    for letter in  secret_word:
        if(letter not in letters_guessed):
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = ''

    for letter in secret_word:
        if(letter in letters_guessed):
            guess += (' ' + letter)
        else:
            guess += '_ '
    return guess



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    letterAvailable = ''

    for letter in letters:
        if(letter in letters_guessed):
            continue
        else:
            letterAvailable += letter
    return letterAvailable

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_guesses = 6
    letters_guessed = []
    num_of_warnings = 3
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long')
    print('----------------------')
    print('You have ' + str(num_of_guesses) + 'guesses left')
    print('Available letters: ' + get_available_letters(letters_guessed))

    while(is_word_guessed(secret_word, letters_guessed) == False):
      #Player Input
      letter_selection = input('Please guess a letter: ')
      #Lowercase selection for input validation
      letter_selection.lower()
      
      #Check if a character assume single char or of the player already guessed the letter
      if((letter_selection.isalpha() == False)):
          num_of_warnings -= 1
          if(num_of_warnings == -1):
              print('You have reached the limit of 3 warnings and have lost the game!')
              break
          print('Oops! That is not a valid letter. You have' + str(num_of_warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
      
      if((letter_selection in letters_guessed)):
          num_of_warnings -= 1
          if(num_of_warnings == -1):
              print('You have reached the limit of 3 warnings and have lost the game!')
              break



      #Add letter to guessed array if not already in the array and check if it is part of the secret word
      letters_guessed.append(letter_selection)
      if letter_selection in 'aeiou':
          if letter_selection not in secret_word:
              num_of_guesses -= 2
          if(num_of_guesses == 0):
              print('---------------------')
              print('Sorry, you ran out of guesses. The word was ' + secret_word)
              break
          print('Oops that letter is not in my word')
      elif letter_selection not in secret_word:
          num_of_guesses -= 1
          if(num_of_guesses == 0):
              print('---------------------')
              print('Sorry, you ran out of guesses. The word was ' + secret_word)
              break
          print('Oops that letter is not in my word')
      else:
          print('Good guess ' + get_guessed_word(secret_word, letters_guessed))


      #If passes input validation do this
      print('---------------------')
      print('You have ' + str(num_of_guesses) + 'guesses left')
      print('Available letters: ' + get_available_letters(letters_guessed))
      print('You have ' + str(num_of_warnings) + ' warnings left')
      print('You have guessed so far ' + get_guessed_word(secret_word, letters_guessed))

      if(is_word_guessed(secret_word, letters_guessed) == True):
          unique_letters = set(secret_word)
          score = num_of_guesses * len(unique_letters)
          print('Congratulations you won!')
          print('Your total score for this game is: ' + str(score))
          break




# game = hangman(secret_word)
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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
    #If lengths aren't equal no way the words can be equal
    
    word = ''

    for char in my_word:
        if(char == ' '):
            continue
        else:
            word += char
            

    if(len(word) != len(other_word)):
        return False

    for n in len(word):
        if(word[n] == '_'):
            continue
        elif(word[n] != other_word[n]):
            return False
    return True
        
            

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    temp_word = ''
    list_of_solutions = []

    #Remove spaces from guessed word
    for char in my_word:
        if(char == ' '):
            continue
        else:
            temp_word += char

    #Iterate through word list
    #If word lengths are equal iterate through to check if letters at same index are not equal
    for word in wordlist:
        if len(word) == len(temp_word):
            word_not_in = False
            for n in range(len(word)):
                if(temp_word[n] != word[n] and temp_word[n] != '_'):
                    word_not_in = True
                    break
            if(word_not_in == False):
                list_of_solutions.append(word)
      
    return list_of_solutions
            



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_guesses = 6
    letters_guessed = []
    num_of_warnings = 3
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long')
    print('----------------------')
    print('You have ' + str(num_of_guesses) + 'guesses left')
    print('Available letters: ' + get_available_letters(letters_guessed))

    while(is_word_guessed(secret_word, letters_guessed) == False):
      #Player Input
      letter_selection = input('Please guess a letter: ')
      #Lowercase selection for input validation
      letter_selection.lower()

      if(letter_selection == '*'):
          print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
          
      
      #Check if a character assume single char or of the player already guessed the letter
      if((letter_selection.isalpha() == False) and (letter_selection != '*')):
          num_of_warnings -= 1
          if(num_of_warnings == -1):
              print('You have reached the limit of 3 warnings and have lost the game!')
              break
          print('Oops! That is not a valid letter. You have' + str(num_of_warnings) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
      
      if((letter_selection in letters_guessed)):
          num_of_warnings -= 1
          if(num_of_warnings == -1):
              print('You have reached the limit of 3 warnings and have lost the game!')
              break



      #Add letter to guessed array if not already in the array and check if it is part of the secret word
      if(letter_selection != '*'):
        letters_guessed.append(letter_selection)
      
      if letter_selection in 'aeiou':
          if letter_selection not in secret_word:
              num_of_guesses -= 2
          if(num_of_guesses == 0):
              print('---------------------')
              print('Sorry, you ran out of guesses. The word was ' + secret_word)
              break
          print('Oops that letter is not in my word')
      elif letter_selection not in secret_word and letter_selection != '*':
          num_of_guesses -= 1
          if(num_of_guesses == 0):
              print('---------------------')
              print('Sorry, you ran out of guesses. The word was ' + secret_word)
              break
          print('Oops that letter is not in my word')
      else:
          print('Good guess ' + get_guessed_word(secret_word, letters_guessed))


      #If passes input validation do this
      print('---------------------')
      print('You have ' + str(num_of_guesses) + 'guesses left')
      print('Available letters: ' + get_available_letters(letters_guessed))
      print('You have ' + str(num_of_warnings) + ' warnings left')
      print('You have guessed so far ' + get_guessed_word(secret_word, letters_guessed))
      print(len(get_guessed_word(secret_word, letters_guessed)))

      if(is_word_guessed(secret_word, letters_guessed) == True):
          unique_letters = set(secret_word)
          score = num_of_guesses * len(unique_letters)
          print('Congratulations you won!')
          print('Your total score for this game is: ' + str(score))
          break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
