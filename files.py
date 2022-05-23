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

# with open('aakash.txt','r') as aakash:
#     all_lines=aakash.readline().rstrip()    # we will single line as string

# print(all_lines) 

# for character in reversed(all_lines):
#     print(character,end='')

# print()
# # strip, istrip and rstrip
# char='"'
# no_quotes=all_lines.strip(char)
# print(no_quotes)

# char='". Myh'
# check=all_lines.strip(char)  #strip check the charater in start and end.
# #if that character is present then it will remove it
# print(check)

# # removeprefix and removesuffix method ->added in python 3.9 so we will write function for this

# def removeprefix(string,prefix):
#     if string.startswith(prefix):
#         return string[len(prefix):]
#     else:
#         return string[:]

# def removesuffix(string,suffix):
#     if suffix and string.endswith(suffix):
#         return string[:-len(suffix)]
#     else:
#         return string[:]

# # p_removed=all_lines.removeprefix('". Myh')  this is not available in python 3.8
# # s_removed=all_lines.removesuffix('gh. "')   this is not available in python 3.8

# print()
# p_removed=removeprefix(all_lines,'"My ')
# s_removed=removesuffix(all_lines,'gh."')
# print(p_removed)
# print(s_removed)

# #parsing -> making sense of data

# countries={}
# input_filename='country_info.txt'
# with open(input_filename) as file:
#     file.readline()     #for loop will start from second line as we have already read first line
#     for row in file:
#         data=row.strip('\n').split('|')
#         country,capital,cc,cc3,iac =data
#         # print(country,capital,cc,cc3,iac)
#         # print(data) 
#         country_dict={
#             'name':country,
#             'capital':capital,
#             'country_code':cc,
#             'cc3':cc3,
#             'iac':iac,
#         }
#         print(country_dict)
#         countries[country.casefold()]=country_dict

# print(countries)

# data={
#     'neem','mango','peepal','banyan','sandalwood'
# }

# # with open('tree.txt','w') as plants:     #print method convert object into string 
# #     for plant in data:
# #         print(plant,file=plants)

# with open('tree.txt','w') as plants:       #write method write as it is
#     for plant in data:
#         plants.write(plant)

# # with open('tree.txt','w') as plants:       #not give error as print convert int to string
# #     for i in range(10):
# #         print(i,file=plants)
                
# with open('tree.txt','w') as plants:       #will give error if we not typecast int to string
#     for i in range(10):
#         plants.write(str(i))

# # with open('tree.txt',encoding='utf-8') as jabber:  we should provide correct encoding 

#serializing data using json -> data into a format which can be stored or transmitted

#JSON is standard format for saving and interchanging data

# import json

# language=[
#     ['ABC',1987],
#     ['Algol 68',1968],
#     ['APL',1962],
#     ['c',1973],
#     ['Perl',1987],
# ]

# #json does not support tuple
 
# # with open('test.json','w',encoding='utf-8') as testfile:
# #     json.dump(language,testfile) 

# with open('test.json','r',encoding='utf-8') as testfile:
#     data=json.load(testfile)
# print(data)
# print(data[2])

# import urllib.request
# json_data_source='https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'

# with urllib.request.urlopen(json_data_source) as json_stream:
#     anomalies=json.load(json_stream)

# for year,value in anomalies['data'].items():
#     year,value=int(year),float(value)
#     print(f'{year} ... {value:6.2f} ')
     

# csv- comma seperated value
# import csv
# csv_filename='OlympicMedals_2020.csv'

# with open(csv_filename,encoding='utf-8',newline='') as csv_file:
#     header=csv_file.readline().strip('\n').split(',')
#     print(f'column header: {header}')
#     reader=csv.reader(csv_file)
#     for row in reader:
#         print(row)

# #To read csv file with different delimiter we can use csv.reader(countries_data,delimiter='|')
# #sniffer and dialect in csv ->check it out again

# #creating csv file
# cereals=[
#     ["Barley",556,1.7,32.9,10.1,13.8],
#     ["Durum",669,5,27.4,4.09,9.7],
#     ["rice",346,2.8,38.1,9.9,0.8],
#     ["wheat",407,1.2,27.8,12.9,13.8],
# ]
# column_heading=["cereal","calories","fat","protein","fibre","vitamin E"]
# output_filename="my_cereals.csv"

# with open(output_filename,'w',encoding='utf-8',newline='') as output_file:
#     # writer=csv.writer(output_file)
#     writer=csv.writer(output_file,quoting=csv.QUOTE_NONNUMERIC) #for quoting non-numeric value
#     writer.writerow(column_heading)
#     writer.writerow(cereals)

# #csv dictreader

# with open('my_cereals.csv',encoding='utf-8',newline='') as cereal_file:
#     reader=csv.DictReader(cereal_file)
#     for row in reader:
#         print(row)

#csv dictwrite
# import csv
# medals_table=[
#     {'country':'United States','gold':39,'silver':41,'bronze':33,'rank':1},
#     {'country':'China','gold':38,'silver':32,'bronze':18,'rank':2},
#     {'country':'Japan','gold':27,'silver':14,'bronze':17,'rank':3},
#     ]

# def sort_key(d:dict)->str:
#     return d['country']

# columns=['country','gold','silver','bronze']
# filename='country_medal.csv'
# with open(filename,'w',encoding='utf-8',newline='') as output_file:
#     writer=csv.DictWriter(output_file,fieldnames=columns,extrasaction='ignore')
#     writer.writeheader()
    # for row in medals_table:
    #     writer.writerow(row)
    # writer.writerows(sorted(medals_table,key=sort_key))

#zip function
#dictwriter is used when data is in dictionary format
 
# import csv


# albums=[("welcome to my nightmare","alice cooper",1975),
#         ("bad company","bad company",1974),
#         ("nightflight","budgie",1981),
# ]
# keys=['album','artist','year']

# filename='albums.csv'
# with open(filename,'w',encoding='utf-8',newline='') as csv_file:
#     writer = csv.DictWriter(csv_file,fieldnames=keys)
#     writer.writeheader()
#     for row in albums:
#         zip_object=zip(keys,row)
#         album_dict=dict(zip_object)
#         print(album_dict)
#         writer.writerow(album_dict)

