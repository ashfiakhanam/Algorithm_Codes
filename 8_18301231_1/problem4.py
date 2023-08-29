f_input = open("D:\Studies\Ashfia Khanam\CSE221\Lab\Lab01\input4.txt", "r")
f_output = open("D:\Studies\Ashfia Khanam\CSE221\Lab\Lab01\output4.txt","w")
file = f_input.read().split("\n")
N = int(file[0])

C = []
for i in range(N):
    C.append([0]*N)

start_A = 1
end_A = start_A+N
A = []
for i in range(start_A, end_A):
    nums = file[i].strip().split(' ')
    sub_list = list(map(int, nums))
    A.append(sub_list)

start_B = end_A+1
end_B = start_B+N   
B = []
for i in range(start_B, end_B):
    nums = file[i].strip().split(' ')
    sub_list = list(map(int, nums))
    B.append(sub_list)

for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i][j]+=A[i][k]*B[k][j]   

ans =""
for i in C:
    for j in i:
        ans = ans + str(j) + " "
    ans += "\n"

f_output.write(ans)
  
