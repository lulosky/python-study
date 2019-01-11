from random import choice, random


def generate_password():
    with open('words.txt', 'r') as f:
        words = f.read()
        listOfWords = words.split()
        # randomWord = choice(listOfWords)
        lengthOfList = len(listOfWords)
        word1 = None
        word2 = None
        word3 = None
           
        for i in range(3):       
            
            randomNumber = random()
            randomIndex = int(randomNumber * lengthOfList)
            
            if i == 0:
                word1 = listOfWords[randomIndex]
            elif i == 1:
                word2 = listOfWords[randomIndex] 
            elif i == 2:
                word3 = listOfWords[randomIndex] 

        password = '{}{}{}' .format(word1, word2, word3)    
        return password.lower()
generate_password()
