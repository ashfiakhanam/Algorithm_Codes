def mergeSort(arr):
    if len(arr) != 1:
        mid = len(arr) // 2
        
        L = mergeSort(arr[:mid])
        R = mergeSort(arr[mid:])

        arr = []

        i = 0 
        j = 0  

        while True:
            if i >= len(L):
                for x in R[j:]:
                    arr.append(x)
                break
            if j >= len(R): 
                for x in L[i:]:
                    arr.append(x)
                break
            if L[i] < R[j]:
                arr.append(L[i])
                i += 1
            else:
                arr.append(R[j])
                j += 1
    return arr


f_input = open("input4.txt","r")
f_output = open("output4.txt","w")

input_data = f_input.read().split("\n")
arr = list(map(int, input_data[1].split(" ")))
sort = mergeSort(arr)

for i in sort:
    f_output.write(str(i)+ " ")
f_input.close()
f_output.close()
