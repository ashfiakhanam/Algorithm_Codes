def bubbleSort(arr):    
    for i in range(len(arr) - 1):
        change = False #This variable will check if two numbers will change their place or not
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                elm = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = elm
                change = True
        if not change: #if two numbers won't change their places the whole loop will break, resulting a best case scenerio.
            break
            
    return arr

f_input = open("input1.txt","r")
f_output = open("output1.txt","w")

input_data = f_input.read().split("\n")
arr = list(map(int, input_data[1].split(" ")))
sort = bubbleSort(arr)

for i in sort:
    f_output.write(str(i)+ " ")
f_input.close()
f_output.close()

