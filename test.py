# Create a function, inside create a for loop that can
# count NUMBERS UP from the next variable

number_up = 0

# for the next list create a function that can count the total
# amount of elements inside the list



element = ['boshka', 'tuna', 9, True, 'crispies', 'hunt', 'lizard']

def total():
    amount_list = 0
    for i in element:
        amount_list = amount_list + 1
    print(amount_list)






total()


def counter():

    number_up = 0

    for i in range(8):
        number_up = number_up + 1
    print(number_up)

counter()
