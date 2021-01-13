import random

def select_counting(previous_num):
        count=0
        mynum=previous_num
        num_count=random.randrange(0,3)
        for i in range(1, num_count):
            count+=1
            mynum=mynum+1
            if mynum == 28 or mynum == 29 or mynum == 22 or mynum == 15 or mynum == 8:
                if count!=3:
                    return num_count+1
            if mynum == 10 or mynum == 18 or mynum == 25 or mynum == 30:
                return 1
            if mynum == 30:
                return 1

        return num_count+1
                
