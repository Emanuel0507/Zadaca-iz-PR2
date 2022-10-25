"""Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)"""

import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']

rjecnik={}
for ime in imena:
    ocjena = random.randint(1, 5)
    rjecnik[ime] = ocjena
  
ocjene = rjecnik.values()
ocjene_lista = list(ocjene)
brojevi = str(ocjene_lista)
brojevi = brojevi.replace(',', '').replace(' ','').replace('[', '').replace(']', '')

ocjena_rjecnik = {}

for broj in brojevi:
    if broj in ocjena_rjecnik:
        ocjena_rjecnik[broj] += 1
    else:
        ocjena_rjecnik[broj] = 1

for broj in ocjena_rjecnik:
    print("Ocjena", broj, "se pojavljuje", ocjena_rjecnik[broj], "puta")

num = brojevi
numbers = list(num)
i = len(numbers)
numbers = map(int, numbers)
suma = sum(numbers)
print("Prosjek iznosi:", suma/i)

pos = ocjene_lista
y = len(pos)
x = 0
for b in pos:
    if b > 1:
        x += 1

rez = (100/y)*x
print("Postotak prolaznosti iznosi: ", rez,"%")










    










