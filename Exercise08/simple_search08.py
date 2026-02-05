#this program searches for a number in a list
# Author: wasaif Diab
# Date: 29/12/2025

names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_term = input("Enter the name to search: ")

if search_term in names:
    print(search_term, "found in the list!")
else:
    print(search_term, "not found in the list.")

