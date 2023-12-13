# user input name of fav rest and save into variable called string_fav
string_fav = input("Please enter the name of your favourite restaurant: ")
int_fav = int(input("Please enter your favourite number:"))
print(string_fav)
print(int_fav)
string_int = int(string_fav)
print(string_int)
'''  ValueError as string cannot be parsed into an integer because it does not contain any
numbers, if string was only numbers it could be parsed into integer.'''