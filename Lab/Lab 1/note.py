def Multiply_matrix(A,B):
    C = []
    for i in range(len(A)):
        n = []
        for j in range(len(B)):
            n.append(0)
        C.append(n)

    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                C[i][j] += A[i][k]*B[k][j]

    return C

file = open("input4.txt")
inputs = file.read().split('\n')
n = int(inputs[0])
A = []
B = []

for i in range(1,2*n+2):
    if i <= n:    A.append(inputs[i].split(' '))
    elif i == n+1:  pass
    else: B.append(inputs[i].split(' '))

for i in range(n):
    for j in range(len(A)):
        A[i][j] = int(A[i][j])
        B[i][j] = int(B[i][j])
file.close()

file = open("output4.txt",'w')
file.close()
file = open("output4.txt",'a')

result = Multiply_matrix(A,B)
for i in range(len(result)):
    for j in range(len(result)):
        file.write(str(result[i][j]))
        file.write(" ")
    file.write("\n")
    
file.close()