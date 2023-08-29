def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        elm = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = elm
    return arr    

f_input = open("input2.txt","r")
f_output = open("output2.txt","w")


input_data = f_input.read().split("\n")
line1 = input_data[0].split(" ")
m = int(line1[1])
arr = list(map(int, input_data[1].split(" ")))
sort = selectionSort(arr)

for i in range(0, m):
    f_output.write(str(sort[i])+ " ")
f_input.close()
f_output.close()

