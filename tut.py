
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


# mylist=["hello","hi"]
# mylist.append("thanks")
# mylist.append("good morning")
# list1=["how are you","welcome"]
# mylist.extend(list1)
# print(mylist)

# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)

# pangram=sorted("The quick brown fox jumps over the lazy dog",key=str.casefold)
# print(pangram)

# names=["Aakash","graham","Nikhil","vivek","sunil","Dev"]
# names.sort(key=str.casefold)
# print(names)

# empty_list=[]
# digits=sorted("87031246")
# digits=list("87031246")
# print(digits)
# print()

# more_digits=digits.copy()
# print(more_digits is digits) #another way for checking if have same id
# print(digits==more_digits)

#replacing a slice
# computer_parts=["cpu","monitor","keyboard","mouse","mouse mat"]
# print(computer_parts)

# computer_parts[3:]="trackball"
# computer_parts[3:]=["trackball"]
# print(computer_parts)

#deleting list data




# data=[4,5,104,105,110,120,130,140,150,160,170]
# print(data)
# del data[0:2]
# del data[7:]
# print(data)
# print(data)
# min_value=104
# max_value=150
# for index,value in enumerate(data):
    # if value<min_value or value>max_value: 
        # del data[index]                     # not giving expected output
# print(data)

#iterating list backward
# for index in range(len(data)-1,-1,-1):
#      if data[index]<min_value or data[index]>max_value: 
#         del data[index]                     #  giving expected output
# print(data)

# original_last_index=len(data)-1
# for index,value in enumerate(reversed(data)):
#     if value<min_value or value>max_value:
#         del data[original_last_index-index]   #length will change so we initialise first
#         print(original_last_index-index)
# print(data)
 
# even=[2,4,6,8]
# odd=[1,3,5,7,9]
# # number=even+odd
# number=[even,odd]
# print(number)

# for number_list in number:
#     print(number_list)

#     for value in number_list:
#         print(value)

#nested list

# menu=[
#     ["egg","bacon"],
#     ["egg","sausage","bacon"],
#     ["egg","spam"],
#     ["egg","bacon","spam"],
#     ["spam","bacon","sausage","spam"],
#     ["spam","sausage","spam","bacon","spam","tomato","spam"],
#     ["spam","egg","spam","spam","bacon","spam"]
# ]

#1st approach to print menu without spam
# for meal in menu:
#     for index in range(len(meal)-1,-1,-1):
#         if meal[index]=="spam":
#             del meal[index]
# print(menu)

#2nd approach to print menu without spam

# for meal in menu:
#     for item in meal:
#         if item!="spam":
#             print(item)
#     print()

# char_list=["a","b","c","d"]
# for i in char_list:
#     print(i,end=" ")

# name="tim"
# age=20
# print(name,age,"python",2020,sep=":")

#the function can take several parameters when *object is in definition like print function

#join method

# flowers=[
#     "Daffodil",
#     "Evening Primrose",
#     "Hydrangea",
#     "Iris",
#     "Lavender",
#     "Sunflower",
#     "Tiger Lily"
# ]                     # if we add a integer here then join will give error
# seperator=" | "
# seperator=","
# output=seperator.join(flowers)
# print(output)

#split method

# panagram="The quick brown fox jumps over the lazy dog"
# panagram="""The quick brown
# fox jumps\tover
# the lazy dog"""
# words=panagram.split() #default splitting argument is space
# print(words)

# numbers="9,224,453,345,345,675,567"  #to make list from sequence use split for opposite use join
# print(numbers.split(","))
# value=numbers.split(",")
# integer_value=[]
# for item in value:
#     integer_value.append(int(item))
# print(integer_value)
 
#Tuples -  ordered set of data and are immutable

# t="a","b","c"  #can do this but always use parenthesis to avoid some unexpected result
# t=("a","b","c") 
# print(t)
# print(t[0])
# # t[0]="c" #will give error as tupple is immutable
# name="Tim"
# age=10
# print(name,age,"python",2020)
# print((name,age,"python",2020))

# a=b=c=d=42
# print(c)
# x,y=1,2
# print(x)
# print(y)

# data=1,2,3  #data represents tuple
# x,y,z=data
# print(x)
# print(y)
# print(z)

