"Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada."

def string(a):
    if not type(a) == str:
        return 0
    else:
        return a[::-1]

rez = string("Lopta")
print(rez)



