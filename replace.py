# save sentence as a single string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# replace the ! with blank spaces using replace command
replace_string = sentence.replace("!", " ")
# print new replaced string
print(replace_string)
# print the replaced string using upper() command
upper_string = replace_string.upper()
print(upper_string)
#print sentence in reverse using slicing method
reverse_string = upper_string[::-1]
print(reverse_string)