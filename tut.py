
# print('hello world') #use single quote or double quote
# print(9*7)
# print()
# print("the end","or is it?","keep watching",3 )
# print("python's string are easy to use")
# print('we can even include "quotes" in stirng')
# print('hello'+'world')

# greeting="hello"
# name="aakash"
# name=input("please enter your name")
# print(greeting+' '+name)

# splitstring="this string has\n been \n splitted several \n times"
# print(splitstring)
# tabbedstring="1\t2\t3\t4"
# print(tabbedstring)
# print("my name is \"aakash\'s singh")  #to escape the character we can use \
# print('my name is \'aakash singh')
# print("""my name is \"aakash\'s singh""")

# anothersplitstring="""this string\
# has been splitted in \ 
# several lines"""
# print(anothersplitstring)
# print("c:\\users\\timbuchalka\\notes.txt")
# print(r"c:\users\timbuchalka\notes.txt")  #raw string
# age=24
# print(age)
# print(type(age))
# age="aakash"
# print(age)
# print(type(age))
# print(age+"hello")

# a=12
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)  # integer division,rounded down toward minus infinity
# print(a%b)
# print() #print an empty line

# for i in range(1,a//b):
#     print(i)

# print(a+b/3-4*12)
# print(a/(b*a)/b)

# parrot="Norwegian Blue"
# print(parrot[7])
# print(parrot[-1])
# print(parrot[3])
# print(parrot[-11])
# print(parrot[0:4])
# print(parrot[2:5])
# print(parrot[0:4])
# print(parrot[10:])
# print(parrot[:]) 
# print(parrot[-4:2])
# print(parrot[-4:-2])
# print(parrot[0:6:2])

# number="9,223,234,567,987"
# print(number[1::4])


# letters="abcdefghijklmnopqrstuvwxyz"
# print(letters[25:0:-1])
# print(letters[25:-1:-1]) #will not print anything
# print(letters[25::-1])
# print(letters[::-1])
# print(letters[-10:-13:-1])
# print(letters[4::-1])
# print(letters[-1:-9:-1])
# print(letters[-4:])
# print(letters[:4])

# string1="he's "
# string2="probably "
# string3="pining "
# string4="for the "
# string5="fjords."
# print(string1+string2+string3+string4+string5)
# print("he's " "probably " "pining " "for the " "fjords.")
# print(string1*3)
# print(string1*(5+4))
# print(string1*5+"4") #if you will add 4 then will give error as integer can't be concatenated to strings.


# today="friday"
# print("day" in today)
# print("fri" in today)
# print("fry" in today) 


# age=24
# print("my age is "+str(age)+" years")
# print("my age is {0} years".format(age))
# print("there ar {0} days in {2},{1},{3}".format(31,"jan","mar","may"))

# for i in range(1,5):
#     print("{0} square is {1} and cube is {2}".format(i,i**2,i**3))

# for i in range(1,5):
#     print("{0:2} square is {1:3} and cube is {2:4}".format(i,i**2,i**3))

# for i in range(1,5):
#     print("{0:2} square is {1:<3} and cube is {2:< 4}".format(i,i**2,i**3))

# for i in range(1,5):
#     print("{0:2} square is {1:^3} and cube is {2:^4}".format(i,i**2,i**3))

# print()

# print("pi is approximately {0:12}".format(22/7))
# print("pi is approximately {0:12f}".format(22/7))
# print("pi is approximately {0:12.50f}".format(22/7))
# print("pi is approximately {0:52.50f}".format(22/7))
# print("pi is approximately {0:62.50f}".format(22/7))
# print("pi is approximately {0:.2f}".format(22/7))

# age=5
# print(f"he is {age} year old")
# print(f"pi is approximately {22/7:12.50f}")
# pi=22/7
# print(f"pi is approximately {pi:12.50f}")

# name=input("please enter your name ")
# age=int(input(f"how old are you {name} ?"))
# # print(type(age))

# if age>=18:
#     print(f"Hello, {name}")
#     print("you are eligible to vote")
# elif age<10:
#     print("you are very young")
# else:
#     print(f"please come back in {18-age} years")

