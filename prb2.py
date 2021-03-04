#problema 2 distanta euclidiana
#complexitate theta(1)

import math
def functie(xM,xN,yM,yN):
    a=math.pow(xM-xN,2)+math.pow(yM-yN,2)
    return math.sqrt(a)

print(functie(1,4,5,1))
print(functie(4,0,3,0))
print(functie(5,0,0,0))


def testare():
    assert functie(1,4,5,1)==5.0
    assert functie(4,0,3,0)==5.0
    assert functie(5,0,0,0)==5.0
    
 
testare()