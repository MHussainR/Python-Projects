import random

def check_word (guess, word):
    b = ''
    guess = guess.lower()
    word = word.lower()
    for letters in range(5):
        if guess[letters] in word:
            if word[letters] == guess[letters]:
                b += '1'
            else:
                b += '0'
        else:
            b += '-'

    return b


def game (attempts, words, word):
    if attempts == 7:
        print ()
        print ('You failed to guess the word.')
        print ()
        print ('The correct word is :', word)
        return
    else:
        print ('Attempt Number :', attempts, 'guess a 5 letter word.')
        a = input().lower()
        if len(a) != 5:
            print ('You cannot guess a word with more or less than 5 letters')
            game (attempts, words, word)
        # elif a not in words:
        #     print ('The word is not in the list')
        #     game (attempts, words, word)
        else:
            guess = check_word (a, word)
            if guess == '11111':
                print ('You guessed it right, the correct word is:', word)
            else:
                print (guess)
                game(attempts+1, words, word)
        

def main (words):
    print ('##### RULES #####')
    print ()
    print ('1. If you get a "-" underneath a certain letter, that means that the letter is not present in the word.')
    print ()
    print ('2. If you get a "0" underneath a certain letter, that means that the letter is present in the word but is not in the rigth place.')
    print ()
    print ('3. If you get a "1" underneath a certain letter, that means that the letter is correct and at the right place.')
    print ()
    print ('You cannot guess a word with more or less than 5 words.')
    print ()
    print ('Let the game begin.....')
    print ()
    print ()
    word = random.choice (words)
    game (1, words, word)


word_book = open('sgb-words.txt','r+')
words = word_book.readlines()

# words = ['shark', 'crane', 'brain', 'plane', 'plain', 'stain', 'claim', 'ulcer', 'nicer', 'boxer', 'cater', 'water', 'piece', 'niece', 'seize', 'table', 'haram', 'halal', 'eagle', 'bacon', 'chair', 'hairy', 'fairy', 'fatty', 'shame', 'woody', 'would', 'shold', 'shade', 'brake', 'break', 'taraiq', ]

main (words)