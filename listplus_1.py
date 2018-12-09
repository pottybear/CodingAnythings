def listplus_1(A): 
    for _ in range(len(A)):
        A[_] = A[_] + 1

    return A 

makeA = input().split()
makeA = list(map(int, makeA))

print(listplus_1(makeA))
