N = int(input("Enter number: "))
if N%2==0:
    print("Number is Even")
else:
    print("Number is Odd")
n = str(N)
rev = n[::-1]
if n == rev:
    print("Number is Palindrome")
if N<=3:
    print("Number is Prime")
else:
    flag= True
    for i in range(2, N):
        if N%i == 0:
            falg = False
            break
    if flag== True:
        print("Number is Prime")
sum = 0
temp = N
while temp>0:
    digit = temp%10
    sum = sum+(digit**3)
    temp = temp//10
if sum==N:
    print("Number is Armstrong number")
