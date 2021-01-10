import random

def select_counting(previous_num):
        previous_num += 1
        mod = previous_num % 7
        if mod == 0:
            if previous_num == 28:
                return random.randrange(2, 4)
            else:
                return 3
        elif mod == 1:
            if previous_num == 29:
                return random.randrange(1, 3)
            else:
                return 2
        elif mod == 2 or mod == 3:
            return 1
        else:
            return 3
