import random

def select_counting(previous_num):
        previous_num += 1
        count=0;
        num_count=random.randragne(0,3)
        for i in num_count:
            count+=1
            if previous_num == 28 or previous_num == 29 or previous_num == 22 or previous_num == 15 or previous_num == 8:
                if count!=3:
                    return num_count+1
            if previous_num == 10 or previous_num == 18 or previous_num == 25 or previous_num == 30:
                return 1
            if previous_num == 30:
                return 1

        return num_count
                
