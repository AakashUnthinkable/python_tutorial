# a=12
# b=4
# print(a+b)
# print(a.__add__(b))

# class Kettle(object):

#     power_source="electricity"      #class attributes

#     def __init__(self,make,price) -> None:
#         self.make=make
#         self.price=price
#         self.on=False

#     def switch_on(self):
#         self.on=True

# kenwood=Kettle("Kenwood",8.99)
# print(kenwood.make)
# print(kenwood.price)

# kenwood.price=7.5
# print(kenwood.price)
# print(type(kenwood))

# hamilton=Kettle("Hamilton",14.55)

# print("Models:{}={} ,{}={} ".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))
# print("Models:{0.make}={0.price} ,{1.make}={1.price} ".format(kenwood,hamilton))

# print(hamilton.on)
# hamilton.switch_on()
# print(hamilton.on)

# kenwood.power=1.5  #instance variable
# print(kenwood.power)

# print("change to atomic power")
# Kettle.power_source="atomic power"
# print(Kettle.power_source)
# print(hamilton.power_source)
# print("switch kenwood to gas")
# kenwood.power_source="gas"
# print(kenwood.power_source)

# print(Kettle.__dict__)
# print(hamilton.__dict__)
# print(kenwood.__dict__)

# import datetime
# import pytz

# class Account:
#     """Simple account class with balance"""
    
#     @staticmethod                 #static method
#     def _current_time():
#         utc_time=datetime.datetime.utcnow()
#         return pytz.utc.localize(utc_time)

#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#         self.transaction_list=[]
#         print("Account created for "+self.name)

#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             self.show_balance()
#             self.transaction_list.append((Account._current_time,amount))
#             # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()),amount))

#     def withdraw(self,amount):
#         if 0<amount<=self.balance:
#             self.balance-=amount
#             self.transaction_list.append((Account._current_time(),-amount))
#         else:
#             print("amount must be greater than zero and more than account balance")

#     def show_balance(self):
#         print("Balance is {} ".format(self.balance))

#     def show_transaction(self):
#         for date,amount in self.transaction_list:
#             if amount>0:
#                 tran_type="deposited"
#             else:
#                 tran_type="withdrawn"
#                 amount*=-1
#             print("{:6} {} on {} )".format(amount,tran_type,date))

# if __name__=='__main__':
#     tim=Account("Tim",0)
#     tim.show_balance()

#     tim.deposit(1000)
#     tim.withdraw(500)
#     tim.show_balance()
#     tim.show_transaction()

# class Song:
#     """class to represent a song
#     title(str):The title of the song
#     artist(Artist):An Artist object representing the song creator.
#     duration(int):The duration of song in seconds. may be zero

#     Attributes:
#     title(str):
#     artist(Artist):
#     duration(int):
#     """
#     def __init__(self,title,artist,duration=0):
#         """
#         song init method
#         Args:
#         title:
#         artist:
#         duration(optional)
#         """
#         self.title=title
#         self.artist=artist
#         self.duration=duration

# print(Song.__doc__)  #printing the docstring
# print(Song.__init__.__doc__)
# Song.__init__.__doc__="""updating the docstring"""
# # help(Song)
# #raw string

# a_string="this is \na string split\t\t and tabbed"
# print(a_string)

# raw_string=r"this  is \n string split \t\t and tabbed\\"
# print(raw_string)


# class Album:
#     def __init__(self,name,year,artist=None):
#         self.name=name
#         self.year=year
#         if artist is None:
#             self.artist=Artist("various Artists")
#         else:
#             self.artist=artist
#         self.tracks=[]

#     def add_song(self,song,position=None):
#         if position is None:
#             self.tracks.append(song)
#         else:
#             self.tracks.insert(position,song)


# from tkinter import Y
# from traceback import print_tb
# from unittest import result


# class A:
#     def test1(self):
#         print("method named test1 of A called")


# class B(A):
#     def test1(self):
#         print("method named test1 of B called")
#         # super().test1()


# class C(A):
#     def test1(self):
#         print("method named test1 of C called")
#         super().test1()


# class D(B,C):
#     def test2(self):
#         print("method named test2 of D called") 


# object1 = D()
# object1.test1()

# class A:    
#     def __init__(self):
#         print("init of A called") 
# class B:
#     def __init__(self):
#         print("init of B called")

# class C(B,A):
#     def __init__(self):
#         super().__init__()

# c = C()

# class Student:
    
#     def __init__(self,name):
#         self._name = name
        
# class Student1(Student):
#     def __init__(self,name):
#         super().__init__(name)

# s = Student("saif")
# print(s._name)

# class Base:

#     def __init__(self):
#         self.multiply(10)
#         print(self.i)

#     def multiply(self, I):
#         self.i = 5 * I

# class Derived(Base):

#     def __init__(self):
#         super().__init__()

#     def multiply(self, I):
#         self.i = 3 * I

# obj = Derived()


