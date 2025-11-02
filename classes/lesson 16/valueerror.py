try:
    number = int(input("Enter number: "))
    print=("Your number is", number)

except ValueError as ex:
    print("Exception:" , ex)