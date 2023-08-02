#Calculator program allows user to select option of Add, Subtract, Multiply
#and divide. It then allows them to select two numbers as input then 
#processes the output as the answer
#this defines what add is. Add is addition
def add(x, y):
    return x + y
#Defines subraction
def subtract(x, y):
    return x - y
#defines multiplication
def multiply(x, y):
    return x * y
#defines division 
def divide(x, y):
    return x / y
#that takes care of how the calculator works. Next we need to program 
#what the user sees and how they interact with this calculator
print("Select opration. ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    #take input from user. input function prints a message onscreen with 
    #the option for the user to type out an instruction or message
    choice = input("Enter choice(1/2/3/4): ")
    
    #check if choice is one of the four options.
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number. ")
            continue

        if choice == '1':
            print(num1, '+', num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
            