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

 
class Account:
    """Simple account class with balance"""

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print("Account created for "+self.name)

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount>0:
            self.balance-=amount

    def show_balance(self):
        print("Balance is {} ".format(self.balance))












