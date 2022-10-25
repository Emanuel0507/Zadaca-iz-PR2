"""Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra."""
def num():
    for a in range (2, 100, 2):
        yield a
    for b in range (1, 100, 2):
        yield b     

gen = num()

for a in gen:   
    print(a)
for b in gen:
    print(b)





