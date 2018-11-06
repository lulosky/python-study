# with open('boshka.txt', 'a') as f:
#     boshka = f.write('My boshka beautiful and fun')
# with open('boshka.txt', 'r') as b:
#     boshka = b.read()
#     print(boshka)

with open('camelot.txt', 'r') as t:
    camelot0 = t.read(2)
    camelot1 = t.read(8)
    camelot2 = t.read()
    print(camelot0, camelot1, camelot2)
