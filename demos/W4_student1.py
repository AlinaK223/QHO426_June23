def generate():
    name = input("Enter name:")
    mrk = float(input("Enter the mark: "))
    return name, mrk

def list_of_studs(n):
    stud_list = []
    for i in range (n):
        stud_list.append(generate())
    return stud_list
#that means 3 times will be generated the column 9
print(list_of_studs(3))
