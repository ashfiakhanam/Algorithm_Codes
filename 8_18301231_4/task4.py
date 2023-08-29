import heapq

def Network(Graph, source):
    dist[source] = 0
    Q = []
    R = heapq    
    visited = [False]*(len(Graph)+1)
    prev[source] = 0    
    for ver_v in Graph:
        if ver_v != source:
            dist[ver_v] = -float("inf")
            prev[ver_v] = None
        R.heappush(Q, (dist[ver_v], ver_v))  
        R._heapify_max(Q) 
    while len(Q) != 0:
        x, u = R._heappop_max(Q)
        if visited[u]:
            continue
        visited[u] = True        
        for neigh_v in Graph[u]:
            if x != 0:
                alt = min(x,neigh_v[1])
            else:
                alt = neigh_v[1]
            if alt > dist[neigh_v[0]]:
                dist[neigh_v[0]] = alt
                prev[neigh_v[0]] = u
                R.heappush(Q,(dist[neigh_v[0]], neigh_v[0]))
                R._heapify_max(Q)
    print(dist[1:])
    return dist[1:]
                
def graphs(nums):
    dic = {}
    for data in nums:
        data = list(map(int, data.split()))
        try:
            dic[data[0]].append((data[1], data[2]))
        except:
            dic[data[0]] = [(data[1], data[2])]        
        try:
            dic[data[1]]
        except:
            dic[data[1]] = [] 
            
    return dic

f_input = open("input4.txt", "r")
data1 = f_input.read().split("\n")
f_output = open("output4.txt", "w")

a = 0
b = 1

while a < int(data1[0]):
    M = int(data1[b].split()[1])
        
    if M == 0:
        graph = {int(data1[b].split()[0]):[]}
    else:
        graph = graphs(data1[b + 1 : b + 1 + M])

    dist = [-float("inf")] * (len(graph) + 1)
    prev= [None]*(len(graph) + 1)

    for a in Network(graph,int(data1[b+1+M])):
        if a == -float("inf"):
            a = -1
        f_output.write(str(a) + " ")
    f_output.write("\n")    
   
    a += 1
    b = b + 2 + M  
                

                
        