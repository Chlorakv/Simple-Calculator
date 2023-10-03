#Calculator

print("Welcome")

#Taking First Value From The User
num1=int(input("Enter you first value: "))

#Taking Second Value From The User
num2=int(input("Enter you second value: "))

#Asking For The Operation that the user want to put b/w the first and second value. In this I've used a string method which is casefold which is used to make any text lowercase, I've used it to avoid errors which could stop my program.
operation=input("""Enter your operation
ADD
SUBTRACT
MULTIPLY
DIVIDE
: """).casefold()

#Using conditional statements to perform calculations.

#Addition
if operation == "add":
    print(num1 + num2)
    
#Subtraction
elif operation == "subtract":
    print(num1 - num2)
    
#Multiply
elif operation == "multiply":
    print(num1 * num2)
    
#Divide
elif operation == "divide":
    print(num1 // num2)
    
#If anyone doesn't enters any operation from the above 4 operations then it will show error.
else:
    print("Error")

