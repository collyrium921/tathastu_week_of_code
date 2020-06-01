print("Enter 1st list: ")
l1 = list(map(int, input().split()))
print("Enter 2nd list: ")
l2 = list(map(int, input().split()))
sl1 = sorted(l1)
sl2 = sorted(l2)
result = sl1 + sl2
res = sorted(result)
print("Sorted resultant list is: ", res )
