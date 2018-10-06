# boshka = {'food': 'tuna', 'games': ['ball', 'rope', 'mouse'], 'communication': 'fubla'}
#
# def boshkaDeals():
#     boshka["food"] = "ham"
#     print(boshka)
#
# boshkaDeals()

boshka_list = ['ball', 'rope', 'mouse']
new_list = ["lagartija"]

def calling_http(response):
    count = response + 1
    number(count)

def number(count):
    my_index = count + len(boshka_list)
    return my_index

boshka_list.append(new_list[number()])

print(boshka_list)
