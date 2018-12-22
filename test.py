upandDown = {
    'boolean': ''
}

def dataBaseRead():
    with open('boshka.txt', 'r') as f:
        boshka = f.read()

        if boshka == 'False' or '':
            upandDown['boolean'] = False
        elif boshka == 'True':
            upandDown['boolean'] = True


def dataBaseWrite():
    with open('boshka.txt', 'w') as v:
        boshka = v.write(str(upandDown['boolean']))



def change():

    dataBaseRead()


    upandDown['boolean'] =  not upandDown['boolean']

    dataBaseWrite()

    print(upandDown['boolean'])

change()
