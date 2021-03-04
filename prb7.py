#problema 7: al k-lea cel mai mare element dintr-un sir de numere
#complexitate O(nlogn)
def functie(x,k):
    x.sort(reverse= False)     
    return x[len(x)-k]
            
def testare():
    assert functie([7,4,6,3,9,1],2)==7
    assert functie([7,4,6,3,9,1],3)==6
    assert functie([7,4,6,3,9,1],4)==4
    assert functie([7,4,6,3,9,1],5)==3
    assert functie([7,4,6,3,9,1],6)==1

testare()