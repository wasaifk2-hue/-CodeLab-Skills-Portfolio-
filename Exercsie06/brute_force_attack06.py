#this program keeps asking for password
# Author: wasaif Diab
# Date: 29/12/2025

password = "12345"
while True:
    
    pwd=input("Enter the password: ")
    if pwd == password:
        print("welcome")
        break
    else:

        print("wrong password")
