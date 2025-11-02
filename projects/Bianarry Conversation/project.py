a = int(input("Enter a decimal number: "))
b = ""
while a > 0:
    remainder = a % 2
    b = str(remainder) + b
    a = a // 2
for i in range(len(b)):
    for j in range(1):
        print(b[i], end="")

print()