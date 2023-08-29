def LCS(X, Y, Z):
    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1
    
    c = (list(list(list(0 for i in range(o)) for i in range(n)) for i in range(m)))
    t = (list(list(list(None for i in range(o)) for i in range(n)) for i in range(m)))    
    max = 0


    for i in range(1, m):
        for j in range(1, n):
            for k in range(1, o):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                    t[i][j][k] = None
                else:
                    if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                        c[i][j][k] = 1 + c[i - 1][j - 1][k - 1]
                        t[i][j][k] = "diagonal"
                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            max = c[i - 1][j][k]

                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = "up-up-left"
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max
                                t[i][j][k] = "left-up-up"
                        else:
                            max = c[i][j - 1][k]

                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                                t[i][j][k] = "up-left-up"
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max
                                t[i][j][k] = "left-up-up"


    longest_length = c[m - 1][n - 1][o - 1]
           
    return longest_length 



f_input = open("task2_input.txt","r")
f_output = open("task2_output.txt","w")

input_data = f_input.read().split("\n")
X = input_data[0]
Y = input_data[1]
Z = input_data[2]

f_output.write(str(LCS(X, Y, Z)))



    
    
