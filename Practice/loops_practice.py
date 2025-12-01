i = 1
while i<=10:
    print(i)
    i += 1

print("------------")

for i in range(1,11):
    print(i)

print("------")


correct_password = "Python123"


while True:
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Your password is correct.")
        break
    else:
        print("Password didn't match. Enter correct password.")
        

