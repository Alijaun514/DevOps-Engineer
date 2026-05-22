# For Loop
for i in range(5):
    print("Hello DevOps")

# Example 02

for i in range(1 , 6):
    print(i)

# While loop
#i = 1

#while i <= 5:
 #   print(i)

#i += 1


# PRINT TAble
# num = int(input("enter your number "))
# for i in range(1 , 11):
#      print(num , "*", i , "=", num*i )  
# SUN NUMBERS
# total = 0
# for i in range(1,6):
#     total += i
#     print("sum = ",total)
secret = 5

while True:
    guess = int(input("enter guess number (1-10): "))

    if guess == secret :
        print(" You Win the Game ")
        break
    elif guess >= secret:
        print("Guess is Too larg")
        break
    elif guess <= secret :
        print("Guess is too low")
        break
    else:
        print("Try Again")
