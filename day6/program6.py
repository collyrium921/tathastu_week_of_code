n = input("Enter number: ")
l = []
for i in n:
    l.append(i)
s = sorted(l)
if l == s:
    print("Number is sorted")
else:
    print("Number is not sorted")
