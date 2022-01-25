zoneCenter = {'Y': "Yasnaya",
              'P': "Pochinki",
              'S': "School",
              'R': "Rozhok",
              'F': "Farm",
              'M': "Mylta",
              'H': "Shelter",
              'I': "Prison",
              }

def LCS (X,Y):
    global zoneCenter
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
    zoneseq = zoneCenter[X[i]]
    while maximum != 0:
        if arr2d[i-1][j-1] +1 == arr2d[i][j] and arr2d[i-1][j] < arr2d[i][j]:
            zoneseq = zoneCenter[X[i-1]] + " " +zoneseq
            maximum -= 1
            i -= 1
            j -= 1
        else:
            i-=1

    print(zoneseq)
    print("Correctness of prediction: {}%".format(100*arr2d[-1][-1]/(m-1)))
    return zoneseq + "\n" + "Correctness of prediction: {}%".format(100*arr2d[-1][-1]/(m-1))

        

file = open("task1_input.txt",'r')
N = int(file.readline())
realZones = file.readline()
realZones = realZones[0:-1]
predictedZones = file.readline()
output = LCS(realZones,predictedZones)
file = open("task1_output.txt",'w')
file.write(output)
file.close()