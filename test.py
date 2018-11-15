def create_cast_list(filename):
    cast_list = []
    with open(filename, "r") as t:
        for i in t:
            list = i.split(',')
            cast_list.append(list[0])
    return(cast_list)
