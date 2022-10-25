"""
Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj ostvarenih ocjena. 
"""
from csv import reader

with open('rezultati.csv', 'r', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    studenti = list(csv_reader)
  
studenti.sort(key=lambda x: x[1])

print("Polozili su:")
for ime, prezime, bodovi in studenti:
    if (int(bodovi)>49):
        print (ime, prezime)
total = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
for ime, prezime, bodovi in studenti:
    if int(bodovi) >= 90:
        total += 1   
    if int(bodovi) >= 80 and int(bodovi) < 90:
        total2 += 1
    if int(bodovi) >= 65 and int(bodovi) < 80:
        total3 += 1
    if int(bodovi) >= 50 and int(bodovi) < 65:
        total4 += 1
    if int(bodovi) >= 0 and int(bodovi) < 50:
        total5 += 1

ocjene = {
    "izvrstan": total,
    "vrlo dobar": total2,
    "dobar": total3,
    "dovoljan": total4,
    "nedovoljan": total5
}
print (ocjene)