# age=int(input("enter your age "))
# if age>=18 and age<=65:
#     print("have a good day at work")
# if 18<=age<=65:
    # print("have a good day at work")

# if age<18 or age>65:
#     print("enjoy your free time")
# else:
#     print("have a good day at work")


# day="monday"
# temperature=30
# raining=True
# if (day=="monday" and temperature>27) or not raining:
#     print("go swimming")
# else:
#     print("learn python")

# name=input("enter your name ")
# if name:    #same as name!=""
#     print("hello ,{}".format(name))
# else:
#     print("don't you have name?")

# parrot="Norwegian Blue"
# letter=input("enter a letter ")

# if letter in parrot:
#     print("letter available in parrot")
# else:
#     print("letter not available in parrot")

# name=input("enter your name")
# age=int(input("enter your age"))
# if age>=18:
#     print("welcome to party")
# else:
#     print("sorry")

# parrot="Norwegian Blue"
# for character in parrot:
#     print(character)

# number="9,223,353:353;343"
# temp=""
# for char in number:
#     if not char.isnumeric():
#         temp+=char
# print(temp)  

# for i in range(10,0,-1):
#     print(f"now number is {i}")

# shopping_list=["milk","pasta","eggs","bread","rice"]  #list
# for items in shopping_list:
#     if items=="eggs":
#         continue
#     else:
#         print("buy "+ items)

# print('*'*50)

# for items in shopping_list:
#     if items=="eggs":
#         break
#     else:
#         print("buy "+ items)

# i=0
# while i<10:
#     print(f"i is now {i}")
#     i+=1

# available_exit=["north","south","east","west"]
# given_exit=""
# while given_exit.casefold() not in available_exit:
#     given_exit=input("please provide exit  ")
# print("you are finally out")

# import random

# answer=random.randint(1,1000)
# for char in str(answer):
#     print(chr(65+int(char)),end="")
# print()
# temp=int(input("enter a number "))
# while temp!=answer:
#     if(answer>temp):
#         temp=int(input("please guess higher "))
#     else:
#         temp=int(input("please guess lower "))
# print("you guessed it right !")

#else in a loop

# numbers=[1,45,31,12,60]

# for number in numbers:
#     if(number%8==0):
#         print("number not acceptable")
#         break
# else:
#     print("terminated normally , all number are acceptable")

#program

# value=-1
# choices=["exit","learn python","learn java","learn c++","learn dsa"]
# given_choices=[]
# while not value==0:
#     # for choice in choices:
#     #     print(f"{choices.index(choice)}. "+choice)  # not the good way 
#     for index,choice in enumerate(choices):     #good way to use enumerate if want to print index and value
#         print(f"{index}. "+choice)
#     value=int(input("enter your choice "))
#     if value==0:
#         break
#     elif not 0<value<len(choices):
#         print("you choosed invalid option\n please choose again")
#     else:
#         print(f"you choosed {choices[value]}")
#         if choices[value] not in given_choices:
#             given_choices.append(choices[value])
#         else:
#             print("this item already choosen ")
#         print(f"your list now contains {given_choices}")
# print(given_choices)

#lists  ->mutable

# computer_parts=["computer","monitor","keyboard","mouse","mouse mat"]

# print(computer_parts[2])
# for parts in computer_parts:
#     print(parts)
# print(computer_parts[0:3])
# print(computer_parts[-1])

# result=True
# another_result=result
# print(id(result))
# print(id(another_result))

# result="correct">
# another_result=result
# print(id(result))
# print(id(another_result))
# result+="ion"
# print(id(result))
# print(id(another_result))

# print('*'*50)
# shopping_list=["milk","pasta","eggs","spam","bread","rice"]
# another_list=shopping_list
# print(id(shopping_list))
# print(id(another_list))
# print("-"*50)
# shopping_list+=["cookies"]
# print(id(shopping_list))
# print(id(another_list)) 
# print(another_list)  

# even=[2,4,6,8]
# odd=[1,3,5,7,9]

# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# print()
# print(len(even))
# print(len(odd))

# print("mississippi".count("iss"))


mylist=["hello","hi"]
mylist.append("thanks")
mylist.append(3)
list1=[2,"welcome"]
mylist.extend(list1)
print(mylist)

