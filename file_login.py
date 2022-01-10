import os
import getpass

if not os.path.exists('database.txt'):
    fs = open('database.txt', 'w')


def register():
    print("===============User Register ============")
    username = input("Enter username:")
    if username in open('database.txt', 'r').read():
        print('Username already exists')
        exit()

    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Enter confirm password: ")
    if password != confirm_password:
        print("password not match")
        exit()
    file = open('database.txt', 'a')
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()
    print("user was successfully register")


def login():
    print("===============User Login ============")
    username = input("Enter username:")
    password = getpass.getpass("Enter password: ")

    find_data = open('database.txt', 'r').readlines()
    users_data = []
    for users in find_data:
        users_data.append(users.split())

    total_users = len(users_data)
    increment = 0
    login_success = False
    while increment < total_users:
        uname = users_data[increment][0]
        upass = users_data[increment][1]
        if username == uname and password == upass:
            login_success = True

        increment += 1

    if login_success:
        print(f"Welcome {username}")
    else:
        print("username & password not match")


question = input("Do you have an account?y/n: ")
if question == 'y':
    login()
else:
    register()