#  1. Write all the contents of a given file to new file.
#   - Read data from file
#   - Write date from one file to another
#   - Display content written in new file

with open("aakash.txt",'r') as text_file:
    data=text_file.read()

with open("new_file.txt","w+") as f:
    f.write(data)
    f.seek(0)          #move file pointer again to the beginning
    new_data=f.read()
    print(new_data)


 
#  2. Read a file and return the count of letters in a text file

# with open("aakash.txt","r") as text_file:
#     word_list=text_file.read()
#     count=0
#     for character in word_list:
#         if character.isalpha():
#             count+=1
#     print(count)

 
#  3. Read a file and check whether the word exists in a text file or not.

# with open("aakash.txt","r") as text_file:

#     all_lines=text_file.read()  # get text as string
#     # all_lines=all_lines.split() # converting string to list
#     # print(all_lines)
#     word_to_find="python"
#     if word_to_find in all_lines:
#         print(f"{word_to_find} is present in text file")
#     else:
#         print(f"{word_to_find} is not present in text file")
    
 
#  4. Write a  program to create a dictionary by asking student name and their grades. And then enter name to print grade of the student.

# student_dict={}
# while True:
#     student_name=input("enter the student name : ")
#     student_grade=input(f"enter {student_name}'s grade : ")
#     student_dict[student_name]=student_grade
#     print("want to add more student y/n : ")
#     check=input()
#     if(not (check=='y' or check=='Y')):
#         break
# check=input("enter student name to check grade: ")
# print(student_dict[check])

#  5. Concatenate multiple dictionary in one

# dict1={1:'one',2:'two',3:'three'}
# dict2={4:'four',5:'five',6:'six'}
# dict3={7:'seven'}
# # dict1.update(dict2)
# dict4={**dict1,**dict2,**dict3} #unpacking
# print(dict4)