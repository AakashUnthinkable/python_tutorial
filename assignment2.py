# 1. Access value 20 from the tuple
tuple1 = ("Test", [11, 17, 19], (1, 9, 29))
# Result : 17
print(tuple1[1][1])

# 2. Counts the number of occurrences of each item from a tuple


tuple1 = (50, 10, 60, 70, 50)
for item in tuple1:
    print(f"{item} : {tuple1.count(item) }")

# 3.Convert two lists into a dictionary
list1=[1,2,3,4]
list2=['one','two','three','four']
mydict={}
for key in list1:
    for value in list2:
        mydict[key]=value
        list2.remove(value)
        break
print(mydict)

#alternative method
# mydict={list1[i]:list2[i] for i in range(len(list1))}
# print(mydict)

# 4.Merge two Python dictionaries into one
dict1={
    1:'one',
    2:'two',
    3:'three',
}

dict2={
    4:'four',
    5:'five',
    6:'six',
}

dict1.update(dict2)
print(dict1)

# 5.Create a dictionary by extracting the keys from a given dictionary
sample_dict = {"name": "Rey","age": 25,"salary": 1000, "city": "New york"}
# Keys to extract keys = ["name", "salary"]

mydict=dict((key,sample_dict[key]) for key in ["name", "salary"])
print(mydict)