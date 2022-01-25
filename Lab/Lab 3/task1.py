# TASK - 1

graph = {}
file = open("input.txt",'r')
n = int(file.readline())

for i in range(n):
    a = file.readline().split('\n')
    a = a[0].split('\t')
    graph[a[0]] = a[1:]
file.close()
print("The created the graph is :")
print(graph)

