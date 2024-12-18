names = ['Juan', 'Brissa', 'Misael', 'Adriel']
for name in names:
    print(f"Hola {name}")
#------------------------------------------------------------------------------------
letter_list = ['a', 'e', 'i', 'o', 'u']
for letter in letter_list:
    letter_number = letter_list.index(letter) + 1 #Makes letter_numbers and says index value is index letter + 1
    print(f"{letter_number}: {letter}")
#------------------------------------------------------------------------------------
names2 = ['Adriel', 'Isai', 'Brissa', 'Itzel', 'Misael', 'Angela']
for name in names2: 
    if name.startswith('A'): #For know if name starts with A
        print(name)
    else:
        print('Nombre que no comienza con A')
#------------------------------------------------------------------------------------
numbers = [1,2,3,4,5]
my_value = 0
for number in numbers:
    my_value = my_value + number
    print(f"If print is inside the for, it shows: {my_value}")
print(f"If print is at the same level of for it shows: {my_value}")
#------------------------------------------------------------------------------------
word = 'Python'
for letter in word:
    print(letter)
#------------------------------------------------------------------------------------
for number in [1,2,3]:
    print(number)
#------------------------------------------------------------------------------------
for a,b in [[1,2], [3, 4], [5, 6]]:
    print(a)
    print(b)
#------------------------------------------------------------------------------------
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for item in dic.items():
    print(item)
#------------------------------------------------------------------------------------
dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

for a,b in dic.items():
    print(a,b)