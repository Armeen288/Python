try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("division by zero is error!")
except SyntaxError:
    print("comma is missing. Enter the numbers seperated by comma like this 1,2")
except:
    print("No exceptions")
finally:
    print("This is excute no matter what")