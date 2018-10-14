
from threading import Timer

def boshka(amount, callback ):
    async def callToExternal():
         for i in range(0, 100):
             print(i)
    Timer(15, callToExternal)
    finish = 'boshka is mad want eat and meaows'
    callback(finish)

boshka(49, lambda finish: print(finish))
