class Node:
    c = 1
    def __init__(self):
        self.region = str(Node.c)
        self.places = []
        Node.c += 1
        
arr = [None]

f_input = open("input.txt", "r")
data1 = int(f_input.readline())
data2 = int(f_input.readline())

for i in range(data1):
    arr.append(Node())

for i in range(data2):
    ending = f_input.readline().split()
    arr[int(ending[0])].places.append(ending[1])
