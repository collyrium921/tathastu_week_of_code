def zeroOneknapsack(max_weight, L):
    if (max_weight == 0 or len(L) == 0):
        return 0
    if (len(L) == 1):
        if L[0][0] > max_weight:
            return 0 
        return L[0][1]  
    if L[0][0] > max_weight:
        return zeroOneknapsack((max_weight, L[1:]))
    return max(L[0][1] + zeroOneknapsack(max_weight - L[0][0], L[1:]), zeroOneknapsack(max_weight, L[1:]))
n =  int(input("Enter the number of items you want to enter: "))
L = []
for i in range(n):
    w = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    p = int(input("Enter the value for item number " + str(i + 1) + ": "))
    L.append((w,p))
max_weight = int(input("Enter the value of weight capacity: "))
print("The maximum value is ", zeroOneknapsack(max_weight, L))
