import task1
graph = task1.arr[1: ]
visited = [0]*len(graph)
queue = []
def BFS (visited, graph, node, endPoint):
    visited[int(node) - 1] = 1
    queue.append(node)
    
    while len(queue) != 0:
        m = queue.pop(0)
        f_output.write(m + " ")
        
        if m == endPoint:
            break

        for neighbour in graph[int(m) - 1].places:
            if visited[int(neighbour) - 1] == 0:
                visited[int(neighbour) - 1] = 1
                queue.append(neighbour)

f_output = open("output2.txt", "w")    
BFS(visited, graph, '1', '12')
