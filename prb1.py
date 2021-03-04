#complexitate O(nlogn)
#date de intrare: l= string
def function(l):
    rez=l.split(" ")
    rez.sort(reverse=True)
    return rez[0]
print(function("Ana are mere rosii si galbene"))
print(function("a b c z d e f g"))
print(function("ghioceii au aparut"))

def testare():
    assert function("Ana are mere rosii si galbene")=="si"
    assert function("a b c z d e f g")=="z"
    assert function("ghioceii au aparut")=="ghioceii"
    assert function("zambile si trandafiri i-am cumparat mamei")=="zambile"
    assert function("carina este studenta in anul doi")=="studenta"
testare()

