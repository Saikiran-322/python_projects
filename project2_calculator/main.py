def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Error: Cannot divide by zero"
    return a/b


print("Simple calculator")
print("-----------------")


while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Good Bye!")
        break

    if choice not in ["1","2","3","4"]:
        print("Invalid choide!")
        continue


    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number! Try again.")
        continue

    if choice  == "1":
        print("Result:", add(num1,num2))
    elif choice == "2":
        print("Result:", subtract(num1,num2))
    elif choice == 3:
        print("Result:",multiply(num1,num2))
    elif choice=="4":
        print("Result:",divide(num1,num2))



