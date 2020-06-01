print("Enter list elements: ")
l = list(map(int,input().split()))

for i in range(0, len(l)):
        flag = True
        for j in range(0, i):
            if (l[j] >= l[i]):
                flag = False
                break
        for j in range(i + 1, len(l)):
            if (l[j] <= l[i]):
                flag = False
                break
if (flag == True):
    print("required element is, ", l[i])
