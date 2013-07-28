# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def concatenateletters(str_input):
    ##concatenate all letters without spaces or other characters
    out_str = ''
    for i in xrange(0,len(str_input)):
                        out_str+=str_input[i]
    return out_str

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# your code begins here!



##initialize variables
choose_word=choose_word(wordlist)
done=0
guesses=2*len(choose_word)
solution=['_',]
for i in xrange(1,len(choose_word)):
    solution.append('_')

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(len(choose_word)) + ' letters long'
print '-------------'

##main program loop is
while done !=1:
    ##Prompt input
    print 'You have guesses ' + str(guesses) +' left.'
    print 'Available letters: ' + concatenateletters(letters)
    guess=raw_input('Please guess a letter: ')

    ##Check if letter is available and remove from list
    if letters.count(guess)>0:
        letters.remove(guess)
        
        ##Check if letter is in word
        if choose_word.count(guess)>0:
            ##loop through all letters to check for matches and replace in solution
            for i in xrange(0,len(choose_word)):
                if choose_word[i]==guess:
                    solution[i]=guess
            print 'Good guess: ' + concatenateletters(solution)
            print '-------------'

            ##check to see if solution matches chosen word
            if choose_word==''.join(solution):
                print 'Congratulations, you won!'
                done=1
        ##if not in word decrease guesses
        else:
            print 'That letter is not in my word: ' + concatenateletters(solution)
            print '-------------'
            guesses -=1
    else:
        print 'That letter is not available. Please enter another'
        print '-------------'

   

    if guesses==0:
        ##Exit main loop after the user has run out of guesses
        done=1




