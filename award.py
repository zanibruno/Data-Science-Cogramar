cycling_time = int(input("How many minutes did you take to complete cycling? "))
running_time = int(input("How many minutes did you take to complete running? "))
swimming_time = int(input("How many minutes did you take to complete swimming? "))

total_time = cycling_time + running_time + swimming_time
print(f"You have taken {total_time} minutes to complete the triathlon!")

if total_time <= 100 :
    print("You have received Provincial Colours award!")
elif total_time >= 101 and total_time <= 105 :
    print("You have receive Provincial Half Colours award!")
elif total_time >= 106 and total_time <= 110 :
    print("You have received Provincial Scroll award!")
else :
    print("You have received no award!")
