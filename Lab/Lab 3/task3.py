from task1 import *

visited = []
def dfs_visit(graph,s):
    for v in graph[s]:
        if v not in visited:
            visited.append(v)
            dfs_visit(graph,v)

def dfs(graph,end):
    for v in [*graph]:
        if v not in visited:
            visited.append(v)
            dfs_visit(graph,v)

dfs(graph,'12')
print("Output of DFS is: ")

output = "Places: "

for i in visited:
    print(i,end = ' ')
    output += i + ' '
    if i == '12':
        break

file = open("output3.txt",'w')
file.write(output)
file.close()