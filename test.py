# Create a function with 1 argument that determine if a number is able to devide by 3 and 5
# a number able to devide by 3 and 5 have to return Boshka Nieves
# a number only able to devide by 3 return Boshka
# a number only able to devide by 5 return Nieves
# print the result to the terminal


def homework(argument):



    if argument % 3 == 0 and argument % 5 == 0:
        return "Boshka Nieves"
    elif argument % 3 == 0:
        return "Boshka"

    elif argument % 5 == 0:
        return "Nieves"


print(homework(5))
