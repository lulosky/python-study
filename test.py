







# Quiz: Mutable Default Arguments:


def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list






print(todo_list('To feed Boshka', ['To change water for Boshka']))
