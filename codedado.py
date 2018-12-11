import random
 
LANCI=6
 
def dado():
    return random.randrange(1,7)
 
for i in range(LANCI):
    esito=dado()
    print(esito,end=' ')