#problema 6
#complexitate O(nlogn)
import math

def functie(x):
    x.sort(reverse= False)
    nrAparitiiMax=0
    for i in range(len(x)-1):
        while x[i]==x[i+1]:
            nrAparitiiMax=nrAparitiiMax+1
            if nrAparitiiMax > len(x)/2:
                return x[i]
        nrAparitiiMax=0
        
print(functie([2,8,7,2,2,5,2,3,1,2,2]))
def testare():
    assert functie([2,8,7,2,2,5,2,3,1,2,2])==2
testare()