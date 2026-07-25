from os import write
from turtledemo.paint import changecolor
from typing import is_typeddict


def add_password():
    website = input("website: ")
    username = input("username: ")
    password = input("password:")
    with open("password.txt", "a")as file:
        file.write(f"{website}, {username}, {password}\n")
    print("good")

def shwo_password():
    with open("password.txt", "r")as file:
        for line in file:
            part = line.strip().split(",")
            website = part[0]
            username = part[1]
            password = part[2]
            print(f"website: {website}")
            print(f"username: {username}")
            print(f"password: {password}")
            print("_*25")

def search_password():
    website_to_find = input("enter website:")
    with open("password.txt", "r")as file:
        for line in file:
            part = line.strip().split(",")
            if part[0] == website_to_find :
                print(f"website: {part[0]}")
                print(f"username: {part[1]}")
                print(f"password: {part[2]}")
                break
            else:
                print("password not found")


def delete_password():
    website_to_delete = input("enter website to delete:")
    passwords = []
    with open("password.txt", "r")as file:
        for line in file:
            part = line.strip().split(",")
            if part[0] != website_to_delete:
                passwords.append(line)
    with open("password.txt", "w")as file:
        for password in passwords:
            file.write(password)

import random
import string
def generated_password():
    changecolors = string.ascii_letters + string.digits + string.punctuation
    try:
        length = int(input("enter password length: "))
    except:
        print("please enter a number")
        return
    password = ""
    for i in range(length):
        password += random.choice(changecolors)
    print("generated_password: ", password)

def mein():
    while True:
        print("\npassword_manager")
        print("1.add_password")
        print("2.shwo_password")
        print("3.search_password")
        print("4.delete_password")
        print("5.generated_password")
        print("6.exit")

        num = int(input("enter number"))
        if num == 1:
            add_password()
        elif num == 2:
            shwo_password()
        elif num == 3:
            search_password()
        elif num == 4:
            delete_password()
        elif num == 5:
            generated_password()
        elif num == 6:
            print("god boy")
            break

mein()







