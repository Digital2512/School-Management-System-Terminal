import os
import sys 
import time
import database
import generalUtils

def pgMain():
    while True: 
        generalUtils.clearConsole()
        generalUtils.createNewLine()
        print("Welcome to Excellent Tution Centre(ETC)\n1. LOGIN\n2. EXIT")
        generalUtils.createNewLine()
        choice = int(input("Choice: "))
        if choice == 1: 
            #Login 
            generalUtils.clearConsole()
            generalUtils.createNewLine()
            print("Login")
            generalUtils.createNewLine()
            list = database.readFile("UserDetails.txt")

            #Give 3 tries for username and also password respectively
            for i in range(0 , 3, 1):
                inputUsername = input("Username: ")
                isUsernameFound = database.searchListValue(inputUsername, 1, list)
                if isUsernameFound:
                    break

            if isUsernameFound == False:
                return
            
            for i in range(0,3,1):
                inputPassword = input("\nPassword: ")
                isPasswordFound = database.searchListValue(inputPassword, 2, list)
                if isPasswordFound:
                    break
            
            if isPasswordFound == False:
                return
            
            # Success logged in
            if isUsernameFound and isPasswordFound == True:
                roleFound = database.readListValue(inputUsername, 1, 0,"UserDetails.txt")
                capitalizedRole = roleFound.upper()
                if capitalizedRole == "ADMIN":
                    print("Admin")
                    break
                    # Add code to navigate to the admin's page here
                elif capitalizedRole == "TUTOR":
                    print("Tutor")
                    break
                    # Add code to navigate to the tutor's page here
                elif capitalizedRole == "STUDENT":
                    print("Student")
                    break
                    # Add code to navigate to the student's page here
                elif capitalizedRole == "RECEPTIONIST":
                    print("Receptionist")
                    break
                else: 
                    print("Role Not Found")
                    break
            else: 
                print("Your account might have been deleted (If you think this is a mistake, please contact the Admin)")
                break

        elif choice == 2:
            print("\nThank you for visiting TEC")
            sys.exit()

        else:
            print("\nInvalid Option")
            continue


pgMain()
