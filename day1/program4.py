cp = int(input("Enter cost price of product: "))
sp = int(input("Enter selling price of product: "))
profit_per = ((sp-cp)/cp)*100
# if profit is incresed by 5%
profit = profit_per + 5
sp = sp + (cp+(profit*cp))/100
print("Profit percentage is: ", profit_per)
print("Selling price should be: ", sp)
