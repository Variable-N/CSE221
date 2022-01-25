

def RMQ (A,l,r):
    minimum = float("inf")
    for i in range(l,r+1):
        if A[i] < minimum:
            minimum = A[i]

    return minimum

array = [4,1,7,3,5]
print(RMQ(array,2,4))
