#problema 3 produsul scalar a doi vectori rari
#complexitate O(n)
#input: a,b vectori unidimensionali
def functie(a,b):
    s=0
    i=0
    if len(a)==len(b) :
        while i < len(a):
            if(a[i]!=0 and b[i]!=0):
                s=s+a[i]*b[i]
            i=i+1
        return s
    
print(functie([1,0,2,0,3],[1,2,0,3,1]))
print(functie([3,2,0,0,1],[2,0,3,0,1]))

def testare():
    assert functie([1,0,2,0,3],[1,2,0,3,1])==4
    assert functie([3,2,0,0,1],[2,0,3,0,1])==7
    assert functie([6,0,0,1],[2,1,0,0])==12
    assert functie([7,0,0,0],[1,0,0,0])==7
    assert functie([1,2,0,0],[0,0,1,1])==0
testare()
