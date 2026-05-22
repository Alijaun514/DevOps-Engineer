#Function 
def function_name():
    print("Hello DevOps")
function_name()
#Function with input
def gareet(name):
    print("Hello " , name)
gareet("Ali")

# Function with return
def add(a , b):
    return a + b
result = add(5 ,7)
print("Result" , result)

# Mini project number guess Game
# def check_guess(secret , Guess):
#     if Guess == secret :
#         return "Win"
#     elif Guess < secret :
#         return "Low" 
#     else:
#         return "High"
    
# def game():
#     secret = 5
#     Attempts = 3

#     while Attempts > 0 :
#         Guess = int(input(" Guess number "))
#         result = check_guess(secret , Guess)
#         if result == "Win" :
#             print("You Win ")
#             break
#         elif result == "Low" :
#             print("Too Low")
#         else :
#             print("Too High")
#             Attempts -= 1
#             print("Attempts left : ", Attempts)
#         if Attempts == 0 :
#             print("Game Over")
# game() 

# Even / Odd 
def check_even_odd(number):

    if number % 2 == 0 :
         
         return "Even Number"
     
    else:
         return "Odd Number "

num = int(input("enter your number = "))
result = check_even_odd(num)
print(result)


 # function of bigger number 
def bigger_number(num1, num2):

    if num1 > num2:
        return num1
    else:
        return num2


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = bigger_number(a, b)

print("Bigger number is:", result)            