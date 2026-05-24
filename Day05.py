# File Handling? Program ke data ko file me save/read karna

# file write
file = open("data.txt" , "w")
file.write("Hello DevOps ")
file.close()

# file read 
file = open("data.txt" , "r")
content = file.read()
print(content)
file.close()

# Append Mode (new data add)
file = open("data.txt" , "a")
file.write("\nNew Line Added")
file.close()

#Logs kya hote hain?
#System/activity records
#Example:
#deployment successful
#server error
#user login
#container crash


# write log

file = open("log.txt" , "a")
log = input("Enter log message : ")
file.write(log + "\n")
file.close()
print("log saved")

# Read log 
file = open("log.txt" , "r")
print(file.read())
file.close()

#Better method (with open)
with open("data.txt" , "w") as file:
    file.write("professional coding")

# Task 1 
# Eik file bnao jis mia file student name ki ho aur std name , city , skill

file = open("student.txt" , "w")
file.write("Name: Muhammad Ali jaun\n")
file.write("City: Multan\n")
file.write("Skill DevOps\n")

file.close()
print("log saved")

#TASK 02
#Program banao: user se notes le notes.txt me save kare

note = input("ENTER YOR NOTES: ")
with open("note.txt " , "a") as file:
    file.write(note)
    print("note saved in note.txt")

#Task 3:
#Ek log system banao: login success login failed sab logs file me save hon

def login_system():
    correct_username = "Ali12"
    correct_password = "1234"

    username = input("enter username: ")
    password = input("enter password: ")

    file = open("logs.txt" , "a")
    if username == correct_username and password == correct_password:
        print("Login success")
        file.write(f"username: {username} - login success\n")
    else:
        print("Login Failed")
        file.write(f"password {password} - Login Failed\n")
    file.close()
login_system()            

#MINI PROJECT — ToDo App (File Based)
task = input("enter you task: ")

with open("todo.txt" , "a") as file:
    file.write(task + "\n")

    print("task saved")