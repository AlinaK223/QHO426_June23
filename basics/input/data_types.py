name = input("Enter your name:")
age = int(input("Enter your age:"))
h = int(input("Enter your height:"))
w = int(input("Enter your weight:"))

bmi = w/(h*h)

print(f"{name} you are {age}years old and your BMI is {bmi}")