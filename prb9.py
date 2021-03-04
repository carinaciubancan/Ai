#complexitate: O(n^2)
def function(matrix,a,b,c,d):
    s=0
    for i in range(a,c+1):
        for j in range(b,d+1):
            s=s+matrix[i][j]
    return s
def suma(matrix,perechi):
    sume=[]
    for i in perechi:
        sume.append(function(matrix,i[0][0],i[0][1],i[1][0],i[1][1]))
    return sume
matrix=[[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]]
perechi=[((1,1),(3,3)),((2,2),(4,4))]
for i in suma(matrix,perechi):
    print (i)
def testare():
    matrix=[[0,2,5,4,1],[4,8,2,3,7],[6,3,4,6,2],[7,3,1,8,3],[1,5,7,9,4]]
    perechi=[((1,1),(3,3)),((2,2),(4,4))]
    assert suma(matrix,perechi)[0]==38
    assert suma(matrix,perechi)[1]==44
testare()