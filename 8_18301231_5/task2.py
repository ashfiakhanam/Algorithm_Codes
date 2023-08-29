f_input = open("task2_input.txt","r")
f_output = open("task2_output.txt","w")

input_data = f_input.read().split("\n")
N = int(input_data[0].split(" ")[0])
M = int(input_data[0].split(" ")[1])
arr = []
for i in range(1, N + 1):
    arr.append(list(map(int, input_data[i].split(" "))))


arr = sorted(arr, key = lambda l:l[1])
p = 0
count = 0

while p <= M-1:
    selected = []
    left = []
    selected.append(arr[0])
    del(arr[0])
    count += 1

    for i in range(len(arr)):
        a = arr[0][0]
        b = selected[-1][1]
        if a >= b:
            count += 1
            selected.append(arr[0])
        else:
            left.append(arr[0])
        del(arr[0])
    arr = left
    p+=1


f_output.write(str(count))





