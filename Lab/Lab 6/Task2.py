
def LCS (X,Y):
    m = len(X)+1
    n = len(Y)+1
    arr2d = []
    for i in range(m):
        c = [0]*n
        arr2d.append(c)
        del(c)
    for i in range(1,m):
        for j in range(1,n):
            if X[i-1] == Y[j-1]:
                arr2d[i][j] = 1 + arr2d[i-1][j-1]
            else:
                arr2d[i][j] = max(arr2d[i-1][j],arr2d[i][j-1])

    maximum = arr2d[-1][-1]-1
    i = -1
    j = -1
    seq = X[i]
    while maximum != 0:
        if arr2d[i-1][j-1] +1 == arr2d[i][j] and arr2d[i-1][j] < arr2d[i][j]:
            seq = X[i-1]+seq
            maximum -= 1
            i -= 1
            j -= 1
        else:
            i-=1
    print(seq)
    return seq

def threeLCS(X,Y,Z):
    A = LCS(X,Y)
    B = LCS(A,Z)
    return str(len(B))

file = open("task2_input.txt",'r')
str1 = file.readline()
str1 = str1[0:-1]
str2 = file.readline()
str2 = str2[0:-1]
str3 = file.readline()
output = threeLCS(str1,str2,str3)
file = open("task2_output.txt",'w')
file.write(output)
file.close()