



# these_are_lists = []
# these_are_dictionaries = {}
# these_are_sets = set()
# these_are_full_sets = {'nieves', 'boshka', 'python'}
# these_are_tuples = ()
# ingrediens = ["Spam", "egg", "sausage", "Spam", 'ham', 'salt', 'tomato', 'pepper', 'cheese']
#
# def first_and_last(sequence):
#     """returns the first and last elements of a sequence"""
#     return sequence[2], sequence[1], sequence[-2], sequence[5], sequence[-1]
#
# boshka, felix, nieves, kiska, charactrisa = first_and_last(ingrediens)
#
# print(boshka, felix, nieves, kiska,)



# Quiz Days and Hours
#
# def hours2days(time):
#  hours = time % 24
#  days = time // 24
#
#
#  return days, hours
#
#
#
#
# boshka = hours2days(10000)
# print(boshka)
#
# boshka = ['Nieves', ['tuna', 'crispy', 'glorious day'], 9, 4, ['Felix']]
#
# element = None
# counter = 0
# not_list = 0
# for i in boshka:
#     element = i
#     test = isinstance(element, list)
#     if test:
#         print('We found a list')
#         counter = counter + 1
#
#     else:
#         print('There is not list yet')
#         not_list = not_list + 1
# # print( 'There are: ' +  str(counter) + ' lists')
# print('There are: {} lists '.format(counter))
# print('There are: {} no lists' .format(not_list))

# symbol = '&'
# print(symbol * 10)
# for i in range(3):
#     print(symbol + ' ' * 8 + symbol)
# print(symbol * 10)


def shape(width, height, symbol = '@'):





    print(symbol * width)

    for i in range(height):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)

shape(9, 4, )
