def replaceMaximum(num_list):
    for i in range(len(num_list)-1):
        maximum = max(num_list[i+1:])
        num_list[i] = maximum
    return num_list
  
print("Enter Number with spaces")
num_list = list(map(int, input().split()))
result = replaceMaximum(num_list)
print("After replacing integers with greatest integers: ", result)
