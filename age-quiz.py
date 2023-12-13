# user will input a data and program will output a response accordingly
age = int(input("Please enter your age: "))
# if user is older than 100 he is dead
if age >= 101 :
    print("Sorry, you're dead!")
# if user is between 40 and 64 he is over the hill
elif age >= 40 and age <= 64 :
    print("You're over the hill.")
# if user is under 13 he qualifies for discount
elif age <= 12 :
    print("You qualify for the kiddie discount.")
# if user is between 65 and 100 he is enjoying retirement
elif age >= 65 and age <= 100 :
    print("Enjoy retirement.")
# if user is 21, happy 21st
elif age == 21 :
    print("Congrats on your 21st!")
# for any other age print age is just a number.
else :
    print("Age is just a number.")
    
    
