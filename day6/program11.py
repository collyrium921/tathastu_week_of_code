print("Enter list elements: ")
l = list(map(int, input().split()))
res = sorted(l)
product = res[-1]*res[-2]*res[-3]
print("Maximum product of 3 elements is: ", product)
