def stolen(L):
    if len(L) == 2:
        return max(L)
    if len(L) == 1:
        return L[0]
    if len(L) == 3:
        return max(L[1], L[0] + stolen(L[2:]))
    return max(L[1] + stolen(L[3:]), L[0] + stolen(L[2:]))
n = int(input("Enter the number of Houses: "))
L = []
print("Enter the values of house numbers")

for i in range(n):
    a =int(input())
    L.append(a)
        
result = stolen(L)
print(result)
             
