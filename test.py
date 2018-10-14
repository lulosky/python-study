


def boshka(amount, callback ):
    for i in range(0, 3000):
        print(i)
    finish = 'This program has finished running'
    callback(finish)



boshka(49, lambda finish: print(finish))
