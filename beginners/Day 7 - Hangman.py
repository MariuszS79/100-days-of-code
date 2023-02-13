#Step 1 
import random

word_list = ['ability', 'absence', 'academy', 'account', 'accuse', 'achieve', 'acquire', 'address', 'advance', 'advice', 'affect', 'afford', 'against', 'airline', 'alcohol', 'allege', 'already', 'amazing', 'analyze', 'anger', 'animal', 'annual', 'answer', 'anxiety', 'apology', 'appoint', 'approve', 'argue', 'around', 'arrival', 'article', 'artist', 'aspect', 'assault', 'assert', 'assess', 'assign', 'assist', 'assume', 'athlete', 'attack', 'attempt', 'attract', 'auction', 'average', 'awesome', 'balance', 'barrier', 'beauty', 'believe', 'benefit', 'between', 'beyond', 'billion', 'biology', 'bishop', 'blanket', 'bottle', 'boundary', 'bravery', 'brother', 'builder', 'burden', 'butter', 'buyer', 'camera', 'campaign', 'capital', 'capture', 'carbon', 'careful', 'carrier', 'carve', 'casual', 'celebrate', 'center', 'ceremony', 'chance', 'change', 'channel', 'charge', 'charity', 'cheap', 'check', 'cheese', 'chef', 'choice', 'choose', 'church', 'climate', 'clinic', 'clothing', 'cluster', 'coastal', 'colony', 'combat', 'comfort', 'command', 'comment', 'compare', 'compete', 'complex', 'concept', 'concern', 'conduct', 'confirm', 'confront', 'congress', 'connect', 'consent', 'consult', 'consumer', 'contain', 'content', 'context', 'control', 'convert', 'cooking', 'corner', 'correct', 'costly', 'courage', 'cover', 'craft', 'crazy', 'create', 'credit', 'crime', 'crisis', 'critic', 'cross', 'crystal']

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for letter in chosen_word:
        display.append("_")

game = True

while game:
    guess = input("guess a letter: ").lower()   
    
    if guess in chosen_word:
        print("Right")
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess         
    else:
        print("Wrong")

    print (' '.join(display))

    if "_" in display:
        game = True
    else: 
        game = False

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed 
# all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.