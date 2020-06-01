flag = 0
l = list(map(int, input().split()))
for i in range(0, len(l) - 2):
    for j in range(i+1, len(l) - 1):
        for k in range(j+1, len(l)):
            if (l[i] + l[j] + l[k] < 2) and (l[i] + l[j] + l[k] > 1):
                flag = 1
                break
        if flag==1:
            break
    if flag==1:
        break

if flag == 1:
    print("Possible triplets are: ", arr[i], arr[j], arr[k])
else:
    print("Sorry, Not possible")
