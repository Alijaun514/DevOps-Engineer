age = int(input("enter your age "))

if age >= 18:
    print("you are adult")
else:
    print("you are minor")

# Example (even/odd)    
        
num = int(input("Enter number : "))

if num % 2 == 0:
    print("Even number = ")
else:
    print("Odd number = ")       

    # Multipul conditions (elif)

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("A Grad")
elif marks == 50:
     print("Pass")
else:
    print("Fail")

# Task01 Number Positive ya Negative

number = int(input("Enter your number"))

if number >= 0:
    print("Positive number")
else:
    print("Negative number")

# Task 02  Password check

Password = input("Enter your password")

if Password == "1234":
    print("Access Granted")
else:
    print("Wrong Password")

# Task 03 biggest number

a = int(input("Enter first your number: "))
b = int(input("Enter second number: "))

if a > b :
    print("A is bigger")
else:
    print("B is bigger")

# Mini task  check temperature

temperature = int(input("enter temperatre: "))

if temperature >= 30:
    print("weather is Hot")
elif temperature >= 20 :
    print("weather is Normal")
else:
     print("weather is Cool")
