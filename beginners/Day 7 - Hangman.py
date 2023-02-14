import os
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['aardvark', 'balloon', 'cactus', 'daffodil', 'elephant', 'frosty', 'giraffe', 'hippopotamus', 'igloo', 'jungle', 'kangaroo', 
'lemur', 'mountain', 'nose', 'octopus', 'penguin', 'quilt', 'rhinoceros', 'squirrel', 'toucan', 'umbrella', 'vulture', 'walrus', 'xylophone', 
'yak', 'zebra', 'apple', 'banana', 'carrot', 'doughnut', 'eggplant', 'fig', 'grape', 'honeydew', 'iceberg', 'jalapeno', 'kiwi', 'lemon', 
'mango', 'nectarine', 'orange', 'peach', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 
'yellow', 'zucchini', 'alligator', 'bear', 'cougar', 'deer', 'elephant', 'flamingo', 'gorilla', 'hippopotamus', 'iguana', 'jaguar', 'koala', 
'llama', 'mongoose', 'narwhal', 'opossum', 'panther', 'quokka', 'rhinoceros', 'sloth', 'tiger', 'urchin', 'vulture', 'walrus', 'xenops', 'yak', 
'zebra', 'archer', 'baker', 'carpenter', 'doctor', 'electrician', 'firefighter', 'gardener', 'hairdresser', 'investigator', 'jeweler', 'knitter', 
'lawyer', 'musician', 'nurse', 'optometrist', 'plumber', 'quilter', 'receptionist', 'surgeon', 'teacher', 'university', 'veterinarian', 
'writer', 'x-ray', 'yoga', 'zoologist']

play_again = True
while play_again:
    chosen_word = random.choice(word_list)
    display = []
    for letter in chosen_word:
            display.append("_")

    lives = 6
    game = True
    os.system('clear')
    while game:
        
        if lives == 6:
            print (stages[6])
        elif lives == 5:
            print (stages[5])
        elif lives == 4:
            print (stages[4])
        elif lives == 3:
            print (stages[3])
        elif lives == 2:
            print (stages[2])
        elif lives == 1:
            print (stages[1])
        elif lives == 0:
            print (stages[0])

        print (' '.join(display))

        guess = input("\nguess a letter: ").lower()   
        
        if guess in chosen_word:
            print("Right")
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    display[i] = guess         
        else:
            print("Wrong")

       

        if "_" in display:
            game = True
        else: 
            game = False

        if guess not in chosen_word:
            lives -= 1
            if lives <=0:
                print ("You lose")
                game = False
        os.system('clear')


    again = input("would you like to play again? y/n: ")
    if again != "y":
        play_again = False
