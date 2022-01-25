from task1 import *

# TASK - 2

visited = []
queue = []

def bfs(visited, graph, node, end):
    output = "Places: "
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end = ' ')
        output += m + " "
        if m == end:
            return "connected"
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return "not connected"

print("Output of BFS is: ")
output = bfs(visited, graph, '1', '5')
print(output)
# file = open("output2.txt",'w')
# file.write(output)
# file.close()
