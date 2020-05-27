n = int(input("enter size of dictionary: "))
d = dict()
for i in range(n):
    key = input("enter "+ "key "+str(i+1))
    value = int(input("enter " + "value "+str(i+1)))
    d[key] = value
res = dict()
for key,value in d.items():
    if value not in res.values():
        res[key] = value
print("Dictonary after removing duplicate values: ", res)
