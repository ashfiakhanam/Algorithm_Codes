import task1
graph = task1.arr[1: ]
visited = [0]*len(graph)
printed = [] 

def DFS_VISIT(graph, node):
	visited[int(node) - 1] = 1
	printed.append(node)
	for city in graph[int(node) - 1].places:
		if visited[int(city) - 1] == 0:
			DFS_VISIT(graph, city)

def DFS(graph, endPoint):
    for city in graph:
        if visited[int(city.region) - 1]==0:
            DFS_VISIT(graph, city.region)
			
    for i in printed:
        f_output.write(i + " ")
        if i == endPoint:
            break
            
f_output = open("output3.txt", "w") 
DFS(graph, '12')

