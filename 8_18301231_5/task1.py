f_input = open("task1_input.txt","r")
f_output = open("task1_output.txt","w")

input_data = f_input.read().split("\n")
N = int(input_data[0])
arr = []
for i in range(1, N + 1):
    arr.append(list(map(int, input_data[i].split(" "))))


arr = sorted(arr, key = lambda l:l[1])
selected = []
selected.append(arr[0])
f = arr[0][1]
del(arr[0])
count = 1


for i in range(len(arr)):
    a = arr[0][0]
    b = selected[-1][1]
    if a >= b:
        count += 1
        f = arr[0][1]
        selected.append(arr[0])
    del(arr[0])

f_output.write(str(count) + "\n")
for i in selected:
    f_output.write(str(i[0]) +" " + str(i[1]) + "\n")
f_input.close()
f_output.close()





