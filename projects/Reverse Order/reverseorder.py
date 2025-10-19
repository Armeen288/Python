n = int(input("Enter a number: "))
a = 0
t = n
while t>0:
    t = t // 10
    a += 1

print("The total number of digits in the number is: ", a)