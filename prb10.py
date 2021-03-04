#complexitate: O(n^2)
def function(matrix):
    sir=[]
    for i in matrix:
        sir.append(sum(i))
    return sir
#complexitate: O(n^2)
def maxIndex(matrix):
    maxind=0
    maxval=0
    sir= function(matrix)
    print(sir)
    for i in range(0,len(sir)):
        if(sir[i]>maxval):
            maxval=sir[i]
            maxind=i
    return(maxind+1)
matrix=[[0,0,0,1,1],[0,1,1,1,1],[0,0,1,1,1]]
def testare():
    assert maxIndex(matrix)==2
testare()