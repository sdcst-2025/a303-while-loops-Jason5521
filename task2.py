#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
adminname = "admin"
adminpassword = "12345"
Loggedin = False

while not Loggedin:
    username = input("Enter username: ")
    if username != adminname:
        print("Access denied")
    else:
        password = (input("Enter password: "))
        if password != adminpassword:
            print("Access denied")
        else:
            Loggedin = True

print("Access granted")