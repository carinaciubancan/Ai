#input: x = int, base = int
#complexitate: O(log n)
def converter(x, base) : 
    s = "" 
    if (x == 0) : 
        return "0"
    while (x != 0) : 
        s = str(x % base) + s  
        x = int(x / base) 
    return s
#input: n= int
#complexity: O(n)
def generator(n):
    arr=[]
    i=0
    for i in range(1,n+1):
        arr.append(converter(i,2))
    return arr

for i in generator(4):
    print(i)

def testare():
    assert generator(4)[0]=="1"
    assert generator(4)[1]=="10"
    assert generator(4)[2]=="11"
    assert generator(4)[3]=="100"
testare()
