# ask user for input of a string and save it on str_manip
str_manip = input("Please enter a sentence: ")
# print out lenght of string
string_len = len(str_manip)
print(string_len)
# find last letter in the string
last = str_manip[-1]
# replace last char with @ and print
replaced_string = str_manip.replace(last, "@")
print(replaced_string)

#print last 3 char of string backwards
# save last 3 char of string as a variable
last3 = str_manip[string_len -3 : ]
# reverse last 3 char
last3_reverse = last3[::-1]
#print last 3 char
print(last3_reverse)

# 5 letter word first 3 char and last 2 char of string
#find first 3 char and save it to variable
first3 = str_manip[:3]
#print(first3)
# find last 2 char of string and savet it variable
last2 = str_manip[-2: ]
#print(last2)
# print 5 letter word
print(f"{first3}{last2}")


