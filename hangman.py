import os
from random import choice

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)
WORDS = ['barbarous',
'government',
'godly',
'glue',
'glove',
'throat',
'harmony',
'knock',
'continue',
'nifty',
'raise',
'toothpaste',
'obeisant',
'pine',
'stay',
'faulty',
'shave',
'applaud',
'blink',
'spiteful',
'suggest',
'paint',
'ancient',
'turkey',
'pocket',
'answer',
'hover',
'cherries',
'happy',
'quixotic',
'calculate',
'meat',
'owe',
'pie',
'sprout',
'reaction',
'devilish',
'meeting',
'actually',
'rural',
'reproduce',
'burn',
'melted',
'fat',
'gratis',
'flowery',
'decorous',
'alive',
'bridge',
'boiling',
'signal',
'vase',
'homely',
'amuck',
'mine',
'eatable',
'dysfunctional',
'useless',
'horses',
'snakes',
'toes',
'school',
'claim',
'growth',
'resonant',
'appreciate',
'heartbreaking',
'tickle',
'stick',
'delightful',
'murky',
'quince',
'moaning',
'transport',
'helpful',
'unbecoming',
'remarkable',
'quartz',
'name',
'afraid',
'quarrelsome',
'chance',
'judicious',
'foamy',
'bee',
'book',
'tender',
'fall',
'enter',
'gaping',
'decisive',
'drunk',
'wicked',
'day',
'annoyed',
'weary',
'root',
'shade',
'waves',
'equable']
def hangman():
    os.system('clear')
    name = input("Hello, stranger. What is your name? ") 
    print("Hello, " + name + ", Let's play a game!")                     # Ввод имени 
    word = choice(WORDS) 
                                                                         # Выбор из списка слов 
    turns = len(HANGMAN)
                                                                         # Рисунок стадии человечка 
    hidden_letter =  '_' * len(word)                                   # Скрытая буква = кол-ву элементов в слове  
    used_letter = []                                                     # Вывод введеных букв 
    wrong = 0 
    counter = 7
    while wrong < turns and hidden_letter != word:                       # Если кол-во букв и попыток не равняется загаданному слову 
         os.system('clear')
         noList= list(hidden_letter)
         print('                                    HANGMAN')
         print(HANGMAN[wrong])                                           # Печать персонажа
         print ('\nAttempts remain: ' ,counter)
         print('\nYou have already used these letters:\n', used_letter)  
         print('\nYour hidden word:\n', ' '.join(noList))    
         guess = input('\nEnter your letter: ')

         while guess in used_letter:                                      # Цикл для вывода угаданной буквы в слове 
             print('You have already guessed that letter ' + guess )      
             guess = input('Enter your letter: ')                         # Ввод предполагаемой буквы 

         used_letter.append(guess)                                        # Угаданная буква есть в скрытом слове                                     

         if guess in word:                                                # буква есть в слове и выполняются условия 
             print('\nCorrect! \'' + guess + '\' is in the word ')        

             new = ''                                                       

             for i in range(len(word)):
                 if guess == word[i]:
                     new =new + guess 
                 else:
                     new += hidden_letter[i]
             hidden_letter = new                                  
         else:
             os.system('clear')
             print('\nSorry, the letter \'' + guess + '\' is not in the word.')
             wrong += 1
             counter -=1                                                     # Неправильно +1 
    if wrong == turns:                                                      # Ф-ция подсчета жизней 
        print('\nOops! Looks like you was hanged')
         
    else:
        os.system('clear')
        print('\nCongratulations! You guessed the word')

    print('\nThe hidden word was \'' + word + '\'')

ans = 'yes'                                                                 # Подключить выбор 
while ans == 'yes':
    
    hangman()
    print('Do you wanna play again? (yes/no)')
    ans = input()
    
else:
    print('As you want. See you next time. Bye!')









