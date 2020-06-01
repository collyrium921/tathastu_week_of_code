n = (input("Enter number: "))
a = []
for i in n:
    a.append(i)
s = sorted(a[2:])
l = []
l.append(a[0])
l.append(s[0])
l.append(a[1])
for i in range(1, len(s)):
    l.append(s[i])
st = ""
st = st.join(l)
print("Next greater number possible is: ", st)
