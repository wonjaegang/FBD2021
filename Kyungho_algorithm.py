import random

def select_counting(previous_num):
        count=0
        mynum=previous_num
        num_count=random.randrange(1,4)
        good=[8,15,22,28,29]
        good2=[7,14,21,27,28]
        bad=[10,18,25,30]
        for i in range(num_count):
            count+=1
            mynum=mynum+1
            if mynum in good2:
                if count == 1:
                        return 3
            if mynum in good:
                if count==1:
                        return 2
                elif count==2:
                        return 3
              
            if mynum in bad:
                if count==1:
                        return 1
                elif count==2:
                    return 2
                else:
                    return 3          
        return num_count
                
