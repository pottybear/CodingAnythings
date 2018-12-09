def listplus_1(A): 
    for i in range(len(A)):
        A[i] = A[i] + 1

    return A 

def pythonic(xs):
    ys = []
    for x in xs:
        ys.append(x + 1)
    return ys

makeA = input().split()
makeA = list(map(int, makeA))

print(listplus_1(makeA))
