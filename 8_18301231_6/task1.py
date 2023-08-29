def LCS(X, Y):
    m = len(X) + 1
    n = len(Y) + 1
    
    c = (list(list(0 for i in range(n)) for i in range(m)))
    t = (list(list(None for i in range(n)) for i in range(m)))


    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = 1 + c[i - 1][j - 1]
                t[i][j] = "diagonal"
            elif c[i - 1][j] <= c[i][j - 1]:
                c[i][j] = c[i][j - 1]
                t[i][j] = "left"
                
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                t[i][j] = "up"
                

    L_C_S = ""

    i = m - 1
    j = n - 1    
    while i > 0 and j > 0:
        if t[i][j] == "up":
            i -= 1
        elif t[i][j] == "left":
            j -= 1
        elif t[i][j] == "diagonal":
            L_C_S = X[i-1] + L_C_S
            i -= 1
            j -= 1 
    for i in c:
        print(i)    
    return L_C_S 



f_input = open("task1_input.txt","r")
f_output = open("task1_output.txt","w")

input_data = f_input.read().split("\n")
N = int(input_data[0])
X = "TTAATCGT" #AATCGT
Y = "TTTTCGAA"

LCZS = LCS(X, Y)
correctness = (len(LCZS)*100)//N
print(LCZS)
print(len(LCZS))

for i in LCZS:
    if i == "Y":
        f_output.write("Yasnaya ")
    elif i == "P":
        f_output.write("Pochinki ")
    elif i == "S":
        f_output.write("School ")
    elif i == "R":
        f_output.write("Rozhok ")
    elif i == "F":
        f_output.write("Farm ")
    elif i == "M":
        f_output.write("Mylta ")
    elif i == "H":
        f_output.write("Shelter ")
    elif i == "I":
        f_output.write("Prison ")

f_output.write("\n"+"Correctness of prediction: "+str(correctness)+"%")
    
    
