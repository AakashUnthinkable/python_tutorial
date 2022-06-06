# DATABASE - python include SQLite in standard library

# import sqlite3

# db=sqlite3.connect("contacts.sqlite")

# db.execute("create table if not exists contacts(name text,phone integer,email text)")
# db.execute("insert into contacts(name,phone,email) values('Tim',65789,'tim@email.com')")
# db.execute("insert into contacts values('Brian',1234,'brian@email.com')")

# cursor=db.cursor()
# cursor.execute("select * from contacts")
# print(cursor.fetchall())
# print(cursor.fetchone())
# for name,phone,email in cursor:
#     print(name,phone,email)

# for name,phone,email in cursor:
#     print(name,phone,email)
# cursor.close()
# db.commit()     #if we not commit then sql commands will be rolled down

# update_sql="update contacts set email='update@update.com' where contacts.phone=1234"
# update_cursor=db.cursor()
# update_cursor.execute(update_sql)
# print("{} rows updated".format(update_cursor.rowcount))
# update_cursor.connection.commit()  # we can commit cursor using connection methods
# update_cursor.close()

# new_email="newemail@update.com"
# phone=input("Please enter the phone number")
# update_sql="update contacts set email=? where phone=?"
# print(update_sql)
# update_cursor=db.cursor()
# update_cursor.execute(update_sql,(new_email,phone))
# update_cursor.connection.commit()
# update_cursor.close()
# for name,phone,email in db.execute("select * from contacts"):
#     print(name,phone,email)

# check=input("enter your name : ")
# # sql_check="select * from contacts where contacts.name=?"
# sql_check="select * from contacts where contacts.name like ?"
# check_cursor=db.cursor()
# check_cursor.execute(sql_check,(check,))
# for row in check_cursor:
#     print(row)

# db.close()



#Exceptions

# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# try:
#     # print(factorial(1000))
#     print(9/0)
# except RecursionError:
#     print("This program can't calculate large factorial")
# # except ZeroDivisionError:
# #     print("why are you dividing by zero ")
# except (RecursionError , ZeroDivisionError):
#     print("one of the error occured ")
# except :
#     print("some error occurred")
# finally:
#     print("program terminated")

import sys

def getint(prompt):
    while True:
        try:
            number=int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered , please try again ")
        except EOFError:
            sys.exit(0)

first_number=getint("Please enter first number ")
second_number=getint("Please enter second number ")

try:
    print("{} divided by {} is {}".format(first_number,second_number,first_number/second_number))
except ZeroDivisionError:
    print("you can't divide by zero") 