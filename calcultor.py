def add(num1, num2):
    return int(num1) + int(num2)

def substract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1) / int(num2)

num1 = input("please enter the value of num1:")
num2 = input("please enter the value of num2:")

operator = input("choose the operation to be perform: [add,substract,multiply,divide] ")


if operator == "add":
    result = add(num1, num2)

elif operator == "substract":
    result = substract(num1, num2)

elif operator == "multiply":
    result = multiply(num1, num2)

elif operator == "divide":
    result = divide(num1, num2)

else:
    result = 0
    print("invalid operator")

print("sum of two number is:"+ str(result))