# #unpacking tuple
# for t in enumerate("abcdefghij"):   #enumerate return tuples
#     index,character=t
#     print(index,character)

#nesting list and tuple

# albums=[("welcome to my Nightmare","Alice Cooper",1975),
#          ("Bad Company","Bad company",1974),
#          ("Nightflight","Budgie",1981),
#          ("More Mayhem","Emilda May",2011),
#          ("Ride the Lightning","Metallica",1984),
#          ]
# print(len(albums))

# for album_name,artist,year in albums:  #unpacking the tuple
#     print(f"Album: {album_name} ,Artist:{artist} , Year:{year} ")


#constants in python
#By convention constants are defined in all capital letters

#SONGS_LIST=3

#Function in python

# def multiply(x,y):
#     result=x*y
#     return result


# answer=multiply(10.5,4)
# print(answer)
# print(multiply(9,7))  

# for val in range(1,5):
#     two_times=multiply(2,val)
#     print(two_times) 

# def is_palindrome(str):
    # if(str==(str[::-1])):
        # return True
    # else:
        # return False
    # return str.casefold()==str[::-1].casefold()


# print(is_palindrome("Radar"))

# def is_palindrome_sentence(sentence):
#     str=""
#     for char in sentence:
#         if char.isalnum():
#             str+=char
#     # return str.casefold()==str[::-1].casefold()
#     return is_palindrome(str)  #function calling function

# sentence=input("enter a sentence ")
# print(is_palindrome_sentence(sentence))

# def adder(a:int,b=10)->int:   #default arguments and annotation
#     """
#     Docstring:
#     add two number and by default one number is 10
#     """  
#     return a+b

# print(adder(4))
# print(adder(a=5)) #keyword arguments
# print(adder(2,3))
 
# print(adder.__doc__)
# help(adder) 

# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(20))

#printing in color
 
# RED='\u001b[31m'
# RESET='\u001b[0m'
# print(RED,"this will be in red colour")
# print("and so is this")
# print(RESET,"but not this")

#*args

# numbers=(0,1,2,3,4,5)

# print(numbers,sep=";")
# print(*numbers,sep=";")  # * will unpack tuple here
# print(0,1,2,3,4,5,sep=";")

# def test_star(*args):
#     print(args)
#     for x in args:
#         print(x)

# test_star(0,1,2,3,4,5)

# def func(p1,p2,*args,k,**kwargs):
#     print("positional-or-keyword:...{}, {} ".format(p1,p2))
#     print("var-positional (*args):...{} ".format(args))
#     print("keyword:....{} ".format(k))
#     print("var-keyword:....{} ".format(kwargs))

# func(1,2,3,4,5,k=6,key1=7,key2=8)

#binary

# for i in range(17):
#     print("{0:>2} in binary is {0:>08b} ".format(i))

# for i in range(17):
#     print("{0:>2} in hexadecimal  is {0:>02x} ".format(i))

# x=0x20   #x represent hexadecimal number
# y=0x0a
# print(x)
# print(y)
# print(x*y)

# print(0b001010001) 

#Dictionary and sets    -> not sequence so can't be accessed by index




# vehicles={
#     'dream':'Honda 250T',
#     'roadster':'BMW R1100',
#     'er5':'Kawasaki ER5',
#     'can-am':'Bombardier Can-Am 250',
#     'jimny':'Suzuki Jimny 1.5'
# }

# my_car=vehicles['jimny']   #will give keyerror when key not matched
# print(my_car)

# learner=vehicles.get("er5")  #will give none when key not match exactly
# print(learner)
# print()
# # for key in vehicles:                    # use .items() method for more efficiency
# #     print(key,vehicles[key],sep=" : ")

# vehicles["fighter"]="Rafael"
# vehicles["toy"]="glider"

# #upgrading
# vehicles["fighter"]="F-35"

# #deleting
# # del vehicles["fighter"] #will give error when key not exists
# # vehicles.pop("f1",None)  #will not give error when key not exists
# # result=vehicles.pop("f1",None)

# result=vehicles.pop("fighter","Not present")
# print(result)
# for key,value in vehicles.items():
#     print(key,value,sep=" : ") 

