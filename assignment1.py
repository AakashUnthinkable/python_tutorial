# 1. Program to convert the temperature from Celsius to Fahrenheit each weekday


# temperature_weekday_celsius=[40,42.1,43.5,38.7,37,44.2,45.3]
# temperature_weekday_celsius_average=sum(temperature_weekday_celsius)/7
# temperature_fahrenheit=((temperature_weekday_celsius_average)*9)/5+32
# print(temperature_fahrenheit)

# 2. Calculate a cube of a number greater than 7

# number=13
# cube=pow(number,3)
# cube=number*number*number
# print(cube)

# 3. Find the greater of the two numbers

# 1st method

# first_num=int(input("enter first number "))
# second_num=int(input("enter first number "))
# if(first_num==second_num):
#     print("both are equal")
# elif(first_num>second_num):
#     print(f"{first_num} is greater")
# else:
#     print(f"{second_num} is greater ")

# 2nd method

# first_num=int(input("enter first number "))
# second_num=int(input("enter first number "))
# greater_num=first_num if first_num>=second_num else second_num
# print(greater_num)

# 4. Write a program that prints the numbers from 1 to 50. But for multiples of three print “three” instead of the number and for the multiples of five print “five”. For numbers that are multiples of both three and five print “threefive”.

for num in range(1,51):
    if(num%3==0 and num%5==0):
        print("threefive")
    elif(num%3==0):
        print("three")
    elif(num%5==0):
        print("five")
    else:
        print(num)

