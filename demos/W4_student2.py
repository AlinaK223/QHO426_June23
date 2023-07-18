def generate():
    name = input("Enter name:")
    mrk = float(input("Enter the mark: "))
    return name, mrk

def list_of_studs(n):
    stud_list = []
    for i in range (n):
        stud_list.append(generate())
    return stud_list

def average(lista = []):
    total = 0
    for tup in lista:
        total += tup[1]
    avg = total/len(lista)
    return avg

print(average(list_of_studs(3)))

