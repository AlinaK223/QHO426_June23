#Declare a tuple
x = ("Alina", 12, True)
y = tuple(["Gary", 23, False])
#Print tuples
print(x)
print(y)
print(x[2])
print(y[0:2])
#Cannot change individual items (imutability)
#x[1] += 1

#Concatenate
z = x + 1
print(z)
print(x)
print(y)




#Use min and max functions on tuples
t = (74, 35, 1, 83, 65, 62)
print(max(t))
print(min(t))

#Fixing errors on tuples
print (x)
L1 = list(x)
L1[2] = False
x = tuple(l1)
peint(x)
