#Declare empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["chocolate", "pizza", "doughnouts", "subway"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[-4])
#Print some items off the list
print(yummy[0:4:2])
#Add elements to our list (expand it) - adding at the end of the list
print(bleh)
bleh.append("spinach")
bleh.append("brocolli")
bleh.append("aubergine")
bleh.append("pesto")
print(bleh)
#Add items to a list (multiple items)
bleh.extend(["liver", "bigos", "tomatoes"])
print(bleh)
#Remove item from a list
if "bigos" in bleh:
    bleh.remove("bigos")
print(bleh)