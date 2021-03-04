#cuvintele care apar o singura data intr-un text
#complexitate O(n)
import collections
def function(l):
    arr=l.split()
    freq= collections.Counter(arr)
    rez=[]
    
    for (key,value) in freq.items():
        if value == 1:
            rez.append(key)
    return rez

for i in function("ana are mere si ana are pere"):
    print(i)
for i in function("carina carina a a fost fost la la  NASA NASA"):
    print(i)
for i in function("mama mea si mama Elenei vorbesc mult la telefon"):
    print(i)

def testare():
    assert len(function("ana are mere si ana are pere"))==3
    assert len(function("carina carina a a fost fost la la  NASA NASA"))==0
    assert len(function("mama mea si mama Elenei vorbesc mult la telefon"))==7
    assert len(function("carina"))==1
    assert len(function("fetele vorbesc mult mult"))==2
testare()
        