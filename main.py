year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("this is not")