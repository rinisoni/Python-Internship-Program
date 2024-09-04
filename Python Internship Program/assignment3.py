# print(-18//4)
# print(2*3**3*4)
# print(10-4*2)

#minimum of two numbers
# num1=int(input("Enter first number"))#taking numbers from user
# num2=int(input("Enter second number"))
# if(num1<num2):
#     print("num1 is minimum")
# else:
#     print("num2 is minimum")

#celcius to farenheit conversion
# celcius=float(input("enter degree in celcius"))
# farenheit=celcius*1.8+32
# print(farenheit)

#average of three numbers
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# num3=int(input("enter 3rd number"))
# average=(num1+num2+num3)/3
# print(average)

#Q.7
games_played=int(input("Enter the number of games played in a tournament"))
games_won=int(input("Enter the number of games won"))
games_lost=int(input("Enter the number of games lost"))

games_tie=games_played-games_lost-games_won
#OR
#games_tie=games_played-(games_lost+games_won)
total_score=(games_won *4) +(games_tie * 2)
print(f"You scored = {total_score}")
