h = input("Are you happy?")
k = input ("Do you know it?")

if h == "yes" and k == "yes":
    print("Clap your hands")
elif h == "yes" and k == "no":
    print("Appreciate what you have =, you're ungrateful'...")
elif h == "no" and k.lower() == "yes":
    print("It'll get better!")
else:
    print("Seek help - let's talk")
print("Glad you're here")