import random

def select_counting(previous_num):
    mod = (previous_num + 1) % 7
    if mod == 2 or mod == 3:
        return 1
    elif mod == 1:
        if previous_num == 28:
            return random.randrange(1, 3)
        else:
            return 2
    else:
        if previous_num == 27:
            return random.randrange(2, 4)
        else:
            return 3