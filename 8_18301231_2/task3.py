def insertionSort(sort, arr):
    for i in range(len(arr) -1, 0, -1):
        elm = arr[i]
        num = sort[i]
        
        while i != 0 and arr[i - 1] < elm:
            sort[i] = sort[i -1]
            i = i - 1
        
        sort[i] = num
    return sort

f_input = open("input3.txt","r")
f_output = open("output3.txt","w")

input_data = f_input.read().split("\n")
arr1 = list(map(int, input_data[1].split(" ")))
arr2 = list(map(int, input_data[2].split(" ")))
sort = insertionSort(arr1, arr2)

for i in sort:
    f_output.write(str(i)+ " ")
f_input.close()
f_output.close()