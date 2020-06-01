s = input("Enter string of zeroes and ones: ")
a =""
for i in range(len(s)):
    if s[i] == '0':
        a=a+'0'
for i in range(len(a), len(s)):
    a=a+'1'
print("String in ascending order is: ", a)
