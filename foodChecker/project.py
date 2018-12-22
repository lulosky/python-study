# DRY PRINCIPLE = DO NOT REPEAT YOURSELF

# boshka = {'tuna': 20, 'crispies': 100, 'eat': True }
def reset(theDayList):
    for i in theDayList:
        i['tuna'] = 0

        i['crispies'] = 0

        i['eat'] = False

    return theDayList

def setEatTimes(tuna, crispies, eat, day, foodTimes):

    boshka = reset(foodTimes)

    fixingIndex = day - 1

    dayOfWeek = boshka[fixingIndex]

    dayOfWeek['tuna'] = tuna
    dayOfWeek['crispies'] = crispies
    dayOfWeek['eat'] = eat

    # boshka.append(dayOfWeek)
    boshka[fixingIndex] = dayOfWeek
    print(boshka)




    # print(dayOfWeek)

def check(tuna, crispies, eat, day):
    # this list represent each day of the week
    boshka = [
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True },
    {'tuna': 20, 'crispies': 100, 'eat': True }
    ]
    setEatTimes(tuna, crispies, eat, day, boshka)
    # dic = boshka[2]
    # dic['eat'] = False


#     for i in boshka:
#         if i == 'eat':
#             boshka[i] = False
#         elif i == 'tuna':
#             boshka[i] = 0
#         elif i == 'crispies':
#             boshka[i] = 0

# boshka['tuna'] = 0
# boshka['crispies'] = 0
# boshka['eat'] = False

check(900, 400, True, 7)
