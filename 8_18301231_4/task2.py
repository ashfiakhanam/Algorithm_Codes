import queue
PQ = queue.PriorityQueue

def Dijkstra(Graph, source):
    if len(Graph) != 0:
        dist[source] = 0
        Q = PQ()
        visited = [False]*(len(Graph) + 1) 
        roads = []
        places = len(graph)       
        for ver_v in Graph:
            if ver_v != source:
                dist[ver_v] = float("inf")
                prev[ver_v] = None
            Q.put((dist[ver_v], ver_v))            
        while not Q.empty():
            u = Q.get()[1]
            if visited[u]:
                continue
            visited[u] = True            
            for neigh_v in Graph[u]:
                alt = dist[u] + neigh_v[1]
                if alt < dist[neigh_v[0]]:
                    dist[neigh_v[0]] = alt
                    prev[neigh_v[0]] = u
                    Q.put((dist[neigh_v[0]], neigh_v[0]))
        while places != 1:
            roads.append(places)
            places = int(prev[places])
        roads.append(places)
        roads.reverse()
    else:            
        return [source]    
    return roads


def graphs(nums):
    dic = {}
    for data in nums:
        data = list(map(int, data.split()))
        try:
            dic[data[0]].append(data[1], data[2])
        except:
            dic[data[0]] = [(data[1], data[2])]
        try:
            dic[data[1]].append((data[0], data[2]))
        except:
            dic[data[1]] = [(data[0], data[2])]            
    return dic
 
f_input = open("input2.txt", "r")
data1 = f_input.read().split("\n")
f_output = open("output2.txt", "w")

a = 0
b = 1

while a < int(data1[0]):
    M = int(data1[b].split()[1])
    graph = graphs(data1[b + 1 : b + 1 + M])

    dist = [0]*(len(graph) + 1)
    prev= [None]*(len(graph) + 1)
    
    for item in Dijkstra(graph, 1):
        f_output.write(str(item) + " ")        
    f_output.write("\n")
    a += 1
    b = b + 1 + M     
      
    
     
    

            