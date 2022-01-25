from heapq import *

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def inputgraph(vertex,edge):
    graph = {}
    for i in range(1,vertex+1):
        graph[i] = {}
    for i in range(1,1+edge):
        a = file.readline().split('\n')
        a = a[0].split(' ')
        graph[int(a[0])] [int(a[1])] = int(a[2])
    return graph

def Dijkstra(graph,source):
    print(graph)
    dist = [float('inf')]*(len(graph)+1)
    dist[source] = 0
    visited = [False]*(len(graph)+1)
    parentNode = [-1]*(len(graph)+1)
    priorityQueue = []
    for v in graph:
        heappush(priorityQueue,[dist[v],v])
    while priorityQueue:
        u = heappop(priorityQueue)[1]
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(priorityQueue,[dist[v],v])
                    parentNode[v] = u

    node = len(graph)
    string = ""
    while node != source:
        string = " " + str(node) + string
        node = parentNode[node]
    string = str(source) + string
    print(parentNode)
    return string



file = open("input1.txt",'r')
T = int(file.readline())
output = ""
for i in range(T):
    verEdge = file.readline().split()
    vertex = int(verEdge[0])
    edge = int(verEdge[1])
    graph = inputgraph(vertex,edge)
    output += Dijkstra(graph,1)
    if i != T-1:
        output += "\n"
print(output)
file = open("output2.txt",'w')
file.write(output)
file.close()