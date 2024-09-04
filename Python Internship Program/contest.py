year=int(input("Enter a year"))#taking year from user
if year % 400 ==0 and year % 100 ==0: #divided by hundred = century year
    print("It is a leap year") #century year/400 = leap year
elif year % 4 == 0 and year % 100 != 0: #not divided by hundred = not a century year
    print("It is a leap year") #year/4 = leap year
else: #if both conditions false, not a leap year
    print("It is not a leap year")
