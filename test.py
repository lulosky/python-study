


boshka = open('boshka.txt')

boshkaFormated = boshka.read()

text = open('boshka.txt', 'w')

for i in range(100):
    text.write('{} and Boshka is a lovely kiska'.format(boshkaFormated))

boshka.close()
text.close()
