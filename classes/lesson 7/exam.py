medicalcause = input("Did you have medical cuse Y or N:")
atten = int(input("Enter the attendance of the student: "))
if medicalcause == 'Y':
    print("You are allowed")
else:
    if  atten>=75:
     print("Allowed")
    else:
        print("Not allowed")