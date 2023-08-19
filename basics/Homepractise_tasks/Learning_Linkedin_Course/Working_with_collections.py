#Each item in a list is automatically assignment
#It's important to know that index numbering doesn't start at one, it's start at 0
#This system is common in a lot of programming languages
#It consists 4 pieces of data

#book1 = 'psychology'
#book2 = 'recipes'
#book3 = 'grammar'
#book4 = 'philosophy'

Books = [
    'psychology',
    'recipes',
    'grammar',
    'philosophy',
]
print(Books[1])

#I can also do this:
Books_numbers = {
    'book1': 'psychology',
    'book2': 'recipes',
    'book3': 'grammar',
    'book4': 'philosophy',
}
print(Books_numbers['book3'])

#Collections provide a way of creating organized code while still allowing you to work with individuals values within them pretty easily