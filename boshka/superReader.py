with open("../boshka.txt", "a") as f:
    reader = f.write('Those lindos meows')


with open('../boshka.txt', 'r') as b:
    reader = b.read()
    print(reader)
