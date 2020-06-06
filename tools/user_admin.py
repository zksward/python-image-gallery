# Needed for importing from parent directory
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from database import users

menu = """
1)  List users
2)  Add user
3)  Edit user
4)  Delete user
5)  Quit

Enter command> """

def menuPrompt():
    return input(menu)

def printTable(headers, data):
    for header in headers:
        print(f"|{header.ljust(30)}", end='')
    print("|\n|==============================|==============================|==============================|")
    for row in data:
        for column in row:
            print(f"|{column.ljust(30)}", end='') 
        print("|")

def listUsersCommand():
    printTable(("Username","Password","Full Name"),users.listUsers())

def addUserCommand():
    username = input("Username> ")
    if not users.userExists(username):
        password = input("Password> ")
        fullName = input("Full Name> ")
        users.addUser(username, password, fullName)
    else:
        print(f"Error: A user with the username {username} already exists")

def editUserCommand():
    username = input("Username to edit> ")
    if users.userExists(username):
        password = input("New Password (press enter to keep the same)> ")
        fullName = input("New Full Name (press enter to keep the same)> ")
        users.updateUser(username, password, fullName)
    else:
        print(f"Error: A user with the username {username} does not exist")

def deleteUserCommand():
    username = input("Username> ")
    decision = input(f"Are you sure you want to delete {username}? (yes/no)> ")
    if decision.lower() == "yes":
        users.deleteUser(username)
        print(f"Deleted {username}")

def main():
    command = 0
    while command is not '5':
        command = menuPrompt()
        if command == '1':
            listUsersCommand()
        elif command == '2':
            addUserCommand()
        elif command == '3':
            editUserCommand()
        elif command == '4':
            deleteUserCommand()
        else:
            pass

if __name__ == "__main__":
    main()