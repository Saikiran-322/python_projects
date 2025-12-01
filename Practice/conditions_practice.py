age = int(input("Enter your age: "))


if age <13:
    print("You are a child.")
elif 13<= age < 18:
    print("You are teenager.")
elif age>=18:
    print("You are an adult and allowed to vote.")
else:
    print("Enter values above 1.")