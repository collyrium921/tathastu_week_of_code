sr = str(input("Enter string  "))
s = ""
for i in sr:
    if i not in s:
        s = s+i
print(" After removing duplicate characters striing is: ", s)
