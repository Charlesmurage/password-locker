#!/usr/bin/env python3.6
from password import Password

def create_password(smedia,first_name,last_name,user_name,password):
        new_password = Password(smedia,first_name,last_name,user_name,password)
        return new_password

def save_password(password):
        password.save_password()

def delete_passwords(Password):
        password.delete_passwords()

def display_passwords():
        return Password.display_passwords()

def main():
        print("Welcome to your password list. What is your name?")
        user_name = input()

        print(f"hello{user_name}. What would you like to do?")
        print('\n')

        while True:

                print("use these short codes : cp - create new password, dp -display passwords, ex - exit the password list" )

                short_code = input().lower()
                if short_code == 'cp':
                        print("New Password")
                        print("-"*10)

                        print("which social media account?")
                        smedia = input()
                        print("First Name")
                        first_name = input()

                        print("Last Name")
                        last_name = input()

                        print("Username")
                        user_name = input()

                        print("Password")
                        password = input()


                        save_password(create_password(smedia,first_name,last_name,user_name,password))
                        print('\n')
                        print(f"New Password {first_name} {last_name} created")
                        print('\n')

                elif short_code == 'dp':
                    if display_passwords():
                        print("Here is a list of all your passwords")
                        print('\n')

                    for password in display_passwords():
                        print(f"{password.first_name} {password.last_name} .....{password.password}")

                        print('\n')

                else:
                        print('\n')
                        print("You don't seem to have any password")
                        print('\n')

                elif short_code == "ex":
                            print("Bye .......")
                            break
                else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()
