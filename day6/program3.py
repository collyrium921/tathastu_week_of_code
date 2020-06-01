n = int(input("Enter Size: "))
l = []
print("Enter numbers: ")
for i in range(n):
    l.append(int(input()))
sor = sorted(l)
for i in range(1,len(sor)+1):
    if i not in sor:
        break
    else:
        continue
print("Smallest number missing is: ", i)
    
