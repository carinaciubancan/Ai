#problema 5
#complexiatate O(nlogn)
import math
def functie(x):
    x.sort(reverse= False)
    ok=0
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            ok=1
            return x[i]
    if ok==0:
        return 0

def testare():
    assert functie([1,2,2,3])==2
    assert functie([1,2,3,4])==0
testare()