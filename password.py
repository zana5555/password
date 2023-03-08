# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 02:53:03 2023

a python code for manage password with creation a json file.
this code asks a user to reate a pssword butif the user likes
the code itself create a password with 8 characters.

@author: Mokhtar Mahmoudian

"""
import json
file_name = "password.json"
def user_password_creator():
    with open(file_name, "w") as f:
        json.dump(input("enter a strong password :"),f)
def user_goal():
    print("create a strong password or change your password ")
    response = input("if you want to generate a password by yourself enter u\
                     but if you want the computer generate it for you enter p :\
                         if you want to quit enter q :")
    if response == "u":
        user_password_creator()
    elif response == "p":
        python_password_creatror()
    elif response == "q":
        return
    else:
        user_goal()
        
def python_password_creatror():
    import string, random
    password = ""
    for i in range(8):
        password += random.choice(string.ascii_letters + string.digits)
        with open(file_name, "w") as f:
            json.dump(password, f)
    print("your password is :" ,password)
    react = input("do you want to change your password ? y/n  :")
    if react == "y":
        user_goal()
    elif react == "n":
        pass
    
def password_reader():
    try:
        with open(file_name) as f:
            password = f.read()
            print("your password is :" ,password)
            react = input("do you want to change your password ? y/n  :")
            if react == "y":
                user_goal()
            elif react == "n":
                pass
    except FileNotFoundError :
        print("create a strong password ")
        response = input("if you want to generate a password by yourself enter u\
                         but if you want the computer generate it for you enter p :")
        if response == "u":
            user_password_creator()
        elif response == "p":
            python_password_creatror()
        else:
            user_goal()
password_reader()

            
            

    

    
    


