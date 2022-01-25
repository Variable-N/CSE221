graph={}
c = 1
with open('input.txt') as inFile:
    while True:
        line = int(inFile.readline())
        print(line)
        #line = list(map(int, line))
        for i in range(line):
            edge = inFile.readline().split()
            print(edge)
            vertex = int(edge[0])
            weight = int(edge[1])
            for i in range(1,1+vertex):
                graph[i] = {}
            for j in range(1,1+weight):
                a = inFile.readline()
                a = a.split('\n')
                a = a[0].split()
                graph[int(a[0])][int(a[1])] = int(a[2])
            print(graph)
            c+=1
        if c > line:
            break