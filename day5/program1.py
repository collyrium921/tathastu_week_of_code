def replaceZero(num):
    result = num.replace('0', '5')
    return result
num = str(input("Enter number: "))
result = replaceZero(num)
print(result)
