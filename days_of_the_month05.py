#this program shows number of days in a month
# Author: wasaif Diab
# Date: 29/12/2025

month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
m=int(input("Enter month number (1-12): "))
if m in month:
    print("Number of days:", month[m])
else:
    print("Invalid month number")