# #using in with dictionary
# print("toy" in vehicles)  # check only key not values
# print("glider" in vehicles)

# #set default method

# pantry={
#     "milk":450,
#     "potatato":2,
# }

# chicken_quantity=pantry.setdefault("chicken",0)
# print(f"chicken: {chicken_quantity}")
# beans_quantity=pantry.get("ketchup",0)
# print(f"beans: {beans_quantity}")

# print(pantry)

# from getpass import getpass

# # a=getpass("enter name") # similar to input but not show while typing
# # print(a)

# pantry_items=['chicken','spam','egg','bread','lemon']

# new_dict=dict.fromkeys(pantry_items)
# new_dict=dict.fromkeys(pantry_items,0) # 0 here denoting default value
# print(new_dict)

# keys=pantry.keys()
# print(keys)

# pantry2={
#     "milk":2000,
# }
# #dict update method  
# pantry.update(pantry2)

# for items,value in pantry.items():
#     print(items,value)

# #dict value method
# v=pantry.values()
# print(v)

# pantry["potatato"]=3
# print(pantry)

# print("potatato" in pantry)
# print("milk" in pantry)

# #Reference to mutable objects
# animals={
#     "lion":"scary",
#     "elephant":"big",
#     "teddy":"cuddly",
# }
# # things=animals
# #if we want to make a copy then we use copy methods 
# things=animals.copy()
# animals["teddy"]="toy"
# print(things["teddy"])

#shallow copy

# animals={
#     "lion":["scary","big","cat"],
#     "elephant":["big","grey","wrinkled"],
#     "teddy":["cuddly","stuffed"]
# }
# things=animals.copy()
# things["teddy"].append("toy")  # animals will also be changed as it is shallow copy
# print(animals)
# print(things)
# print(id(animals["teddy"]))
# print(id(things["teddy"]))
# #deep copy 

# import copy
# animals={
#     "lion":["scary","big","cat"],
#     "elephant":["big","grey","wrinkled"],
#     "teddy":["cuddly","stuffed"]
# }
# things=copy.deepcopy(animals)
# things["teddy"].append("toy")  # animals won't be changed as it is deep copy
# print(animals)
# print(things)

# print(id(animals["teddy"]))
# print(id(things["teddy"]))

# #hashing

# def simple_hash(s):
#     basic_hash=ord(s[0])
#     return basic_hash%10

# data=[("orange","a sweet, orange,citrus fruit"),
#       ("apple","red and good"),
#       ("lemon","a sour, yello fruit"),
#       ("grape","small green fruit"),
#       ("melon","sweet and juicy"),
# ]

# for key,value in data:
#     h=simple_hash(key)
#     # h=hash(key)
#     print(key,h)

# import hashlib  #hashlib ->secure hash model
# print(sorted(hashlib.algorithms_guaranteed))
# print(sorted(hashlib.algorithms_available))

# python_program="""
# for i in range(10):
#     print(i)
# """
# print(python_program)
# original_hash=hashlib.sha256(python_program.encode('utf8'))
# print(f"SHA256: {original_hash.hexdigest()}")


# sets  -> do not have any order , we can't use index with sets

# farm_animals={'cow','sheep','hen','goat','horse'}
# print(farm_animals)

# for animal in farm_animals:
#     print(animal)

# animal={'sheep','cow','horse','goat','hen'}

# if animal==farm_animals:
#     print("both set are equal ")

# #checking item in set is fast compared to list as it use hashing

# numbers={}
# print(type(numbers))
# # numbers={*""} #unpacking
# numbers=set()
# numbers.add(1)  #adding data to sets
# print(numbers,type(numbers))

# while len(numbers)<4:
#     next_value=int(input("enter your next value "))
#     numbers.add(next_value)

#deleting items from set
# small_ints=set(range(21))
# print(small_ints)
# # small_ints.clear()
# # print(small_ints)

# small_ints.remove(11)
# small_ints.discard(11) #not give error if element is not present
# print(small_ints)

# #pop method
# #set aren't indexable so set pop method not take any arguments like list or dictionary
# # it pops an arbitrary items from the sets and returns that item

# trail_patients={"denise","eddie","frank","georgia","kenny"}

# while trail_patients:
#     patient=trail_patients.pop()
#     print(patient)

