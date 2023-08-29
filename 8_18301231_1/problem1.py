f_input = open("input.txt","r")
f_output = open("output.txt","w")
f_record = open("record.txt","w")
even_count = 0
odd_count = 0
no_parity_count = 0
palindrome_count = 0
non_palindrome_count = 0
input_count = 0

for i in f_input:
    input_list = i.split()
    input_count += 1
    if '.' in input_list[0]:
        f_output.write(input_list[0]+" cannot have parity and ") 
        no_parity_count += 1
    else:
        if int(input_list[0]) % 2 == 0:
            f_output.write(input_list[0]+" has even parity and ") 
            even_count += 1
        else:
            f_output.write(input_list[0]+" has odd parity and ")    
            odd_count += 1

    words = "".join(reversed(input_list[1]))
    if input_list[1] == words:
        f_output.write(input_list[1]+" is a palindrome\n")
        palindrome_count += 1
    else:
        palindrome = False
        f_output.write(input_list[1]+" is not a palindrome\n")
        non_palindrome_count += 1

f_record.write("Percentage of odd parity: "+str((odd_count*100//input_count))+"%\n")
f_record.write("Percentage of even parity: "+str((even_count*100//input_count))+"%\n")
f_record.write("Percentage of no parity: "+str((no_parity_count*100//input_count))+"%\n")
f_record.write("Percentage of palindrome: "+str((palindrome_count*100//input_count))+"%\n")
f_record.write("Percentage of non-palindrome: "+str((non_palindrome_count*100//input_count))+"%")
    
