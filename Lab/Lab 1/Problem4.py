def Multiply_matrix(A,B):
    n = len(A)
    C = []
    for i in range(n):
        t = [0]*n
        C.append(t)
        del t

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += int(A[i][k])*int(B[k][j])   #Added int for fix the file input string issue.
                
    return C

#Tester Code


f= open("input4.txt")
inputs = f.read().split('\n')
n = int(inputs[0])
A = []
B = []
for i in range(1,n+1):
    A.append(inputs[i].split(' '))
for i in range(n+2,2*n+2):
    B.append(inputs[i].split(' '))


output = Multiply_matrix(A,B)
string = ''
of = open("output4.txt",'w')
for i in range(len(output)):
    for j in range(len(output)):
        string += str(output[i][j])
        if j != len(output)-1:
            string += ' '
    string+= '\n'

of.write(string)