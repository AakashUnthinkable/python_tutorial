# #generator save memory
# import numbers
# import sys
# # big_range=range(1000)

# def my_range(n):
#     start=0
#     while(start<n):
#         yield start
#         start+=1

# big_range=my_range(1000)
# print("big int is of {} bytes".format(sys.getsizeof(big_range)))
# big_list=[]
# for i in big_range:
#     big_list.append(i)
# print("big list is of {} bytes".format(sys.getsizeof(big_list)))


# a=2
# b=3
# print("a is {}, b is {} ".format(a,b))
# a,b=b,a
# print("a is {}, b is {} ".format(a,b))

# def fibinacci():
#     current,previous=0,1
#     while True:
#         yield current 
#         current,previous=current+previous,current


# fib=fibinacci()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# def odd_num():
#     start=1
#     while True:
#         yield start
#         start+=2

# # odd=odd_num()

# # for i in range(101):
# #     print(next(odd))

# def pi_series():
#     odd=odd_num()
#     approximation=0
#     while True:
#         approximation+=(4/next(odd))
#         yield approximation
#         approximation-=(4/next(odd))
#         yield approximation


# approx_pi=pi_series()
# for x in range(10):
#     print(next(approx_pi))


# # List comprehension

# numbers=[1,2,3,4,5,6]
# squares=[number**2 for number in numbers]  
# squares={number**2 for number in numbers}  # Set comprehension
# print(squares) 

# text="how are you"
# capitals=[char.upper() for char in text]
# print(capitals)
# words=[word.upper() for word in text.split(' ')]
# print(words)

# menu=[
#     ["egg","bacon"],
#     ["egg","sausage","bacon"],
#     ["egg","spam"],
#     ["egg","bacon","spam"],
#     ["spam","bacon","sausage","spam"],
#     ["spam","sausage","spam","bacon","spam","tomato","spam"],
#     ["spam","egg","spam","spam","bacon","spam"]
# ]

# #conditional comprehension
# meals=[meal for meal in menu if "spam" not in meal and "chicken" not in meal]  # 1st part-> expression , 2nd part-> iteration ,3rd part->filter
# print(meals)

# #conditional expression
# meals=[meal if "spam" not in meal else "a meal skipped" for meal in menu]
# print(meals)

# #nested comprehension
# burgers=["chicken","spicy beans","egg"]
# toppings=["cheese","beans","spam"]

# for nested_meals in [[(burger,topping) for burger in burgers] for topping in toppings]:
#     print(nested_meals)


# for x,y in [(i,i*j) for i in range(1,11) for j in range(1,11)]:  # list comprehension
#     print(x,y)

# for x,y in ((i,i*j) for i in range(1,11) for j in range(1,11)):  # generator
#     print(x,y)


# # Timeit module

# import timeit
# from statistics import mean,stdev

# fact_test="""\
# def fact(n):
#     result=1
#     if n>1:
#         for f in range(2,n+1):
#             result*=f
#     return result

# x=fact(130)
# """

# factorial_test="""\
# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# y=factorial(130)
# """

# print(timeit.timeit(fact_test,number=10000))
# list1=timeit.repeat(fact_test,number=10000,repeat=5)
# print(timeit.timeit(factorial_test,number=10000))
# list2=timeit.repeat(factorial_test,number=10000,repeat=5)
# print(mean(list1),stdev(list1))
# print(mean(list2),stdev(list2))


# map
from functools import reduce
import numbers


text="what have the roman ever done for us"
map_capitals=list(map(str.upper,text))
print(map_capitals)
map_words=list(map(str.upper,text.split(" "))) # when passing function as argument don't include parenthesis
print(map_words)

# filter

menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"]
]

def not_spam(meal_list:list):
    return "spam" not in meal_list

spamless_meals=list(filter(not_spam,menu))
print(spamless_meals)

#comprehension generally take less time than map and filter

#Reduce
# it take function and sequence and reduce sequence to one value by repeateadly calling function

import functools
def add(x,y):
    return x+y

numbers=[2,3,5,8,13]
reduced_value=functools.reduce(add,numbers)
print(reduced_value)
print(sum(numbers))

# any and all
entries=[1,2,3,4,5,0]
if entries:
    print("all:{}".format(all(entries))) #all return true if all item in list are true value
else:
    print("false")
print("all:{}".format(any(entries))) #any return true if any item in list are true value

result=bool(entries) and all(entries)
print(result)

# named tuple

