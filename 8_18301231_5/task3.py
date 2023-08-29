from queue import LifoQueue

f_input = open("task3_input.txt","r")
f_output = open("task3_output.txt","w")

input_data = f_input.read().split("\n")
N = int(input_data[0])
T = list(map(int, input_data[1].split(" ")))
call = input_data[2]


T.sort()
stack = LifoQueue()
index = 0
jack_hours = 0
jill_hours = 0
sequence = ""

for c in call:
    if c == "J":
        stack.put(T[index])
        sequence += str(T[index])
        jack_hours += T[index]
        index += 1

    elif c == "j":
        v = stack.get()
        sequence += str(v)
        jill_hours += v


f_output.write(sequence+"\n")
f_output.write("Jack will work for " + str(jack_hours) + " hours\n")
f_output.write("Jill will work for " + str(jill_hours) + " hours")
