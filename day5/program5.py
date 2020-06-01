def sorting(L):
    o = []
    e = []
    for i in L:
        if i % 2 == 0:
            even.append(i)
        else :
            odd.append(i)
    result sorted(odd, reverse = True) + sorted(even)
    return result
print("Enter the numbers with spaces")
L = lsit(map(int, input().split()))
print("The list of numbers after sorting them according to given condition is", str(sorting(L))[1:-1])
