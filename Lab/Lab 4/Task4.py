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

def Network(graph,source):
    dist = [float('-inf')]*(len(graph)+1)
    dist[source] = float('inf')
    visited = [False]*(len(graph)+1)
    priorityQueue = []
    for v in graph:
        heappush(priorityQueue,[dist[v]*-1,v])
    while priorityQueue:
        u = heappop(priorityQueue)[1]
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                alt = min(dist[u],graph[u][v])
                if alt > dist[v]:
                    dist[v] = alt
                    heappush(priorityQueue,[dist[v]*-1,v])
    dist[source] = 0
    return dist



file = open("input4.txt",'r')
T = int(file.readline())
output = ""
for i in range(T):
    verEdge = file.readline().split()
    vertex = int(verEdge[0])
    edge = int(verEdge[1])
    graph = inputgraph(vertex,edge)
    source = int(file.readline())
    ans = Network(graph,source)
    
    for i in range(1,len(ans)):
        if ans[i] == float('-inf'):
            output += "-1 "
        else:
            output += str(ans[i]) + " "
    if i != T:
        output += "\n"

print(output)
file = open("output4.txt",'w')
file.write(output)
file.close()