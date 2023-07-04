age = int(input("Enter age:"))
ch = int(input("Enter number of children:"))

if age > 25 and ch > 2 and age <= 55: #True if all conditions are true
    print("You are parent, Yay!")
    print(f"Next year you'll be  {age+1} y.o!")
elif age < 55 and ch > 0:
    print("You're slowly getting older. Hope they'll support you")
elif age < 18 and ch == 0: #One or both need to be true
    print("You still have time for kids")
else:
    print("None of the conditions worked")
