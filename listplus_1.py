def listplus_1(A): 
    for i in range(len(A)):
        A[i] = A[i] + 1

    return A 

makeA = input().split()
makeA = list(map(int, makeA))

print(listplus_1(makeA))
