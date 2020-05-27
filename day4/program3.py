n = int(input("enter size of dictionary: "))
d = dict()
for i in range(n):
    key = input("enter "+ "key "+str(i+1))
    value = int(input("enter " + "value "+str(i+1)))
    d[key] = value
print("2nd largest value is", list(sorted(d.values()))[-2])
    
