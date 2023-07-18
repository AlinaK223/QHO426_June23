def generate():
    name = input("Enter name:")
    mrk = float(input("Enter the mark: "))
    return name, mrk

print(generate())
x = generate()
print(x)
print(type(x))