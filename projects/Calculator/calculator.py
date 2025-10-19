p = int(input("Enter the number you want to calculate : "))
n = int(input("Enter the power : "))
result = 1
for i in range(n):
    result *= p 

print("{p} to the power of {n} is ", result)