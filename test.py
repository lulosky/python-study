def felixon(word):
    response = '{} I see and I like Meow sometimes'.format(word)
    return response

def FoodOfCat(word):
    catFood = '{} eat tuna and bones'.format(word)
    return catFood


def boshka(word, callback):
    groupWords = "{} I'm Boshka and I like to".format(word)
    amountOfLetters = str(len(groupWords))
    response = felixon(groupWords)
    catFood = FoodOfCat(groupWords)
    callback(groupWords, amountOfLetters, response, catFood)



boshka('hello', lambda a, b, c, d: print('{} Meow'.format(a), '**The amount of letters is {}**'.format(b), 'Response from Felixon: {}'.format(c), 'Answer from BoshkaNieves {}'.format(d)))
