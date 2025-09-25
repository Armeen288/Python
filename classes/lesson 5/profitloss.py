actualcost = float(input("Enter the actual product price:"))
saleamount = float(input("Enter the sale product price: "))
if (saleamount > actualcost):
    amount =  saleamount - actualcost
    print("Total profit = {0}".format(amount))
else:
    print("No profit")
