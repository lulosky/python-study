# with open('boshka.txt', 'a') as f:
#     boshka = f.write('My boshka beautiful and fun')
# with open('boshka.txt', 'r') as b:
#     boshka = b.read()
#     print(boshka)

# with open('camelot.txt', 'r') as t:
#     camelot0 = t.read(3)
#     camelot1 = t.read(8)
#     camelot2 = t.read()
#     print(camelot0)

def boshka(number, boshkaCallback):
    amountMeows = "{} times".format(number)
    boshkaCallback(amountMeows)


boshka(4, lambda a: print("Meow {}".format(a)))
