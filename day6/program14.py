N = int(input("Enter number of rows: "))
print("Enter values row wise: ")
a=[]
for i in range(N):
    m=[]
    for j in range(N):
        m.append(int(input()))
    a.append(m)

for x in range(0, int(N / 2)):
    for y in range(x, N - x - 1):
        temp = mat[x][y]    # store current cell in temp variable
        mat[x][y] = mat[y][N - 1 - x]  # move values from right to top
        mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]   # move values from bottom to right
        mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]   # move values from left to bottom
        mat[N - 1 - y][x] = temp    # assign temp to left
for i in range(0, N):
    for j in range(0, N):
        print(mat[i][j], end=' ')
    print("")