# farm_animals={'cow','sheep','hen','goat','horse'}
# wild_animal={'lion','elephant','horse','goat','tiger','bear'} 

# #union
# all_animals=farm_animals.union(wild_animal)
# print(all_animals)
# all_animals2=farm_animals|wild_animal
# print(all_animals2)

# #union update ->if we donot create a new variable but updated union in same variable

# farm_animals.update(wild_animal) #or
# # farm_animals|=wild_animal
# print(farm_animals)

# evens=set(range(0,30,2))
# temp={1,2,3,4,5,6,7,8,9,10}
# #intersection
# print(evens.intersection(temp))
# print(evens&temp)

# #set differences
# print(evens.difference(temp))
# print(evens-temp)

# #symmetric difference -> opposite of intersection

# print(evens^temp)
# print(evens.symmetric_difference(temp))   #method also work with list but operator not work with list

#subsets and supersets

# animals={
#     'turtle',
#     'horse',
#     'robin',
#     'python',
#     'swallow',
#     'wren',
#     'cat',
# }
# birds={'robin','swallow','wren'}
# garden_birds={'robin','swallow','wren'}
# print(garden_birds<birds)
# print(garden_birds==birds)
# print(garden_birds<=birds)
# print(birds<=animals)
# print(animals>birds)
# print(animals>=birds)
# print(birds.issubset(animals))
# print(animals.issuperset(birds))


#Reading and Writing files in Python
#reading
# print("hello")
# aakash1=open('aakash.txt','r')    # not the good way

# for line in aakash1:
    # print(line.strip())
    # print(line,end='')

# aakash1.close() 

#opening file with 'with'
# with open('aakash.txt','r') as aakash:
#     # for line in aakash:
#     #     print(line.rstrip())
#     all_lines=aakash.readlines()    

# print(all_lines)  #we will get all text as list with readlines()
# print(all_lines[-1:])

# with open('aakash.txt','r') as aakash:
#     all_lines=aakash.read()    # we will get all text as string with read()

# print(all_lines) 

# for character in reversed(all_lines):
#     print(character,end='')

with open('aakash.txt','r') as aakash:
    all_lines=aakash.readline().rstrip()    # we will single line as string

print(all_lines) 

for character in reversed(all_lines):
    print(character,end='')

print()
# strip, istrip and rstrip
char='"'
no_quotes=all_lines.strip(char)
print(no_quotes)

char='". Myh'
check=all_lines.strip(char)  #strip check the charater in start and end.
#if that character is present then it will remove it
print(check)

# removeprefix and removesuffix method ->added in python 3.9 so we will write function for this

def removeprefix(string,prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]

def removesuffix(string,suffix):
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]

# p_removed=all_lines.removeprefix('". Myh')  this is not available in python 3.8
# s_removed=all_lines.removesuffix('gh. "')   this is not available in python 3.8

print()
p_removed=removeprefix(all_lines,'"My ')
s_removed=removesuffix(all_lines,'gh."')
print(p_removed)
print(s_removed)

#parsing -> making sense of data

countries={}
input_filename='country_info.txt'
with open(input_filename) as file:
    file.readline()     #for loop will start from second line as we have already read first line
    for row in file:
        data=row.strip('\n').split('|')
        country,capital,cc,cc3,iac =data
        # print(country,capital,cc,cc3,iac)
        # print(data) 
        country_dict={
            'name':country,
            'capital':capital,
            'country_code':cc,
            'cc3':cc3,
            'iac':iac,
        }
        print(country_dict)
        countries[country.casefold()]=country_dict

print(countries)

data={
    'neem','mango','peepal','banyan','sandalwood'
}

# with open('tree.txt','w') as plants:     #print method convert object into string 
#     for plant in data:
#         print(plant,file=plants)

with open('tree.txt','w') as plants:       #write method write as it is
    for plant in data:
        plants.write(plant)

# with open('tree.txt','w') as plants:       #not give error as print convert int to string
#     for i in range(10):
#         print(i,file=plants)
                
with open('tree.txt','w') as plants:       #will give error if we not typecast int to string
    for i in range(10):
        plants.write(str(i))

# with open('tree.txt',encoding='utf-8') as jabber:  we should provide encoding 