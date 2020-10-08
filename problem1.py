#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
mylist = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(mylist)
a = str(input("Choose a person from the list to replace:")).strip()
b = str(input("Enter the replacement:")).strip()

c = mylist.index(a)
mylist.insert(c,b)
mylist.remove(a)
print(mylist)
